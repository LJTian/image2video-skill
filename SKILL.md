---
name: image2video
description: Use when turning still images, product photos, character references, concept art, or storyboards into short videos, playable local video files, narration/audio plans, image-to-video prompts, shot plans, camera motion specs, or tool-ready generation briefs.
---

# Image to Video

## Overview

Use this skill to turn still images into a video plan or a playable local clip. Preserve the image facts first, then add motion, timing, narration, audio, and delivery constraints.

Default rules:

- Keep identity, geometry, text, and branding stable.
- Ask only for constraints that change the result.
- Prefer plausible motion over dramatic drift.
- Use `ffmpeg` when no AI video model is available.

## Workflow

1. Inspect the source image or ask for it if none is available.
2. Extract stable facts: subject, composition, clothes, materials, text, light, background, style, and any must-not-change details.
3. Ask only for missing constraints that matter: duration, aspect ratio, platform, motion intensity, mood, and exact text/logo/face handling.
4. Match motion to the image instead of forcing unsupported action.
5. Output a tool-ready brief: prompt, negative prompt, timing, camera, subject motion, and consistency notes.
6. If needed, build the clip locally or with the named tool, then verify the result.
7. For multiple options, vary only one major dimension per option.

## Clarifying Boundaries

Ask only when the answer changes the output:

- duration if the cut length is unclear
- aspect ratio if the platform matters or the source is ambiguous
- exact handling if text, logos, hands, or faces are present
- motion intensity if subtle vs cinematic vs stylized is unclear

## Image Analysis Checklist

Key checks:

- Subject: central person/object, pose, expression, shape, color, accessories
- Scene: location, depth, weather, props, signs, horizon/floor lines
- Style: photo, cinematic, anime, product render, illustration, UI, mixed media
- Lighting: direction, contrast, temperature, reflections, shadows, time
- Constraints: text, branding, face, hands, geometry, garment details
- Risk: readable text, logos, fingers, transparent objects, patterns, mirrors

Motion by asset:

- Portrait: breathing, blink, slight turn, hair movement, push-in
- Product: slow orbit, slider move, highlight sweep, parallax, rack focus
- Landscape: clouds, water, foliage, distant movement, dolly/crane
- Illustration: layered parallax, particles, smoke/cloth drift, camera drift
- UI: clean zoom/pan/cursor/state change; do not invent interactions

Keep motion subtle unless the user asks for stylized transformation.

## Local Video Assembly

If no AI video model is available, use `ffmpeg` and verify the final file.

- Order inputs by filename unless the user gives a sequence.
- For comics/storyboards/explainers, make a contact sheet first.
- Normalize early; use 720p (`1280x720`) when asked for 720P.
- For square lesson posts, prefer 1080×1080 and pad instead of crop when text matters.
- Use `zoompan` for slow push, pan, or drift. Do not imply real character animation.
- Match each image duration to the narration segment when audio exists.
- Prefer H.264 MP4 with `yuv420p`.
- Never leave an intermediate file as the final output.

Minimal example:

```bash
ffmpeg -loop 1 -i input.jpg -vf "scale=1280:720,zoompan=z='min(zoom+0.0015,1.08)':d=180:s=1280x720:fps=30,format=yuv420p" -t 6 -c:v libx264 output.mp4
```

If narration exists: make one audio segment per image, measure durations with `ffprobe`, render each shot to match, then mux and verify the final MP4.

## Narration and Audio

If the image has readable captions, labels, or bottom text, use them as the narration source. Rewrite only for speech clarity.

Voice selection guidance:

- Mainland Chinese female anchor: `zh-CN-XiaoxiaoNeural`
- Mainland Chinese male anchor/news/doc: `zh-CN-YunyangNeural` (`--rate=-4%`, `--pitch=-8Hz` if needed)
- Passionate mainland Chinese male: `zh-CN-YunjianNeural` if available
- Taiwanese Mandarin female: `zh-TW-HsiaoYuNeural` or `zh-TW-HsiaoChenNeural`
- If only macOS `say` is available, warn that it is less natural.
- Verify voice availability before promising it.

Audio handling rules:

- Do not add compression, EQ, or pitch tricks unless asked.
- Verify `edge-tts` voices before use; if network is blocked, ask for permission.
- Use AAC in MP4.
- Lengthen video instead of rushing long narration.
- Verify the final audio stream with `ffprobe` and a non-silent check.

## Educational Explainer Pattern

Use this pattern when the images are a numbered lesson, historical explanation, comic panel sequence, infographic, or social-media carousel.

Story arc:

- First 3 seconds: hook with curiosity, tension, or a sharp promise
- Middle: show the conflict, problem, misconception, or tradeoff
- End: explain the principle and resolve the tension
- Keep the hook tied to the source image and end with one clear takeaway when useful

Rules:

- Keep the source text visible; use padding and modest zoom
- Let narration follow the panel logic, not just describe the image
- Match tone to topic: news, documentary, teacher, or energetic host
- Give each panel enough time for natural delivery
- Use slow push, gentle parallax, or alternating pan; avoid fast moves/shake
- End with a short synthesis if needed

## Failure Modes

Call out likely drift risks in the negative prompt when they matter.

- Preserve text, subtitles, labels, and logos unless stylization is requested.
- Hands, fingers, jewelry, and small accessories drift easily.
- Be careful with transparent, reflective, mirrored, patterned, or grid-heavy assets.
- Preserve face or brand identity unless the user asks for a transformation.

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

For explainers and story-driven clips, prefer this beat structure:

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
- For tools with separate fields, split prompt, negative prompt, duration, aspect ratio, motion strength, and seed instead of burying everything in one paragraph.

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

- The output path exists and points to the final file, not an intermediate.
- Video stream: codec, resolution, FPS, duration.
- Audio stream when requested: codec, sample rate, channels, duration, and audible nonzero volume.
- Playback compatibility: prefer H.264 + AAC in MP4 for broad players.
