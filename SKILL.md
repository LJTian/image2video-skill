---
name: image2video
description: Use when turning still images, product photos, character references, concept art, or storyboards into short videos, image-to-video prompts, shot plans, camera motion specs, or tool-ready generation briefs.
---

# Image to Video

## Overview

Use this skill to convert one or more still images into a practical video generation plan. Preserve the visual facts of the source image first, then add motion, camera behavior, timing, and delivery constraints.

## Workflow

1. Inspect the source image or ask for it if none is available.
2. Extract stable facts: subject identity, composition, clothing, materials, text, lighting, background, style, and any details that must not change.
3. Clarify missing production constraints only when they materially affect output: duration, aspect ratio, target platform, motion intensity, mood, and whether text/logos/faces must remain exact.
4. Choose a motion pattern that fits the image instead of forcing action the still cannot support.
5. Produce a tool-ready brief with prompt, negative prompt, shot timing, camera movement, subject motion, and consistency constraints.
6. If the user wants multiple options, vary only one major dimension per option, such as camera move, emotion, environment motion, or pacing.

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
