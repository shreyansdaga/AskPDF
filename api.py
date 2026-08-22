from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from parse import return_chunks
from encoding import encode, save_index

class Question(BaseModel):
    question: str

app = FastAPI()

@app.post("/ingest")
def ingest_file(pdf: UploadFile):
    chunks = return_chunks(pdf)
    index = encode(chunks)
    save_index(index, chunks)
    return {"status": "recieved", "filename": pdf.filename}

@app.post("/ask_question")
def get_question(payload: Question):
    print(payload.question)
    return {"answer": f"Answer to the question will be provided"}
