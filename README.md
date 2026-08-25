# Anna — AI Clinic Secretary Chatbot 

An AI-powered administrative assistant for a psychiatric clinic, built with **Google Gemini**, **FastAPI**, and **SQLite**.

Anna helps patients check appointment availability, book appointments, and answer general clinic questions — while safely redirecting any medical or psychological questions directly to the doctor.

## Features

-  Natural conversation with memory (multi-turn chat)
-  Real appointment booking via **function calling** (not just text replies)
-  Persistent storage with SQLite
-  Web interface with a floating chat widget
-  Streaming responses for a natural typing experience
-  Strict boundaries: never answers medical/psychological questions, always redirects to the doctor

## Tech Stack

- **LLM**: Google Gemini (gemini-3.6-flash)
- **Backend**: FastAPI
- **Database**: SQLite
- **Frontend**: HTML/CSS/JavaScript

## Project Structure

AI_Bot/
├── main.py                   # FastAPI server & routes
├── chatbot.py                 # Terminal version of the chatbot
├── chatbot_config.py          # Gemini client & system instructions
├── appointments.py            # Booking logic & clinic data access
├── database.py                # SQLite database layer
├── data/
│   └── clinic_schedule.json   # Clinic schedule, doctors, treatments
├── static/
│   ├── homepage.html          # Clinic landing page
│   └── index.html             # Chat widget
├── test_appointments.py       # Tests for booking logic
├── test_chat.py                # Tests for chat memory
├── test_gemini.py              # Tests for Gemini connection
└── requirements.txt

## Getting Started

### 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/clinic-secretary-chatbot.git
cd clinic-secretary-chatbot

### 2. Install dependencies
pip install -r requirements.txt

### 3. Set up your API key
Create a .env file in the root directory:
GEMINI_API_KEY=your_api_key_here

Get a free key at Google AI Studio: https://aistudio.google.com/apikey

### 4. Run the app
uvicorn main:app --reload

Visit http://127.0.0.1:8000 in your browser.

## Why This Project?

This project demonstrates a practical application of agentic AI — an assistant that doesn't just talk, but performs real actions (checking availability, booking appointments) through function calling, while maintaining clear ethical boundaries around sensitive topics.

## License

MIT