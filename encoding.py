from parse import return_chunks
from sentence_transformers import SentenceTransformer
import faiss

# import numpy as np || need only for testing purposes

chunks = return_chunks()

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [chunk.text for chunk in chunks]
embeddings = model.encode(texts)

"""
Testing code to make sure no chuunks were dropped and everything was encoded properly
print(len(chunks))          # e.g. 114
print(embeddings.shape)     # should be (114, 384)
print(chunks[0].text[:80])
print(embeddings[0][:5])   # just look at the first 5 numbers, not to interpret them, just to confirm it's not all zeros / NaN
print(np.isnan(embeddings).any())  # should be False — a NaN anywhere means something went wrong during encoding
"""

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print(index.ntotal, len(chunks))