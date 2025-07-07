from llama_index.core import SimpleDirectoryReader
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exception import customexception
from logger import logging

def load_data(data):
    """
    Load PDF document from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loadded documents. The specific type of documents may vary.
    """

    try:
        logging.info("data loding started....")
        loader = SimpleDirectoryReader("Data")
        documents = loader.load_data()
        logging.info("Data loading completed....")
        return documents

    except Exception as e:
        logging.info("exception in loading data...")
        raise customexception(e,sys)