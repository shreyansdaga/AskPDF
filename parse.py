import pymupdf4llm
import pymupdf
from dataclasses import dataclass
import re
import os

MAX_CHUNK_SIZE = 2000
file_name = os.path.join("uploads", "test_paper.pdf")
# Turning pdf into MD
doc = pymupdf.open(file_name)
pages = pymupdf4llm.to_markdown(doc, page_chunks=True)

@dataclass
class Chunk:
    chunk_id: str
    text: str
    source_file: str
    page_number: int

def create_chunks(text):
    return_chunks = []
    final_return_chunks = []
    header_chunks = [c for c in re.split(r'\n#{1,2}\s', text) if c.strip()]
    for chunk in header_chunks: # Split the really long header chunks into paragraph chunks
        if len(chunk) > MAX_CHUNK_SIZE:
            para_chunks = [p for p in chunk.split('\n\n') if p.strip()]
            for i in para_chunks:
                return_chunks.append(i)
        else:
            return_chunks.append(chunk)

    for chunk in return_chunks: # Split the really long paragraphs into chunks with the maximum chunk length
        if len(chunk) > MAX_CHUNK_SIZE:
            fin_chunks = [chunk[i:i+MAX_CHUNK_SIZE] for i in range(0, len(chunk), MAX_CHUNK_SIZE)]
            for i in fin_chunks:
                final_return_chunks.append(i)
        else:
            final_return_chunks.append(chunk)

    return final_return_chunks

def return_chunks():
    chunks = []
    chunk_counter = 1

    for page_number, page in enumerate(pages, start=1):
        page_text = page["text"]
        chunk_text = create_chunks(page_text)
        for each_chunk_text in chunk_text:
            id = file_name + "_chunk_" + str(chunk_counter)
            chunk = Chunk(
                chunk_id=id,
                text=each_chunk_text,
                source_file=file_name,
                page_number=page_number
            )
            chunks.append(chunk)

            chunk_counter += 1

    return chunks
