from llm import llm
from db import db

def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

# 1. Savolni va promptni o‘qiymiz
question = read_file("question.txt")
prompt_template = read_file("prompt/prompt_template.txt")

# 2. LLM uchun SQL so‘rovini yaratish
sql_prompt = prompt_template.format(question=question)
sql_query = llm.invoke(sql_prompt).strip()

# Faqat SQL qismigacha ajratamiz (ba'zan LLM noto'g'ri matn ham qaytaradi)
sql_lines = sql_query.splitlines()
clean_sql = "\n".join(
    line for line in sql_lines if line.strip().upper().startswith("SELECT") or line.strip().startswith("FROM") or "JOIN" in line or "WHERE" in line or "GROUP BY" in line or "ORDER BY" in line or line.strip().endswith(";")
)

print("🧠 Yaralgan SQL so‘rov:\n", clean_sql)

# 3. SQL ni bajaramiz
try:
    result = db.run(clean_sql)
    print("\n📊 SQL natijasi:\n", result)
except Exception as e:
    print("❌ SQL bajarishda xato:", e)
    exit()

# 4. Natijani oddiy tilga tarjima qilamiz
explain_prompt = f"""
Savol: {question}
SQLdan olingan natija: {result}
Iltimos, foydalanuvchiga oddiy so‘zlar bilan tushuntiring. Hech qanday kod yozmang. Uzbek tilida yoz tushunarli sodda qilib va so'ralgan savolga javob ber , Uzbek tilida yoz dedim senga o'zbekcha yoz, inglizcha emas!
"""

final_answer = llm.invoke(explain_prompt)
print("\n✅ Tushunarli javob:\n", final_answer.strip())
