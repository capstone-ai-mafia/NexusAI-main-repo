import shutil

from .loader import load_documents
from .cleaner import clean_text
from .chunker import split_documents
from .metadata import add_metadata

from .embeddings import get_embeddings
from .vector_client import get_vectorstore
from .config import CHROMA_PATH




def ingest():


    # Clear existing vector store for clean re-ingest
    if CHROMA_PATH.exists():
        print(f"Removing existing chroma_db at {CHROMA_PATH}...")
        shutil.rmtree(CHROMA_PATH)


    print("Loading documents...")


    documents = load_documents()



    print(
        f"Loaded {len(documents)} documents"
    )



    for doc in documents:

        doc.page_content = clean_text(
            doc.page_content
        )



    chunks = split_documents(
        documents
    )



    chunks = add_metadata(
        chunks
    )



    print(
        f"Created {len(chunks)} chunks"
    )

    # Report section extraction stats
    with_section = sum(1 for c in chunks if c.metadata.get("section"))
    print(f"Chunks with section metadata: {with_section}/{len(chunks)}")


    embeddings = get_embeddings()



    vectorstore = get_vectorstore(
        embeddings
    )



    vectorstore.add_documents(
        chunks
    )



    print(
        "Ingestion completed"
    )




if __name__ == "__main__":

    ingest()