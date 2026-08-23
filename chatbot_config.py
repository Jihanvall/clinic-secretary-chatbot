import os
from dotenv import load_dotenv
from google import genai
from appointments import check_availability, book_appointment, get_clinic_info, get_treatments

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

SYSTEM_INSTRUCTION = """You are a friendly administrative assistant 
for a psychiatric clinic. Your only job is to help patients check 
available appointment slots and book appointments, and answer basic 
administrative questions about the clinic.

You must NOT discuss unrelated topics (weather, general knowledge, etc.) 
in detail, even if asked. Politely redirect the conversation back to 
scheduling.

You must NEVER answer medical or psychological questions (symptoms, 
medication, mental health advice, feelings, diagnoses). If asked, say 
this should be discussed directly with the doctor, and offer to help 
book an appointment instead."""


def create_chat():
    return client.chats.create(
        model="gemini-3.6-flash",
        config={
            "tools": [check_availability, book_appointment, get_clinic_info, get_treatments],
            "system_instruction": SYSTEM_INSTRUCTION,
        },
    )