#!/usr/bin/env bash
set -e

DURATION=$((8*3600))
VID_IN=$(ls video | head -n1)
AUD_IN=$(ls audio | head -n1)

ffmpeg -y \
  -stream_loop -1 -i "video/$VID_IN" \
  -stream_loop -1 -i "audio/$AUD_IN" \
  -t "$DURATION" \
  -c:v libx264 -preset veryfast -crf 23 \
  -c:a aac -b:a 192k \
  output/sleep_relax.mp4
