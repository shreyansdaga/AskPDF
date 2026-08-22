from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from parse import return_chunks
from encoding import encode, save_index, load_index, encode_string
from retrieval import retrieve

class Question(BaseModel):
    question: str

app = FastAPI()

@app.post("/ingest")
def ingest_file(file: UploadFile):
    chunks = return_chunks(file)
    index = encode(chunks)
    save_index(index, chunks)
    return {"status": "recieved", "filename": file.filename}

@app.post("/ask_question")
def get_question(payload: Question):
    index, chunks = load_index()
    encoded_question = encode_string(payload.question)
    relevant_chunks = retrieve(index, encoded_question, chunks)
    text = ""
    for chunk in relevant_chunks:
        text += chunk.text
    return {"answer": f"{text}"}
