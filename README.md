# Image to Video Skill

This repository contains a Codex skill for planning image-to-video generation from still images, product photos, character references, concept art, or storyboards.

## Contents

```text
SKILL.md
agents/
  openai.yaml
```

## What It Does

The skill helps an agent turn a reference image into a tool-ready brief or a playable local clip. It covers:

- Source image analysis
- Visual consistency and motion planning
- Prompt, negative prompt, and timing structure
- Narration/audio for text-heavy or panel-based images
- Local `ffmpeg` assembly when no AI video model is available
- Hook -> conflict -> resolution storytelling for explainers
- Basic quality checks for common failure modes

## Usage

Invoke the skill explicitly when asking for image-to-video planning:

```text
Use $image2video to plan a short image-to-video generation from my reference image.
```

If the skill is installed in Codex's skills directory, Codex can also invoke it when the task clearly involves turning still images into video prompts, shot plans, generation briefs, or local video files.

## Installation

To make the skill discoverable by Codex, copy or symlink this directory into your Codex skills directory under the skill name `image2video`, for example:

```bash
mkdir -p ~/.codex/skills
ln -s /Volumes/data/git/image2video-skill ~/.codex/skills/image2video
```

## Validation

Required files:

- `SKILL.md`
- `agents/openai.yaml`

Validate with `quick_validate.py` if `PyYAML` is installed:

```bash
python3 /Users/ljtian-mac-mini/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Volumes/data/git/image2video-skill
```

If your Codex environment uses `RTK`, prefix shell commands with `rtk`:

```bash
rtk python3 /Users/ljtian-mac-mini/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Volumes/data/git/image2video-skill
```
