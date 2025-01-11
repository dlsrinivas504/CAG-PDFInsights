from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
import google.generativeai as genai
import os


class PerformLangChainIndex:
    #def __init__(self, raw_text):
        #self.raw_text = raw_text  # Property initialized in the constructor

    def langChainIndexing(self,raw_text):
        text_chunks = self.get_text_chunks(raw_text)
        self.get_vector_store(text_chunks)

    

    def get_text_chunks(self,raw_text):
        print("inside get_text_chunks")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        chunks=text_splitter.split_text(raw_text)
        return chunks
    
    def get_vector_store(self,text_chunks):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        print("inside get_vector_store")
        embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
        print("Successfully FAISS done")