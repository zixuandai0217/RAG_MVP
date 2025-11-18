---

# **README.md**

# **RAG-MVP: Minimal Retrieval-Augmented Generation System**

一个轻量、可快速部署的 RAG（Retrieval-Augmented Generation）端到端 Demo，包含文档处理、向量检索、RAG 生成、FastAPI 服务与 Gradio Web Demo。
本项目结构极简，适合作为大模型应用开发实习项目、真实业务 Demo 或进一步扩展为企业级 RAG 系统的基础架构。

---

## **🌟 Features**

* **轻量级 RAG Pipeline**

  * 文本切分（chunking）
  * SentenceTransformers Embedding（MiniLM）
  * FAISS 本地向量检索
* **高扩展性**

  * 模块化架构，便于替换 embedding、模型、检索器
* **简单易用的 API**

  * FastAPI 提供 `/ask` 问答接口
* **即开即用的 Web Demo**

  * Gradio Chat 界面
* **2 分钟即可跑通，2 小时可扩展为可用系统**

---

## **📁 Project Structure**

```
rag-mvp/
│── data/
│     └── docs.txt            # 文档语料
│── embeddings/               # 向量库（运行后自动生成）
│── app/
│     ├── build_index.py      # 构建向量数据库
│     ├── retriever.py        # 检索模块
│     ├── rag.py              # RAG 生成逻辑
│     └── api.py              # FastAPI 服务端
│── demo.py                   # Gradio 网页 Demo
│── requirements.txt
│── README.md
```

---

## **🚀 Quick Start**

### **1. 安装依赖**

```bash
pip install -r requirements.txt
```

### **2. 准备文档**

编辑 `data/docs.txt`，填入你的知识库内容。

### **3. 构建向量索引**

```bash
python app/build_index.py
```

成功后会生成：

```
embeddings/index.faiss
embeddings/chunks.npy
```

### **4. 设置 API Key**

编辑 `app/rag.py`：

```python
client = OpenAI(api_key="YOUR_API_KEY")
```

支持：

* OpenAI
* DeepSeek
* Moonshot
* SiliconFlow（OpenAI API 格式）

### **5. 启动 FastAPI 服务**

```bash
uvicorn app.api:app --reload --port 8000
```

访问：

```
http://localhost:8000/ask?q=什么是RAG？
```

### **6. 启动 Gradio Demo**

```bash
python demo.py
```

打开浏览器即可使用 Web UI。

---

## **🧠 How It Works**

### **1. 文本拆分 (Chunking)**

将文档分为大小约 300 tokens 的片段，并加入 50 token 重叠，增强语义连续性。

### **2. Embedding & 向量检索**

使用 MiniLM 编码 → FAISS 建立向量索引 → 根据 query 找到 Top-k 相关 chunks。

### **3. RAG Prompting**

将检索到的内容打包为 Prompt，并交给大模型生成最终回答。

---

## **🔧 Configuration**

你可以轻松修改以下组件：

| 模块        | 可替换项                   | 示例                                                 |
| --------- | ---------------------- | -------------------------------------------------- |
| Embedding | bge-small / jina / m3  | `model = SentenceTransformer("BAAI/bge-small-en")` |
| LLM       | GPT、Qwen、DeepSeek      | `model="deepseek-chat"`                            |
| 检索        | FAISS / HNSW / Elastic | 可替换成混合检索                                           |
| API 服务    | FastAPI / Flask        | 默认 FastAPI                                         |

---

## **📈 Recommended Upgrades（快速从 MVP → 企业级）**

### **1. 混合检索（向量 + BM25）**

提升召回率，可用 Whoosh / Elasticsearch。

### **2. 重排序（Cross-Encoder）**

让回答更精准。

### **3. 自动评估体系**

基于：

* Recall@K
* F1
* BLEU / ROUGE
* GPT-as-a-judge

这是企业级 RAG 基本要求。

---

## **📜 License**

MIT License

---
