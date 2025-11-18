import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def split_text(text, chunk_size=300, overlap=50):
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i+chunk_size])
    return chunks

def build_index():
    os.makedirs("embeddings", exist_ok=True)

    with open("data/example.txt", "r", encoding="utf-8") as f:
        text = f.read()

    chunks = split_text(text)

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    vectors = model.encode(chunks)

    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors))

    faiss.write_index(index, "embeddings/index.faiss")
    np.save("embeddings/chunks.npy", np.array(chunks))

    print("Index built. Total chunks:", len(chunks))


if __name__ == "__main__":
    build_index()
