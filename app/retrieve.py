import chromadb
from sentence_transformers import SentenceTransformer


client = chromadb.PersistentClient(path="chroma_store")

collection = client.get_or_create_collection(
    name="documents"
)

model = SentenceTransformer("all-MiniLM-L6-v2")


def add_document_to_vector_store(doc_id, title, content, access_level):
    embedding = model.encode(content).tolist()

    collection.add(
        ids=[str(doc_id)],
        documents=[content],
        embeddings=[embedding],
        metadatas=[{
            "title": title,
            "access_level": access_level
        }]
    )

def search_documents(query, access_level):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
        where={
            "access_level": access_level
        }
    )

    return results