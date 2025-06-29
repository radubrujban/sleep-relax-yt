#!/usr/bin/env bash
# Generate a thumbnail by overlaying text on the background
convert assets/background.jpg \
  -gravity Center \
  -pointsize 64 \
  -fill white \
  -annotate +0+200 "8 Hours Rain Sounds for Sleep" \
  thumbnail.jpg
