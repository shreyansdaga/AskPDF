from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

class Question(BaseModel):
    question: str

app = FastAPI()

@app.post("/ingest")
def ingest_file(file: UploadFile):
    return {"status": "recieved", "filename": file.filename}

@app.post("/ask_question")
def get_question(payload: Question):
    print(payload.question)
    return {"answer": f"Answer to the question will be provided"}
