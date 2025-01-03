import chromadb
import uuid
from typing import List
from backend.embeddings.jina_embedding import JinaEmbedding, JinaEmbeddingInput
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def add_pdf_to_chroma(pdf_path: str, collection_name: str = "travel_data") -> None:
    """
    Add PDF content to ChromaDB after splitting into chunks and generating embeddings.

    Args:
        pdf_path: Path to the PDF file
        collection_name: Name of the ChromaDB collection to store data in
    """
    client = chromadb.PersistentClient()
    collection = client.get_or_create_collection(collection_name)

    loader = PyPDFLoader(pdf_path)
    pages: List[Document] = loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False,
    )

    chunks: List[Document] = text_splitter.split_documents(pages)

    # Create embeddings and insert into chroma db
    for idx, doc in enumerate(chunks):
        embedding_model = JinaEmbedding(
            JinaEmbeddingInput(
                model_name="jina-embeddings-v3",
                task="text-matching",
                late_chunking=False,
                dimensions=1024,
                embedding_type="float",
            )
        )
        embedding_outputs: List[float] = embedding_model.generate_embedding(
            doc.page_content
        )
        print(f"Embedding created for {doc.metadata['source'], doc.metadata['page']}")

        collection.add(
            ids=[str(uuid.uuid4())],
            documents=[doc.page_content],
            metadatas=[doc.metadata],
            embeddings=[embedding_outputs],
        )

    print(f"Total documents added: {collection.count()}")
