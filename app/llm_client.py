import os
from dotenv import load_dotenv
from openai import OpenAI

# 自动读取 .env，无需 export
load_dotenv()

BASE_URL = os.getenv("ARK_BASE_URL")
API_KEY = os.getenv("ARK_API_KEY")
MODEL_ID = os.getenv("ARK_MODEL")

# 初始化 Ark 客户端
client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

def llm_answer(prompt: str):
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                ],
            }
        ],
    )
    return response.choices[0].message.content
