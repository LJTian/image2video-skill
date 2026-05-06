#!/usr/bin/env python3
"""Validate this skill repository without third-party dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_AGENT_FIELDS = ("display_name", "short_description", "default_prompt")
SKILL_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}$")


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")

    try:
        end = lines[1:].index("---") + 1
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter must close with ---") from exc

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"\'')
    return metadata


def parse_interface_yaml(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "interface:":
        raise ValueError(f"{path.name} must start with interface:")

    values: dict[str, str] = {}
    for line in lines[1:]:
        if not line.strip():
            continue
        match = re.fullmatch(r"\s{2}([A-Za-z_][A-Za-z0-9_]*):\s*(.+)", line)
        if not match:
            raise ValueError(f"{path.name} has unsupported YAML line: {line}")
        key, value = match.groups()
        values[key] = value.strip().strip('"\'')
    return values


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    skill_md = root / "SKILL.md"
    agent_yaml = root / "agents" / "openai.yaml"

    if not skill_md.is_file():
        errors.append("missing SKILL.md")
    if not agent_yaml.is_file():
        errors.append("missing agents/openai.yaml")
    if errors:
        return errors

    try:
        metadata = parse_frontmatter(skill_md)
    except ValueError as exc:
        errors.append(str(exc))
        metadata = {}

    name = metadata.get("name", "")
    if not name:
        errors.append("SKILL.md frontmatter missing name")
    elif not SKILL_NAME_RE.fullmatch(name):
        errors.append("SKILL.md name must use lowercase letters, digits, and hyphens")

    if not metadata.get("description", ""):
        errors.append("SKILL.md frontmatter missing description")

    for rel_path in ("agents/openai.yaml", "agents/openai.zh-CN.yaml"):
        path = root / rel_path
        if not path.exists():
            continue
        try:
            fields = parse_interface_yaml(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        for field in REQUIRED_AGENT_FIELDS:
            if not fields.get(field):
                errors.append(f"{rel_path} missing interface.{field}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "skill_dir",
        nargs="?",
        default=".",
        help="Path to the skill directory, default: current directory",
    )
    args = parser.parse_args()

    root = Path(args.skill_dir).resolve()
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("OK: skill validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
