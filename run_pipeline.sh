#!/usr/bin/env bash
set -e

# 1. Activate virtual environment (GitHub Actions runner already has Python)
#    Locally you'd do: source env/bin/activate

# 2. Install or update dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 3. Generate the video
python make_video.py

# 4. Generate metadata
python generate_meta.py

# 5. Create thumbnail
./make_thumbnail.sh

# 6. Upload to YouTube and capture the video ID
VIDEO_ID=$(python upload.py)
echo "LAST_VIDEO_ID=\$VIDEO_ID" > last_video.env
export LAST_VIDEO_ID=\$VIDEO_ID

# 7. Post to Twitter
python post_twitter.py
