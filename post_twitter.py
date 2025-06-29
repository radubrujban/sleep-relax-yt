import os
import tweepy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Twitter client
client = tweepy.Client(
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
)

# Build and send the tweet
video_id = os.getenv("LAST_VIDEO_ID")
url = f"https://youtu.be/{video_id}"
tweet = f"🛌 Relax with 8 hours of rain sounds: {url} #SleepSounds #Relaxation"

response = client.create_tweet(text=tweet)
print("Tweet ID:", response.data["id"])
