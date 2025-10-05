import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, Document
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding 

# Load environment variables from .env file
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class Summarizer:
    def __init__(self):
        # Set up the LLM (Gemini) and embedding model in global Settings
        Settings.llm = GoogleGenAI(model="models/gemini-2.5-flash", api_key=GEMINI_API_KEY)
        Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

        

    def summarize_text(self, text):
        documents = [Document(text=text)]
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()
        response = query_engine.query("Summarize the following textin points for presentaion slides.")
        
        return response.response

if __name__ == "__main__":
    summarizer = Summarizer()
    text = '''AI Agent for Presentations

                This project builds an AI agent using the Gemini API to automatically generate professional slide decks. 
                It will parse an input document, structure the content, and create a complete presentation file. 
                The agent will leverage various tools for tasks like image generation, data visualization, and final document formatting.
                The goal is to dramatically reduce the time and effort required to create a polished presentation.'''
    summary = summarizer.summarize_text(text)
    print(f"\nSummarized text:\n{summary}")
