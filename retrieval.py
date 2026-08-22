K = 5 # Number of top hits produced by model

def retrieve(index, encoded_question, chunks):
    distances, indices = index.search(encoded_question, K)
    chunk_list = [chunks[i] for i in indices[0]]
    return chunk_list
