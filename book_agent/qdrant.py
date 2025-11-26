import json
import os
# pip install sentence-transformers hf_xet
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct


with open(f"{os.path.dirname(__file__)}/best-seller-books.json", "r", encoding="utf-8") as f:
    books = json.load(f)


model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")

points = [PointStruct(id=idx+1, vector=model.encode(book["description"]).tolist(),
                      payload=book) for idx, book in enumerate(books)]


bestseller_vdb_client = QdrantClient(url="http://localhost:6333")

if bestseller_vdb_client.collection_exists(collection_name="best_sellers") is False:
    bestseller_vdb_client.create_collection(
        collection_name="best_sellers",
        vectors_config=VectorParams(size=model.get_sentence_embedding_dimension(), distance=Distance.COSINE),
    )

    bestseller_vdb_client.upsert(
        collection_name="best_sellers",
        points=points,
    )
