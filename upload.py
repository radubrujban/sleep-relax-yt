import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# 1. Load saved token or run OAuth flow
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
else:
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    creds = flow.run_local_server(port=0)
    with open("token.json", "w") as f:
        f.write(creds.to_json())

# 2. Build YouTube client
yt = googleapiclient.discovery.build("youtube", "v3", credentials=creds)

# 3. Read metadata
with open("meta.txt") as f:
    lines = f.read().splitlines()
title = lines[0]
description = "\n".join(lines[1:-1])
tags = lines[-1].split(",")

# 4. Upload video
request = yt.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "27"
        },
        "status": {"privacyStatus": "public"}
    },
    media_body="output/sleep_relax.mp4"
)
response = request.execute()
print(response["id"])
