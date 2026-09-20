#!/bin/bash
# Video encoding script — stitches captured frames into seamless-loop MP4s
# Run after frame capture completes

set -e

echo "=== Encoding Literal Slide 4K ==="
ffmpeg -y -framerate 30 -i frames/f%04d.png \
  -c:v libx264 -preset slow -crf 17 \
  -pix_fmt yuv420p -movflags +faststart \
  ../videos/literal_slide_4K.mp4

echo "=== Encoding Literal Slide 1080p ==="
ffmpeg -y -framerate 30 -i frames/f%04d.png \
  -c:v libx264 -preset slow -crf 17 \
  -pix_fmt yuv420p -movflags +faststart \
  ../videos/literal_slide_1080p.mp4

echo "=== Encoding Cinematic 1080p ==="
ffmpeg -y -framerate 30 -i gframes/f%04d.png \
  -c:v libx264 -preset slow -crf 17 \
  -pix_fmt yuv420p -movflags +faststart \
  ../videos/cinematic_1080p.mp4

echo "=== DONE — All videos encoded ==="
ls -lh ../videos/*.mp4
