#!/usr/bin/env bash
set -e

# Duration: 8 hours in seconds
DURATION=$((8*3600))

# Prepare folders if missing
mkdir -p video audio output

# If no video files exist, generate a 10-second black video placeholder
if [ -z "$(ls video 2>/dev/null)" ]; then
  ffmpeg -y -f lavfi -i color=size=1280x720:duration=10:rate=30 \
    -c:v libx264 video/sample.mp4
fi

# If no audio files exist, generate 10-second silent audio placeholder
if [ -z "$(ls audio 2>/dev/null)" ]; then
  ffmpeg -y -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 \
    -t 10 -c:a libmp3lame audio/sample.mp3
fi

# Now loop & combine to the full DURATION
IN_VID=$(ls video | head -n1)
IN_AUD=$(ls audio | head -n1)

ffmpeg -y \
  -stream_loop -1 -i "video/$IN_VID" \
  -stream_loop -1 -i "audio/$IN_AUD" \
  -t "$DURATION" \
  -c:v libx264 -preset veryfast -crf 23 \
  -c:a aac -b:a 192k \
  output/sleep_relax.mp4
