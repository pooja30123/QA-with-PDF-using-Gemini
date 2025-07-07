from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exception import customexception
from logger import logging


def download_gemini_embedding(model,document):
    """
    Download and initializes a Gemini Enbedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """

    try:
        logging.info("")
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")

        logging.info("")
        index = VectorStoreIndex.from_documents(document,llm=model,embed_model=gemini_embed_model)
        index.storage_context.persist()

        logging.info("")
        query_engine = index.as_query_engine(llm=model)
        return query_engine
    
    except Exception as e:
        raise customexception(e,sys)