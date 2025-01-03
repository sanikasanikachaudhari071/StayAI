import chromadb
from chromadb import QueryResult
from backend.embeddings.jina_embedding import JinaEmbedding, JinaEmbeddingInput


def query_chroma(
    query_text: str, collection_name: str = "travel_data", n_results: int = 1
) -> str:
    """
    Query ChromaDB with text and return relevant results.

    Args:
        query_text: Text to search for in the database
        collection_name: Name of ChromaDB collection to query
        n_results: Number of results to return

    Returns:
        Query results from ChromaDB
    """
    client = chromadb.PersistentClient()
    collection = client.get_or_create_collection(collection_name)

    embedding_model = JinaEmbedding(
        JinaEmbeddingInput(
            model_name="jina-embeddings-v3",
            task="text-matching",
            late_chunking=False,
            dimensions=1024,
            embedding_type="float",
        )
    )

    embedding_outputs = embedding_model.generate_embedding(query_text)

    query: QueryResult = collection.query(
        query_texts=[query_text],
        query_embeddings=[embedding_outputs],
        n_results=n_results,
    )

    list_of_documents = query["documents"][0]
    final_document_answer = ""
    for idx, document in enumerate(list_of_documents):
        final_document_answer += f"""
        DOCUMENT {idx+1}: {document} 
        
        """
    return final_document_answer
