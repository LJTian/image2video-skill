# Image to Video Skill

This repository contains a Codex skill for planning image-to-video generation from still images, product photos, character references, concept art, or storyboards.

## Contents

```text
SKILL.md
agents/
  openai.yaml
```

## What It Does

The skill helps an agent turn a reference image into a tool-ready video generation brief. It covers:

- Source image analysis
- Visual consistency constraints
- Camera and subject motion planning
- Prompt and negative prompt structure
- Duration, aspect ratio, FPS, and motion-strength settings
- Quality checks for common image-to-video failure modes

## Usage

Invoke the skill explicitly when asking for image-to-video planning:

```text
Use $image2video to plan a short image-to-video generation from my reference image.
```

If the skill is installed in Codex's skills directory, Codex can also invoke it when the task clearly involves turning still images into video prompts, shot plans, or generation briefs.

## Installation

To make the skill discoverable by Codex, copy or symlink this directory into your Codex skills directory under the skill name `image2video`, for example:

```bash
mkdir -p ~/.codex/skills
ln -s /Volumes/data/git/image2video-skill ~/.codex/skills/image2video
```

## Validation

The skill has valid frontmatter and the required local files:

- `SKILL.md`
- `agents/openai.yaml`

The official `quick_validate.py` script requires `PyYAML`. If that dependency is available, validate with:

```bash
python3 /Users/ljtian-mac-mini/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Volumes/data/git/image2video-skill
```
