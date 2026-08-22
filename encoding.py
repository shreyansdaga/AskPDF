from sentence_transformers import SentenceTransformer
import faiss
import pickle

# import numpy as np || need only for testing purposes

model = SentenceTransformer("all-MiniLM-L6-v2")
def encode(chunks):
    texts = [chunk.text for chunk in chunks]
    embeddings = model.encode(texts)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def encode_string(string):
    embedding = model.encode([string])
    return embedding

"""
Testing code to make sure no chuunks were dropped and everything was encoded properly
print(len(chunks))          # e.g. 114
print(embeddings.shape)     # should be (114, 384)
print(chunks[0].text[:80])
print(embeddings[0][:5])   # just look at the first 5 numbers, not to interpret them, just to confirm it's not all zeros / NaN
print(np.isnan(embeddings).any())  # should be False — a NaN anywhere means something went wrong during encoding
"""

INDEX_PATH = "index.faiss"
CHUNKS_PATH = "chunks.pkl"

def save_index(index, chunks):
    faiss.write_index(index, INDEX_PATH)
    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(chunks, f)

def load_index():
    index = faiss.read_index(INDEX_PATH)
    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)
    return index, chunks
