# RBC Performance Gala 2026 — Animated Slide Assets

Animated / cinematic interpretations of the **RBC Performance Gala 2026** transition slide,
built from the source PowerPoint. The event celebrates RBC's highest-recognition employees,
so every variation stays true to the deck's colour palette and design language:

- **Background:** deep royal midnight navy (`#03091e` → `#0a1e5c`)
- **Accent lines:** electric cyan (`#00e5ff`, `#4fc3f7`) + warm gold (`#d4af37`, `#ffe060`)
- **Bokeh:** amber/orange (left) · cobalt blue (right)
- **Star:** white-to-gold gradient, encircled by a glowing gold ring
- **Anchor:** RBC heraldic shield crest ("Leo the Lion") dead centre
- **Type:** "RBC Performance Gala 2026" in white with a cyan glow

---

## Contents — all variations produced

### `html/` — interactive HTML animations (open in any modern browser, full-screen / borderless)

| File | Variation | Notes |
|------|-----------|-------|
| `v1_dark_dashed.html` | **V1 — original** | Darker navy background; swirl arms use flowing **dashed** lines streaming inward. First iteration. |
| `v2_bright_solid.html` | **V2 — projector-optimised** | Brighter palette, **solid continuous thick** swirl lines, stronger glows. Supersedes V1 for projector use. |
| `video_source_literal.html` | **Video source — literal** | Self-contained (embedded assets) render source for the literal-slide MP4s. |
| `video_source_cinematic.html` | **Video source — cinematic** | Self-contained render source for the cinematic interstitial MP4 (darkness → ignition → bloom → reveal build sequence). |

### `videos/` — rendered MP4s (seamless loops)

| File | Variation | Res | Length |
|------|-----------|-----|--------|
| `literal_slide_4K.mp4` | Literal animation of the slide layout | 3840×2160 | 12s |
| `literal_slide_1080p.mp4` | Literal animation of the slide layout | 1920×1080 | 12s |
| `cinematic_1080p.mp4` | Free-form regal cinematic interstitial | 1920×1080 | 12s |

### `renders/` — static full-bleed stills (borderless)

| File | Variation | Res |
|------|-----------|-----|
| `v2_bright_solid_4k.png` | V2 still | 3840×2160 |
| `v2_bright_solid_1080p.png` | V2 still | 1920×1080 |

### `source/`

| File | Description |
|------|-------------|
| `RBC_Awardsa_Animated.pptx` | Original source PowerPoint slide. |

---

## Iteration history

1. **V1 (dark / dashed)** — first animated HTML interpretation of the slide.
2. **V2 (bright / solid)** — brightened for projector display; swirl lines converted from dashed to
   solid continuous thick lines per feedback ("too dark… lines shouldn't be dotted… brighter colours").
3. **Literal-slide video** — V-style animation rendered to seamless-loop MP4 (4K + 1080p), RBC lion dead-centre.
4. **Cinematic interstitial** — free-form regal interpretation (luxury awards-show opener) as a seamless
   1080p loop, for use as a transition between event segments.

All videos are seamless loops (end frame matches start frame) suitable for continuous projection.
