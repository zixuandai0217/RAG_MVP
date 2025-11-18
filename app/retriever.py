import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Load FAISS index & chunks
index = faiss.read_index("embeddings/index.faiss")
chunks = np.load("embeddings/chunks.npy", allow_pickle=True).tolist()

def retrieve(query, top_k=3):
    q_vec = model.encode([query])
    distances, ids = index.search(np.array(q_vec), top_k)
    return [chunks[i] for i in ids[0]]
