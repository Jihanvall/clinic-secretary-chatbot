from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Clinic Assistant is running!"}