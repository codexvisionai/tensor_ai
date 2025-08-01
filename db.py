from langchain_community.utilities import SQLDatabase
import os
from dotenv import load_dotenv
load_dotenv()

uri = os.getenv("POSTGRES_URI")
if not uri:
    raise ValueError("❌ POSTGRES_URI topilmadi. Iltimos .env faylga qo‘shing.")

db = SQLDatabase.from_uri(uri)
