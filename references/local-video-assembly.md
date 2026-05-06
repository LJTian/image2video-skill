# Local Video Assembly Reference

Use this reference only when the user asks for a playable local video file, audio muxing, or `ffmpeg` fallback output.

## Input Handling

- Order multiple source images by filename unless the user gives a sequence.
- For comics, storyboards, explainers, or carousels, inspect the sequence before writing narration.
- Normalize early. Use 720p (`1280x720`) when the user asks for 720P.
- For square lesson posts, prefer `1080x1080` and pad instead of crop when text matters.
- Never leave an intermediate file as the final output.

## Motion

- Use `zoompan` for slow push, pan, or drift.
- Do not imply real character animation when using static-image assembly.
- Prefer slow push, gentle parallax, or alternating pan for explainers.
- Avoid fast moves and camera shake unless explicitly requested.

Minimal silent clip:

```bash
ffmpeg -loop 1 -i input.jpg -vf "scale=1280:720,zoompan=z='min(zoom+0.0015,1.08)':d=180:s=1280x720:fps=30,format=yuv420p" -t 6 -c:v libx264 output.mp4
```

## Narration Timing

- Make one narration segment per image or beat when narration exists.
- Measure audio durations with `ffprobe`.
- Render each visual segment to match its narration segment.
- Lengthen video instead of rushing long narration.

## Verification

Use H.264 MP4 with AAC audio when audio exists.

Check the final file, not an intermediate:

```bash
ffprobe -v error -show_streams -show_format output.mp4
```

Verify:

- Output path exists and points to the final MP4.
- Video stream has expected codec, resolution, FPS, and duration.
- Audio stream exists when requested, uses AAC, and has expected duration.
- Audio is non-silent when narration or music was requested.
