import os

from dotenv import load_dotenv
from google import genai


# Load variables from the .env file
load_dotenv()

# Get the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key exists
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")


# Create the Gemini client
client = genai.Client(api_key=api_key)


# Get a question from the user
prompt = input("Ask AI: ")


try:
    # Send the prompt to the Gemini API
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Print the generated answer
    print("\nAI Response:\n")
    print(response.text)

except Exception as e:
    print(f"\nError: {e}")