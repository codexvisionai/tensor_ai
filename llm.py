
# llm.py

from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

load_dotenv()  # .env faylni avtomatik yuklaydi

ollama_url = os.getenv("OLLAMA_URL")
if not ollama_url:
    raise ValueError("❌ OLLAMA_URL topilmadi. .env faylga qo‘shing.")

llm = Ollama(
    model="llama3:70b",        # Masalan: llama3 yoki medical-uz-assistant:latest
    base_url=ollama_url,
)
