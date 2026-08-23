import json
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from chatbot_config import create_chat
from fastapi.responses import StreamingResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

chat = create_chat()

with open("data/clinic_schedule.json", "r") as f:
    CLINIC_DATA = json.load(f)


class ChatMessage(BaseModel):
    message: str


@app.get("/")
def read_root():
    return FileResponse("static/homepage.html")


@app.get("/chat-widget")
def chat_widget():
    return FileResponse("static/index.html")


@app.get("/clinic-info")
def clinic_info():
    return {
        "clinic_info": CLINIC_DATA["clinic_info"],
        "doctors": CLINIC_DATA["doctors"],
    }


@app.post("/chat")
def chat_endpoint(chat_message: ChatMessage):
    def generate():
        response = chat.send_message_stream(chat_message.message)
        for chunk in response:
            if chunk.text:
                yield chunk.text

    return StreamingResponse(generate(), media_type="text/plain")