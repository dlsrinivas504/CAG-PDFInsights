from pymongo import MongoClient
import gridfs
import PyPDF2
from io import BytesIO

class ReadPDFFromDatabase:
    def readPdfDoc(self):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["admin"]  # Replace 'mydatabase' with your database name
        fs = gridfs.GridFS(db)
        try:
            gridfs_data = fs.find_one({"filename": "example.pdf"})  # Search by filename
            if gridfs_data:
                pdf_binary = gridfs_data.read()
                with BytesIO(pdf_binary) as pdf_stream:
                    reader = PyPDF2.PdfReader(pdf_stream)
                    text_content = ""
                    for page in reader.pages:
                        text_content += page.extract_text()
    
                return text_content
            else:    
               print("No data")
           
        except Exception as e:
            print(f"Error retrieving PDF: {e}")

