---
name: image2video
description: Use when turning still images, product photos, character references, concept art, or storyboards into short videos, playable local video files, narration/audio plans, image-to-video prompts, shot plans, camera motion specs, or tool-ready generation briefs.
---

# Image to Video

## Overview

Turn still images into a video plan or playable local clip. Preserve image facts first, then add motion, timing, narration, audio, subtitles, and delivery constraints.

Default rules:

- Keep identity, geometry, text, and branding stable.
- Ask only for constraints that change the result.
- Prefer plausible motion over dramatic drift.
- Use `ffmpeg` when no AI video model is available.

References:

- For playable local MP4 output, audio muxing, or `ffmpeg` fallback, read `references/local-video-assembly.md`.
- For narration, subtitles, story-driven explainers, numbered panels, or fidelity risks, read `references/story-audio-and-risk.md`.

## Workflow

1. Inspect the source image or ask for it if none is available.
2. Extract stable facts: subject, composition, pose, clothing/materials, text, light, background, style, and must-not-change details.
3. Ask only for missing constraints that affect output: duration, aspect ratio, story template, narration, voice type, background music, subtitles, motion controls, and exact text/logo/face handling.
4. Match motion to the image instead of forcing unsupported action.
5. Produce a tool-ready brief: prompt, negative prompt, timing, camera, motion, audio, subtitles, and consistency notes.
6. If building a local clip, verify the final file path and streams before reporting it.
7. For multiple options, vary only one major dimension per option.

Suggested question order:

- Story template: default to the story line template unless the user asks for another template later
- Narration: on or off
- Voice type: female anchor or male anchor only
- Background music: on or off
- Subtitles: on or off
- Motion controls: choose specific camera and subject movements
- Duration and aspect ratio: only if still unclear

## Clarifying Boundaries

Ask only when the answer changes the output:

- duration if the cut length is unclear
- aspect ratio if the platform matters or the source is ambiguous
- exact handling if text, logos, hands, or faces are present
- narration, music, subtitles, or motion controls if the user has not chosen them yet

Default story template:

- Story line: hook in the first 3 seconds with curiosity, tension, or a strong promise
- Middle: show the conflict, problem, misconception, or tradeoff
- End: explain the principle and clear the tension
- Keep the hook tied to the source image and end with one clear takeaway when useful

Other story templates are intentionally left empty for later addition.

## Image Analysis Checklist

Key checks:

- Subject: central person/object, pose, expression, shape, color, accessories
- Scene: location, depth, weather, props, signs, horizon/floor lines
- Style: photo, cinematic, anime, product render, illustration, UI, mixed media
- Lighting: direction, contrast, temperature, reflections, shadows, time
- Constraints: text, branding, face, hands, geometry, garment details
- Risk: readable text, logos, hands, transparency, reflections, patterns, mirrors

Motion by asset:

- Portrait: breathing, blink, slight turn, hair movement, push-in
- Product: slow orbit, slider move, highlight sweep, parallax, rack focus
- Landscape: clouds, water, foliage, distant movement, dolly/crane
- Illustration: layered parallax, particles, smoke/cloth drift, camera drift
- UI: clean zoom/pan/cursor/state change; do not invent interactions

Keep motion subtle unless the user asks for stylized transformation.

If the source image contains numbered panels, step labels, or numbered overlays, remove the numbering in the video by default unless the user explicitly asks to preserve it.

## Local Video Assembly

If no AI video model is available, use `ffmpeg` and verify the final file. Read `references/local-video-assembly.md` before assembling a playable video.

```bash
ffmpeg -loop 1 -i input.jpg -vf "scale=1280:720,zoompan=z='min(zoom+0.0015,1.08)':d=180:s=1280x720:fps=30,format=yuv420p" -t 6 -c:v libx264 output.mp4
```

Use H.264 MP4 with `yuv420p`. If narration exists, match each image to the audio segment and verify the final MP4 with `ffprobe`.

## Narration and Audio

If the image has readable captions, labels, or bottom text, use them as the narration source. Rewrite only for speech clarity. Read `references/story-audio-and-risk.md` for explainers, subtitles, panel sequences, or fidelity-sensitive assets.

Voice selection guidance:

- Only offer two voice types: female anchor and male anchor
- Use a female anchor voice or a male anchor voice available in the chosen tool
- If only macOS `say` is available, warn that it is less natural
- Verify voice availability before promising it

Audio handling rules:

- Do not add compression, EQ, or pitch tricks unless asked.
- Verify the chosen voice before use; if network is blocked, ask for permission.
- Use AAC in MP4.
- Lengthen video instead of rushing long narration.
- Verify the final audio stream with `ffprobe` and a non-silent check.

## Output Format

For a single generation:

```markdown
Brief:
- Duration:
- Aspect ratio:
- Visual anchors:
- Camera motion:
- Subject motion:
- Environment motion:
- Style and lighting:

Prompt:
[One dense paragraph that starts from the source image and adds precise video motion.]

Negative prompt:
[Identity drift, changed clothing/product shape, extra limbs, warped hands, unreadable text, flicker, morphing, logo distortion, camera shake if unwanted.]

Settings:
- Duration:
- FPS:
- Resolution or aspect ratio:
- Motion strength:
- Seed or consistency note:
```

For multiple shots:

```markdown
Shot 1:
- Time:
- Framing:
- Camera:
- Motion:
- Prompt:
- Continuity notes:
```

For story-driven clips, use this beat structure:

```markdown
Beat 1:
- Time:
- Goal: Hook / Conflict / Resolution
- Hook:
- Visual anchors:
- Motion:
- Narration:
- Continuity notes:
```

## Prompting Rules

- Start from the reference image: "Using the provided image as the first frame/reference..."
- Name visual anchors explicitly, especially identity, pose, outfit, product geometry, colors, logo placement, and background layout.
- Put motion verbs after anchors so the generator changes time, not identity.
- Use one camera move per short clip unless the requested result needs a sequence.
- Keep temporal language concrete: "over 5 seconds", "slow push-in", "subtle hair movement", "background lights shimmer".
- State preservation constraints positively in the prompt and failure modes in the negative prompt.
- For tools with separate fields, split prompt, negative prompt, duration, aspect ratio, motion strength, and seed.

## Tool Adaptation

When a specific image-to-video tool is named, adapt the brief to that tool's fields and limits. If the tool has unknown current limits, verify them from official documentation before claiming exact duration, resolution, pricing, model names, or availability.

If no tool is named, produce a model-neutral brief and avoid unsupported claims about any provider.

## Quality Review

Before finalizing, check that the plan:

- Preserves the source image's important visual facts.
- Contains enough motion detail for a video model, not just a static image prompt.
- Avoids conflicting camera instructions.
- Names likely failure modes in the negative prompt.
- Matches the requested platform, aspect ratio, and duration.
- Does not promise exact text, face, logo, or product fidelity unless the selected tool supports it.

For playable files, also check:

- Output path exists and points to the final file, not an intermediate.
- Video stream has expected codec, resolution, FPS, and duration.
- Audio stream exists and is non-silent when requested.
- Playback compatibility uses H.264 MP4 and AAC audio when audio is present.
