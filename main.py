from ReadPDFFromDatabase import ReadPDFFromDatabase
from PerformLangChainIndex import PerformLangChainIndex
from dotenv import load_dotenv
import streamlit as st
import diskcache
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from PerformConversationalChain import PerformConversationalChain

import os



class main:
    load_dotenv()

    
  
    def __init__(self):
        self.readDoc = ReadPDFFromDatabase()
        self.langChain = PerformLangChainIndex()
        #Create or connect to a cache directory
        self.cache = diskcache.Cache('cache_directory')

    
    def processUserPrompt(self):
        st.set_page_config("PDF Summary")
        st.header("Get the PDF Summary using Gemini")
        
        user_question = st.text_input("Ask a Question from the PDF Files")
        if user_question:
            if user_question in self.cache:
                print("Reading response from the cache:::Cache Hit")
                response =  self.cache[user_question]
                st.write("Reply: ", response["output_text"])
            else:
                textData = self.readDoc.readPdfDoc()
                self.langChain.langChainIndexing(textData)
                embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
                new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
                docs = new_db.similarity_search(user_question)
                chain = PerformConversationalChain.get_conversational_chain()
                response = chain(
                                {"input_documents":docs, "question": user_question
                                }, 
                                return_only_outputs=True)
                self.cache[user_question] = response
                print("Response saved in the cache--", self.cache[user_question])
                st.write("Reply: ", response["output_text"])
      
                
# Create an instance of MainClass and perform addition
if __name__ == "__main__":
    main_class = main()
    main_class.processUserPrompt()
    