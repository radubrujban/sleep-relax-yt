import os
import openai
from dotenv import load_dotenv

# Load your OpenAI API key from the .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Prompt for metadata
prompt = (
    "Generate a YouTube title, description with timestamps, "
    "and 10 tags for an 8-hour rain sleep sounds video."
)

# Call the API
resp = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{'role':'user','content':prompt}]
)

# Write the output
with open('meta.txt', 'w') as f:
    f.write(resp.choices[0].message.content)
