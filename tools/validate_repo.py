"""Repository validator for the sales-agent-foundation.

Asserts the contracts in SPEC.md section 9. Python standard library only, no
dependencies, no network. Run it before every commit:

    python tools/validate_repo.py

Exit code 0 means every check passed. Exit code 1 means at least one error.
Warnings never fail the run.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parent.parent

AGENTS_DIR = REPO_ROOT / ".github" / "agents"
PROMPTS_DIR = REPO_ROOT / ".github" / "prompts"
SKILLS_DIR = REPO_ROOT / ".github" / "skills"
CATALOG_PATH = REPO_ROOT / ".github" / "AGENT-CATALOG.md"

# Lifecycle personas describe how changes to this repo are made. They are not
# revenue workflows, so they are exempt from prompt parity and use a lighter
# section contract.
LIFECYCLE_AGENTS = {"spec", "plan", "build", "validate", "code-reviewer"}

TASK_AGENT_SECTIONS = [
    "## When to activate",
    "## What it resolves (never hardcode)",
    "## Process",
    "## Output",
    "## Guardrails",
    "## Anti-patterns",
]

LIFECYCLE_AGENT_SECTIONS = ["## When to activate", "## Process", "## Output"]

# Binary formats we cannot usefully scan as text. Everything else is scanned,
# so a new file extension is checked by default rather than silently skipped.
BINARY_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip", ".gz",
    ".woff", ".woff2", ".ttf", ".otf", ".eot", ".mp4", ".mov", ".xlsx",
    ".pptx", ".docx", ".pyc", ".so", ".dll", ".exe",
}

MAX_GITHUB_FILE_BYTES = 60 * 1024

EM_DASH = "\u2014"
EN_DASH = "\u2013"

# Placeholder domains are allowed so docs can show what an address looks like.
# Matched as a whole domain, never as a suffix, so `badexample.com` is caught.
ALLOWED_EMAIL_DOMAINS = frozenset(
    {
        "example.com",
        "example.org",
        "example.net",
        "yourcompany.com",
        "noreply.github.com",
        "users.noreply.github.com",
    }
)

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b")
GUID_RE = re.compile(
    r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b"
)
# A 32 character hex run is a hyphenless GUID or a hash. Either way it does not
# belong in prose. Bounded by non-hex so a longer hex blob still trips it.
BARE_HEX_RE = re.compile(r"(?<![0-9a-fA-F])[0-9a-fA-F]{32,}(?![0-9a-fA-F])")

# Pinning a GitHub Action to a commit SHA is a supply-chain best practice, so a
# 40 character hex on a `uses:` line is expected rather than a leak.
ACTION_PIN_RE = re.compile(r"^\s*-?\s*uses:\s*\S+@[0-9a-f]{40}\b")

_NOT_A_SECRET = r"(?!<|\$\{|your[-_ ]|placeholder|example|redacted|xxx|\.\.\.|TODO)"

SECRET_PATTERNS = [
    # key: value style assignments
    re.compile(
        r"(?i)\b(api[_-]?key|client[_-]?secret|access[_-]?token|auth[_-]?token"
        r"|secret[_-]?key|password|passwd|connection[_-]?string)\s*[:=]\s*"
        rf"[\"']?{_NOT_A_SECRET}\S{{12,}}"
    ),
    re.compile(rf"(?i)\bbearer\s+{_NOT_A_SECRET}[A-Za-z0-9._-]{{20,}}"),
    # PEM blocks
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    # JWTs
    re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),
    # Connection strings carrying an inline credential
    re.compile(rf"(?i)\b(AccountKey|SharedAccessSignature|Pwd|Password)=\s*{_NOT_A_SECRET}\S{{12,}}"),
    # Common vendor token prefixes
    re.compile(r"\b(gh[pousr]_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|sk-[A-Za-z0-9]{20,})"),
]

# [text](target). Also matches ![alt](target), which we check identically.
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(\s*(<[^>]+>|[^)\s]+)")

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)

FENCE_RE = re.compile(r"^\s{0,3}(```|~~~)")

# A description is the routing contract, so it must read as a third-person
# statement of what the agent does. These openings mean it was written as an
# instruction or from the runner's point of view instead.
IMPERATIVE_OPENINGS = {
    "analyse", "analyze", "build", "check", "create", "draft", "find",
    "generate", "give", "help", "identify", "inspect", "keep", "make",
    "map", "produce", "prep", "read", "resolve", "review", "roll", "run",
    "score", "show", "sweep", "turn", "update", "write",
}


@dataclass
class Report:
    """Collects errors and warnings, keyed by check name."""

    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, check: str, path: Path, message: str, line: Optional[int] = None) -> None:
        where = _rel(path) + (f":{line}" if line else "")
        self.errors.append(f"[{check}] {where}: {message}")

    def warn(self, check: str, path: Path, message: str, line: Optional[int] = None) -> None:
        where = _rel(path) + (f":{line}" if line else "")
        self.warnings.append(f"[{check}] {where}: {message}")


def _rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str, strict_keys: tuple[str, ...] = ()) -> Optional[dict]:
    """Parse a flat `key: value` YAML frontmatter block.

    Returns None if there is no frontmatter. Returns a dict that may carry a
    special `__errors__` list describing malformed content, because silently
    accepting broken frontmatter is how an agent stops being routable without
    anyone noticing.

    Keys listed in `strict_keys` must be single-line scalars. A continuation
    line under one of them is an error, since the routing contract depends on
    the description being one line.
    """
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None

    data: dict = {}
    problems: list[str] = []
    key: Optional[str] = None

    for number, raw in enumerate(match.group(1).splitlines(), start=2):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith((" ", "\t")):
            if key is None:
                problems.append(f"line {number}: indented line with no parent key")
            elif key in strict_keys:
                problems.append(
                    f"line {number}: `{key}` must be a single line, found a continuation"
                )
            else:
                data[key] = (str(data[key]) + " " + raw.strip()).strip()
            continue
        if ":" not in raw:
            problems.append(f"line {number}: `{raw.strip()[:40]}` is not a `key: value` pair")
            continue
        key, _, value = raw.partition(":")
        key = key.strip()
        if key in data:
            problems.append(f"line {number}: duplicate key `{key}`")
        data[key] = value.strip().strip("'\"")

    if problems:
        data["__errors__"] = problems
    return data


def _walk_all_files() -> list:
    skip_parts = {".git", "__pycache__", "node_modules", ".venv"}
    return [
        p
        for p in REPO_ROOT.rglob("*")
        if p.is_file() and not (skip_parts & set(p.parts))
    ]


def iter_text_files() -> list[Path]:
    """Every tracked text file, falling back to a full walk.

    Enumerating from `git ls-files` means a file is checked because it is
    committed, not because its extension happened to be on an allowlist. If git
    is unavailable, or the index is empty (a fresh checkout before the first
    commit), fall back to walking the tree. An empty result must never be
    treated as "nothing to check", because that would silently pass everything.
    """
    candidates: list = []
    try:
        out = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        candidates = [REPO_ROOT / n for n in out.split("\0") if n]
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        candidates = []

    if not candidates:
        candidates = _walk_all_files()

    files = []
    for path in candidates:
        if not path.is_file() or path.suffix.lower() in BINARY_SUFFIXES:
            continue
        files.append(path)
    return sorted(files)


def strip_fenced_blocks(text: str) -> str:
    """Blank out fenced code blocks, preserving line numbering.

    Required so a heading shown as an example inside a fence cannot satisfy the
    section contract, and so a sample credential in a fence is still scanned as
    text but a sample heading is not counted as structure.
    """
    lines = text.splitlines()
    out: list[str] = []
    fence: Optional[str] = None
    for line in lines:
        match = FENCE_RE.match(line)
        if fence is None and match:
            fence = match.group(1)
            out.append("")
            continue
        if fence is not None:
            if match and match.group(1) == fence:
                fence = None
            out.append("")
            continue
        out.append(line)
    return "\n".join(out)


def heading_positions(text: str) -> list[tuple[int, str]]:
    """Exact `##` headings outside fenced blocks, as (offset, heading)."""
    body = strip_fenced_blocks(text)
    found = []
    offset = 0
    for line in body.splitlines(keepends=True):
        stripped = line.strip()
        if stripped.startswith("## "):
            found.append((offset, stripped))
        offset += len(line)
    return found


def check_agents(report: Report) -> dict:
    """Checks 1, 2, 3. Returns {agent_name: frontmatter}."""
    agents: dict = {}
    if not AGENTS_DIR.is_dir():
        report.errors.append("[agents] .github/agents is missing")
        return agents

    for path in sorted(AGENTS_DIR.glob("*.agent.md")):
        stem = path.name[: -len(".agent.md")]
        text = _read(path)
        front = parse_frontmatter(text, strict_keys=("name", "description"))
        if front is None:
            report.error("agent-frontmatter", path, "missing YAML frontmatter block")
            continue
        for problem in front.pop("__errors__", []):
            report.error("agent-frontmatter", path, f"malformed frontmatter, {problem}")
        name = front.get("name", "")
        description = front.get("description", "")
        if not name:
            report.error("agent-frontmatter", path, "frontmatter has no `name`")
        elif name != stem:
            report.error(
                "agent-frontmatter", path, f"`name: {name}` does not match filename stem `{stem}`"
            )
        if not description:
            report.error("agent-frontmatter", path, "frontmatter has no `description`")
        elif len(description) < 40:
            report.error(
                "agent-description",
                path,
                f"description is {len(description)} chars, needs at least 40 with trigger phrases",
            )
        else:
            first = re.split(r"[^A-Za-z]", description.strip(), maxsplit=1)[0].lower()
            if first in IMPERATIVE_OPENINGS:
                report.error(
                    "agent-description",
                    path,
                    f"description opens with the imperative `{first}`, the routing contract "
                    f"must be third person (`{first}s ...`)",
                )
            # Trigger phrases are quoted examples of what a human says, so
            # first person inside quotes is correct and expected. Only the
            # agent's own narration must be third person.
            narration = re.sub(r"\"[^\"]*\"|'[^']*'", " ", description)
            if re.search(r"\b(my|me)\b|\bI\b", narration):
                report.error(
                    "agent-description",
                    path,
                    "description narration is written in first person, it must describe the "
                    "agent in third person (first person belongs in quoted trigger phrases "
                    "and in the prompt)",
                )

        required = (
            LIFECYCLE_AGENT_SECTIONS if stem in LIFECYCLE_AGENTS else TASK_AGENT_SECTIONS
        )
        headings = heading_positions(text)
        by_text = {heading: offset for offset, heading in headings}
        positions = []
        for heading in required:
            if heading not in by_text:
                report.error("agent-sections", path, f"missing required section `{heading}`")
            else:
                positions.append((by_text[heading], heading))
        if len(positions) == len(required) and positions != sorted(positions):
            got = " then ".join(h for _, h in sorted(positions))
            report.error("agent-sections", path, f"sections out of order, found: {got}")

        agents[stem] = front
    return agents


def check_prompts(report: Report, agents: dict) -> set:
    """Checks 4, 5, 6. Returns the set of prompt stems."""
    prompts: set = set()
    if not PROMPTS_DIR.is_dir():
        report.errors.append("[prompts] .github/prompts is missing")
        return prompts

    for path in sorted(PROMPTS_DIR.glob("*.prompt.md")):
        stem = path.name[: -len(".prompt.md")]
        prompts.add(stem)
        text = _read(path)
        front = parse_frontmatter(text, strict_keys=("mode", "description"))
        if front is None:
            report.error("prompt-frontmatter", path, "missing YAML frontmatter block")
            continue
        for problem in front.pop("__errors__", []):
            report.error("prompt-frontmatter", path, f"malformed frontmatter, {problem}")
        if front.get("mode") != "agent":
            report.error("prompt-frontmatter", path, "frontmatter needs `mode: agent`")
        if not front.get("description"):
            report.error("prompt-frontmatter", path, "frontmatter has no `description`")

        recommended = re.search(r"Recommended agent:\s*\*\*([a-z0-9-]+)\*\*", text)
        if not recommended:
            report.error(
                "prompt-agent-link",
                path,
                "body must name its agent as `Recommended agent: **<name>**`",
            )
        elif recommended.group(1) not in agents:
            report.error(
                "prompt-agent-link",
                path,
                f"names agent `{recommended.group(1)}`, which has no file in .github/agents",
            )
        elif recommended.group(1) != stem:
            report.error(
                "prompt-agent-link",
                path,
                f"stem is `{stem}` but recommends agent `{recommended.group(1)}`",
            )

        if stem not in agents:
            report.error("agent-prompt-parity", path, f"no agent `{stem}.agent.md` for this prompt")

    for name in sorted(agents):
        if name in LIFECYCLE_AGENTS:
            continue
        if name not in prompts:
            report.error(
                "agent-prompt-parity",
                AGENTS_DIR / f"{name}.agent.md",
                f"no reusable prompt `.github/prompts/{name}.prompt.md`",
            )
    return prompts


def check_skills(report: Report) -> set:
    """Check 7. Returns the set of skill names."""
    skills: set = set()
    if not SKILLS_DIR.is_dir():
        report.errors.append("[skills] .github/skills is missing")
        return skills

    for directory in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            report.error("skill-shape", directory, "skill directory has no SKILL.md")
            continue
        front = parse_frontmatter(_read(skill_file), strict_keys=("name", "description"))
        if front is None:
            report.error("skill-frontmatter", skill_file, "missing YAML frontmatter block")
            continue
        for problem in front.pop("__errors__", []):
            report.error("skill-frontmatter", skill_file, f"malformed frontmatter, {problem}")
        name = front.get("name", "")
        if name != directory.name:
            report.error(
                "skill-frontmatter",
                skill_file,
                f"`name: {name or '(empty)'}` does not match directory `{directory.name}`",
            )
        if not front.get("description"):
            report.error("skill-frontmatter", skill_file, "frontmatter has no `description`")
        skills.add(directory.name)
    return skills


def _parse_catalog_tables(text: str) -> list:
    """Parse every pipe table in the catalog into header-keyed row dicts."""
    rows: list = []
    headers: Optional[list] = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            headers = None
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if headers is None:
            headers = [c.lower() for c in cells]
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue
        rows.append(dict(zip(headers, cells)))
    return rows


def check_catalog(report: Report, agents: dict, skills: set) -> None:
    """Checks 8 and 9."""
    if not CATALOG_PATH.is_file():
        report.errors.append("[catalog] .github/AGENT-CATALOG.md is missing")
        return

    text = _read(CATALOG_PATH)
    listed: set[str] = set()
    for row in _parse_catalog_tables(text):
        cell = row.get("agent")
        if not cell:
            continue
        names = re.findall(r"`([a-z0-9-]+)`", cell)
        for name in names:
            listed.add(name)
            if name not in agents:
                report.error("catalog", CATALOG_PATH, f"lists agent `{name}` with no file on disk")
        for skill_name in re.findall(r"`([a-z0-9-]+)`", row.get("skills", "")):
            if skill_name not in skills:
                report.error(
                    "catalog",
                    CATALOG_PATH,
                    f"row for `{names[0] if names else '?'}` cites skill `{skill_name}`, "
                    "which has no directory in .github/skills",
                )

    for name in sorted(agents):
        if name not in listed:
            report.error("catalog", CATALOG_PATH, f"agent `{name}` is not listed in the catalog")


def check_spec_agrees_with_catalog(report: Report, agents: dict) -> None:
    """Check 15: SPEC.md section 6 must name the same groups as the catalog.

    Two lists of agents that can disagree is how a catalog rots. The spec names
    groups and their agents in a table, the catalog names them in per-group
    tables, and they must not drift apart.
    """
    spec_path = REPO_ROOT / "SPEC.md"
    if not spec_path.is_file() or not CATALOG_PATH.is_file():
        return

    spec_agents = set()
    for row in _parse_catalog_tables(_read(spec_path)):
        cell = row.get("agents") or row.get("agent")
        if not cell:
            continue
        spec_agents.update(re.findall(r"`([a-z0-9-]+)`", cell))

    if not spec_agents:
        report.error("spec-catalog", spec_path, "no agent table found in SPEC.md section 6")
        return

    missing_from_spec = sorted(set(agents) - spec_agents)
    unknown_in_spec = sorted(spec_agents - set(agents))
    for name in missing_from_spec:
        report.error("spec-catalog", spec_path, f"agent `{name}` exists but SPEC.md omits it")
    for name in unknown_in_spec:
        report.error("spec-catalog", spec_path, f"SPEC.md names agent `{name}`, which has no file")


def check_dashes_and_secrets(report: Report) -> None:
    """Checks 10 and 12.

    Note there is no self-exemption. This file is scanned like every other, so
    the patterns below are written to describe credentials without containing
    one.
    """
    for path in iter_text_files():
        try:
            text = _read(path)
        except (UnicodeDecodeError, OSError):
            continue
        for number, line in enumerate(text.splitlines(), start=1):
            if EM_DASH in line:
                report.error("dashes", path, "contains an em dash (U+2014)", number)
            if EN_DASH in line:
                report.error("dashes", path, "contains an en dash (U+2013)", number)
            for match in EMAIL_RE.finditer(line):
                domain = match.group(1).lower().rstrip(".")
                if domain in ALLOWED_EMAIL_DOMAINS:
                    continue
                report.error(
                    "pii", path, f"contains an email address `{match.group(0)}`", number
                )
            if GUID_RE.search(line):
                report.error("pii", path, "contains a bare GUID, use a placeholder", number)
            if BARE_HEX_RE.search(line) and not ACTION_PIN_RE.match(line):
                report.error(
                    "pii",
                    path,
                    "contains a long hex string (hyphenless GUID, hash, or key)",
                    number,
                )
            for pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    report.error("secrets", path, "looks like a hardcoded credential", number)
                    break


def check_links(report: Report) -> None:
    """Check 11."""
    for path in iter_text_files():
        if path.suffix.lower() != ".md":
            continue
        try:
            text = _read(path)
        except (UnicodeDecodeError, OSError):
            continue
        for number, line in enumerate(text.splitlines(), start=1):
            for match in MD_LINK_RE.finditer(line):
                target = match.group(1).strip()
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                if target.startswith("${") or "${input:" in target:
                    continue
                target = target.split("#", 1)[0].split("?", 1)[0]
                if not target:
                    continue
                base = REPO_ROOT if target.startswith("/") else path.parent
                resolved = (base / target.lstrip("/")).resolve()
                if not resolved.exists():
                    report.error("links", path, f"dead relative link `{target}`", number)


def check_referenced_skills(report: Report, skills: set) -> None:
    """Check 13: a skill named in backticks by an agent or prompt must exist."""
    known_non_skills = {
        "crm",
        "workplace",
        "notes",
        "web",
        "decks",
        "name",
        "description",
        "mode",
    }
    for directory in (AGENTS_DIR, PROMPTS_DIR):
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            text = _read(path)
            for match in re.finditer(r"Skills?:\s*(.+)", text):
                for skill_name in re.findall(r"`([a-z0-9-]+)`", match.group(1)):
                    if skill_name in known_non_skills or skill_name in skills:
                        continue
                    report.error(
                        "skill-reference",
                        path,
                        f"cites skill `{skill_name}`, which has no directory in .github/skills",
                    )


def check_file_sizes(report: Report) -> None:
    """Check 14, warning only."""
    github_dir = REPO_ROOT / ".github"
    if not github_dir.is_dir():
        return
    for path in sorted(github_dir.rglob("*")):
        if path.is_file() and path.stat().st_size > MAX_GITHUB_FILE_BYTES:
            kb = path.stat().st_size / 1024
            report.warn("file-size", path, f"is {kb:.0f} KB, consider splitting for readability")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="treat warnings as errors",
    )
    args = parser.parse_args()

    report = Report()
    agents = check_agents(report)
    check_prompts(report, agents)
    skills = check_skills(report)
    check_catalog(report, agents, skills)
    check_spec_agrees_with_catalog(report, agents)
    check_referenced_skills(report, skills)
    check_dashes_and_secrets(report)
    check_links(report)
    check_file_sizes(report)

    for warning in report.warnings:
        print(f"WARN  {warning}")
    for error in report.errors:
        print(f"ERROR {error}")

    print()
    print(
        f"{len(agents)} agents, {len(skills)} skills checked, "
        f"{len(iter_text_files())} text files scanned. "
        f"{len(report.errors)} error(s), {len(report.warnings)} warning(s)."
    )

    if report.errors or (args.strict and report.warnings):
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
