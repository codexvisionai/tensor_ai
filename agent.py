# agent.py
from langchain_experimental.sql import SQLDatabaseChain
from db import db
from llm import llm

def get_sql_agent():
    return SQLDatabaseChain.from_llm(
        llm=llm,
        db=db,
        verbose=True,
        return_intermediate_steps=True  # 🟢 Bu qism SQL query va natijani alohida olish imkonini beradi
    )
