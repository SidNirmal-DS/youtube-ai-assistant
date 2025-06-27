from openai import OpenAI
import os

# Load your OpenAI API key from .env (already loaded in main.py)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content