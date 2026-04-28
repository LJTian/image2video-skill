---
name: image2video
description: Use when turning still images, product photos, character references, concept art, or storyboards into short videos, playable local video files, narration/audio plans, image-to-video prompts, shot plans, camera motion specs, or tool-ready generation briefs.
---

# Image to Video

## Overview

Use this skill to convert one or more still images into a practical video generation plan or a playable local video file. Preserve the visual facts of the source image first, then add motion, camera behavior, timing, narration, audio, and delivery constraints.

## Workflow

1. Inspect the source image or ask for it if none is available.
2. Extract stable facts: subject identity, composition, clothing, materials, text, lighting, background, style, and any details that must not change.
3. Clarify missing production constraints only when they materially affect output: duration, aspect ratio, target platform, motion intensity, mood, and whether text/logos/faces must remain exact.
4. Choose a motion pattern that fits the image instead of forcing action the still cannot support.
5. Produce a tool-ready brief with prompt, negative prompt, shot timing, camera movement, subject motion, and consistency constraints.
6. If the user wants an actual video file, build it with available local tools or the named generation tool, then verify the resulting streams.
7. If the user wants multiple options, vary only one major dimension per option, such as camera move, emotion, environment motion, pacing, or voice style.

## Image Analysis Checklist

- Subject: who or what is central, including pose, expression, shape, color, and visible accessories.
- Scene: location, background depth, weather, props, signage, and horizon or floor lines.
- Style: photo, cinematic, anime, product render, illustration, archival, UI mockup, or mixed media.
- Lighting: source direction, contrast, color temperature, reflections, shadows, and time of day.
- Constraints: exact text, brand marks, face identity, hands, product geometry, garment details, and anything likely to drift.
- Video risk: areas where generation may fail, such as readable text, small logos, fingers, transparent objects, complex patterns, or mirrored reflections.

## Motion Selection

Prefer subtle, physically plausible motion unless the user asks for a stylized transformation.

- Portrait or character: breathing, blink, hair movement, slight head turn, expression shift, handheld push-in.
- Product: slow orbit, slider move, controlled highlight sweep, background parallax, shallow depth-of-field rack focus.
- Landscape or architecture: clouds, water, foliage, people or vehicles in the distance, crane or dolly movement.
- Illustration or concept art: layered parallax, atmospheric particles, cloth or smoke movement, cinematic camera drift.
- UI or graphic: avoid inventing interactions unless requested; use clean zoom, pan, cursor trace, or state transition.

Avoid motion that contradicts the still image, changes the object design, invents unreadable text, or requires unseen anatomy.

## Local Video Assembly

When the user asks to generate a video from local images and no AI video model is configured, use `ffmpeg` to create a playable file rather than stopping at prompts.

- Order inputs by filename unless the user specifies a sequence.
- Normalize resolution and aspect ratio early; use 720p (`1280x720`) when the user asks for 720P.
- Make stills feel alive with `zoompan`: slow push-in/out, gentle pan, or slight drift. Avoid implying real character animation unless an AI video model is used.
- Set each image duration from the content. If narration is present, match each image's display duration to the corresponding narration segment.
- Prefer H.264 video in MP4 for compatibility. Use `yuv420p` pixel format.
- Do not leave a partially generated file as the final output. If a command is slow or wrong, stop it and regenerate with corrected timing.

For image-by-image narration timing, generate or collect one audio segment per image, measure each duration with `ffprobe`, then set each shot's frame count or duration from those measurements.

## Narration and Audio

When images contain readable captions, labels, or bottom explanatory text, extract that text as the narration source instead of inventing a summary. Rewrite only enough for speech clarity while preserving the original meaning.

Voice selection guidance:

- If the user requests a mainland Chinese female anchor/newscaster voice, prefer `zh-CN-XiaoxiaoNeural` when Microsoft Edge/Azure TTS is available. It is a warm Mandarin female voice and commonly supports news-style use.
- If the user requests a Taiwanese Mandarin female voice, prefer `zh-TW-HsiaoYuNeural` or `zh-TW-HsiaoChenNeural` when available.
- If only macOS `say` is available, warn that voices such as `Tingting` or `Meijia` are less natural than neural TTS.
- If current TTS voice availability might have changed, verify with the tool or official provider docs before promising a specific voice.

Audio handling rules:

- If the user asks for the voice to sound natural, do not apply dynamic compression, heavy normalization, EQ, or pitch tricks unless they ask for processing.
- For MP4 delivery, encode or remux audio as AAC for compatibility. Do not rely on MP3-in-MP4 as the final deliverable; some players show the stream but play silence.
- Preserve a natural pace by lengthening the video when narration is long instead of truncating the audio or forcing an unnatural speed.
- Verify the final audio stream with `ffprobe`, and use a short `volumedetect` or decode-to-null check to confirm it is not silent.

## Output Format

For a single generation, provide:

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

For multiple shots, use a compact shot list:

```markdown
Shot 1:
- Time:
- Framing:
- Camera:
- Motion:
- Prompt:
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
