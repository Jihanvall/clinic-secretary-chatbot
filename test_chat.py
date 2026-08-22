import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

chat = client.chats.create(model="gemini-3.6-flash")

response1 = chat.send_message("My name is Sara.")
print("Bot:", response1.text)

response2 = chat.send_message("What is my name?")
print("Bot:", response2.text)