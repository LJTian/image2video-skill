# Story, Audio, and Risk Reference

Use this reference when the request includes narration, subtitles, explainers, panel sequences, numbered overlays, or high-fidelity text/logo/face requirements.

## Story-Driven Clips

Use this pattern for numbered lessons, historical explanations, comic panels, infographics, social-media carousels, or other educational explainers.

Story arc:

- First 3 seconds: hook with curiosity, tension, or a sharp promise.
- Middle: show the conflict, problem, misconception, or tradeoff.
- End: explain the principle and resolve the tension.
- Keep the hook tied to the source image.
- End with one clear takeaway when useful.

Rules:

- Keep source text visible when it matters.
- Use padding and modest zoom for text-heavy images.
- Let narration follow the panel logic instead of merely describing the image.
- Match tone to the topic: news, documentary, teacher, or energetic host.
- Give each panel enough time for natural delivery.
- Remove numbered panels, step labels, or numbered overlays in the video by default unless the user explicitly asks to preserve them.

## Voice Selection

Only offer two voice-type choices unless the user names a specific voice:

- Female anchor
- Male anchor

Use a voice available in the chosen tool. If only macOS `say` is available, warn that it is less natural. Verify voice availability before promising a specific voice.

## Failure Modes

Call out likely drift risks in the negative prompt when they matter:

- Preserve text, subtitles, labels, and logos unless stylization is requested.
- Hands, fingers, jewelry, and small accessories drift easily.
- Transparent, reflective, mirrored, patterned, and grid-heavy assets need extra preservation constraints.
- Faces, brand identity, product shape, and logo placement need explicit anchors.
- Readable text can become warped or inconsistent across frames.
