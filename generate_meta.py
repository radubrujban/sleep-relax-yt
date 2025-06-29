# generate_meta.py
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables (OPENAI_API_KEY, etc.)
load_dotenv()

# Instantiate new-style client
client = OpenAI()

# Your prompt for metadata
template = (
    "Generate a title and description for a soothing sleep/relaxation video. "
    "Include relevant keywords and a call to action to subscribe."
)

# Call the v1 API
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an expert at writing YouTube metadata."},
        {"role": "user", "content": template},
    ],
    temperature=0.7,
)

# Print out the generated title & description
print(response.choices[0].message.content)

