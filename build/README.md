# Build Pipeline — Video Generation

This directory contains the complete source code and scripts used to generate the MP4 video files from the HTML animations.

## Pipeline Overview

1. **HTML Source** → 2. **Frame Capture** (Playwright) → 3. **Video Encoding** (FFmpeg)

---

## 1. HTML Sources (before asset embedding)

| File | Description |
|------|-------------|
| `literal_source.html` | Base HTML for literal-slide animation (before assets embedded) |
| `cinematic_source.html` | Base HTML for cinematic animation (before assets embedded) |

These are the "clean" source files. The `*_full.html` files in `../html/video_source_*.html` have the PPTX assets base64-embedded so they render standalone in headless Chrome.

---

## 2. Frame Capture Scripts (Playwright)

Each script opens the embedded HTML in headless Chrome and renders 360 frames (12s @ 30fps) by calling `window.renderAt(t)` for deterministic animation timing.

| Script | Target | Resolution | Output |
|--------|--------|------------|--------|
| `capture_literal_4k.py` | `video_source_literal.html` | 3840×2160 | `frames/f0000.png` … `f0359.png` |
| `capture_literal_1080p.py` | `video_source_literal.html` | 1920×1080 | `frames/f0000.png` … `f0359.png` |
| `capture_cinematic.py` | `video_source_cinematic.html` | 1920×1080 | `gframes/f0000.png` … `f0359.png` |

Also includes single-frame test scripts:
- `shot_literal.py` — render one frame at a given timestamp (for testing/verification)
- `shot_cinematic.py` — render one frame at a given timestamp

---

## 3. Video Encoding (FFmpeg)

After frame capture, frames are stitched into seamless-loop MP4s:

```bash
# Literal slide 4K
ffmpeg -framerate 30 -i frames/f%04d.png -c:v libx264 -preset slow \
  -crf 17 -pix_fmt yuv420p -movflags +faststart \
  ../videos/literal_slide_4K.mp4

# Literal slide 1080p
ffmpeg -framerate 30 -i frames/f%04d.png -c:v libx264 -preset slow \
  -crf 17 -pix_fmt yuv420p -movflags +faststart \
  ../videos/literal_slide_1080p.mp4

# Cinematic 1080p
ffmpeg -framerate 30 -i gframes/f%04d.png -c:v libx264 -preset slow \
  -crf 17 -pix_fmt yuv420p -movflags +faststart \
  ../videos/cinematic_1080p.mp4
```

**Settings:**
- `-crf 17` — high quality (visually lossless)
- `-preset slow` — better compression
- `-pix_fmt yuv420p` — maximum compatibility
- `-movflags +faststart` — web-optimized (moov atom at start)

---

## Reproducibility

To regenerate any video from scratch:

1. Ensure dependencies: `playwright`, `ffmpeg`, Chrome/Chromium
2. Run the appropriate capture script: `python3 capture_*.py`
3. Encode with FFmpeg using the command above
4. Verify seamless loop: frame 0 should visually match frame 359

All animations are deterministic — same HTML + same timestamp = identical frame.
