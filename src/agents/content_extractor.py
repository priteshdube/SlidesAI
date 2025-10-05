import os
import pandas as pd
import fitz # PyMuPDF
from docx import Document
from pptx import Presentation
from llama_index.core import SimpleDirectoryReader

class ContentExtractor:
    def __init__(self, directory="data/"):
        self.directory = directory

    def extract_text_from_txt(self, file_path):
        with open(file_path, "r", encoding="utf-8" ) as file:
            return file.read()
        
    def extract_text_from_pdf(self, file_path):
        text = ""
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text("text") + "\n"
        return text
    
    def extract_text_from_docx(self, file_path):
        doc= Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    
    def extract_text_from_csv(self, file_path):
        df = pd.read_csv(file_path)
        return df.to_string()
    
    def extract_from_file(self, file_path):
        _, ext = os.path.splitext(file_path)

        if ext.lower() == ".txt":
            return self.extract_text_from_txt(file_path=file_path)
        elif ext.lower() == ".pdf":
            return self.extract_text_from_pdf(file_path=file_path)
        elif ext.lower() == ".docx":
            return self.extract_text_from_docx(file_path=file_path)
        elif ext.lower()== ".csv":
            return self.extract_text_from_csv(file_path=file_path)
        else:
            raise ValueError(f"Unsupported file format: {ext}")
        
    def extract_from_directory(self):
        extracted_data= {}
        if not os.path.exists(self.directory):
            raise FileNotFoundError(f"Directory {self.directory} does not exist.")
        
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)

            if os.path.isfile(file_path):
                try:
                    extracted_data[file_path] = self.extract_from_file(file_path=file_path)
                except Exception as e:
                    print(f"Error extracting {file_path}: {e}")

        return extracted_data
    

if __name__ == "__main__":
    extractor= ContentExtractor(directory= "data/")
    extracted_data= extractor.extract_from_directory()
    for file,content in extracted_data.items():
        print(f"File: {file}\nContent Preview: {content[:500]}\n{'-'*40}\n")
       


