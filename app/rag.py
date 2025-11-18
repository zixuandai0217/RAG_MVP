from app.retriever import retrieve
from app.llm_client import llm_answer

def rag_answer(query):
    contexts = retrieve(query)
    context_text = "\n\n---\n".join(contexts)

    prompt = f"""
你是一个严格基于知识库回答的助手，请使用提供的上下文回答问题。

【上下文】
{context_text}

【问题】
{query}

【要求】
- 若上下文未包含答案，请回复“文档中未找到相关信息”
- 不允许编造信息
"""

    return llm_answer(prompt)
