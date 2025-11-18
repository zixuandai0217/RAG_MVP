import gradio as gr
from app.rag import rag_answer

def chat(query):
    return rag_answer(query)

gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text",
    title="RAG MVP Demo (Ark)"
).launch()
