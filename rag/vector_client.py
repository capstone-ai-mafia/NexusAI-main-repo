from langchain_chroma import Chroma

from .config import CHROMA_PATH



def get_vectorstore(embeddings):

    vectorstore = Chroma(

        persist_directory=str(CHROMA_PATH),

        embedding_function=embeddings

    )


    return vectorstore