import openai
import json
import os

def answer_email(message):
    """
    Generate an answer to the email using the OpenAI API.
    Loads the OpenAI API key from config/settings.json,
    constructs a prompt based on the email's snippet, and calls the ChatCompletion API.
    """
    # Load the OpenAI API key from settings.json
    settings_file = os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.json')
    try:
        with open(settings_file, 'r') as f:
            settings = json.load(f)
    except Exception as e:
        print("Error loading settings:", e)
        return "Unable to load settings."

    openai_api_key = settings.get("openai_api_key")
    if not openai_api_key:
        print("OpenAI API key not found in settings.json")
        return "OpenAI API key missing."

    # Set the API key for openai
    openai.api_key = openai_api_key

    # Use the email's snippet to construct a prompt for generating a response.
    snippet = message.get('snippet', '')
    prompt = (
        f"Email content: {snippet}\n\n"
        "Generate a professional, helpful response for this email:"
    )

    try:
        # Use the ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert personal inbox manager."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        print("Error calling OpenAI API:", e)
        return "Error generating response."
