# RAG-MVP: Minimal Retrieval-Augmented Generation System

一个轻量、可快速部署的 RAG（Retrieval-Augmented Generation）端到端 Demo，包含文档处理、向量检索、RAG 生成、FastAPI 服务与 Gradio Web Demo。
本项目结构极简，适合进一步扩展为企业级 RAG 系统的基础架构。

---

## 🌟 Features

* **轻量级 RAG Pipeline**
  * 文本切分（chunking）
  * SentenceTransformers Embedding（MiniLM）
  * FAISS 本地向量检索
* **高扩展性**
  * 模块化架构，便于替换 embedding、模型、检索器
* **简单易用的 API**
  * FastAPI 提供 `/ask` 问答接口，支持 UTF-8 编码
* **即开即用的 Web Demo**
  * Gradio Chat 界面
* **一键运行脚本**
  * `run.sh` 自动安装依赖、构建索引、启动服务
* **2 分钟即可跑通，2 小时可扩展为可用系统**

---

## 📁 Project Structure

```
RAG_MVP/
│── data/
│     └── example.txt          # 知识库文档
│── embeddings/
│     ├── index.faiss          # FAISS 向量索引
│     └── chunks.npy           # 文本块数据
│── app/
│     ├── build_index.py       # 构建向量索引
│     ├── retriever.py         # 向量检索模块
│     ├── llm_client.py        # LLM 客户端（支持 Ark）
│     ├── rag.py               # RAG 核心逻辑
│     └── api.py               # FastAPI 服务
│── demo.py                    # Gradio Web Demo
│── .env                       # 环境变量配置
│── .gitignore
│── requirements.txt           # Python 依赖
│── run.sh                     # 一键运行脚本
│── README.md
```

---

## 🚀 Quick Start

### 方法一：使用一键运行脚本（推荐）

```bash
chmod +x run.sh
./run.sh
```

脚本会自动完成：
1. 安装依赖包
2. 构建向量索引
3. 启动 FastAPI 服务（端口 8000）

### 方法二：手动启动

#### 1. 安装依赖

```bash
pip install -r requirements.txt
```

#### 2. 准备文档

编辑 `data/example.txt`，填入你的知识库内容。

#### 3. 构建向量索引

```bash
python app/build_index.py
```

成功后会生成：
```
embeddings/index.faiss
embeddings/chunks.npy
```

#### 4. 配置环境变量

创建 `.env` 文件，配置 Ark API 信息：

```bash
ARK_BASE_URL=https://your-ark-api-url
ARK_API_KEY=your-api-key
ARK_MODEL=your-model-id
```

**支持的 LLM 服务：**
* Ark（当前配置）
* OpenAI（兼容 OpenAI API 格式）
* DeepSeek
* Moonshot
* SiliconFlow（OpenAI API 格式）

只需修改 `.env` 中的配置即可切换不同的 LLM 服务。

#### 5. 启动 FastAPI 服务

```bash
uvicorn app.api:app --reload --port 8000
```

访问 API：

```bash
# 浏览器访问
http://localhost:8000/ask?q=什么是RAG？

# 或使用 curl
curl "http://localhost:8000/ask?q=什么是RAG？"
```

**响应格式：**
```json
{
  "answer": "RAG 是 Retrieval-Augmented Generation 的缩写，指通过检索增强生成能力的技术..."
}
```

#### 6. 启动 Gradio Demo（可选）

```bash
python demo.py
```

打开浏览器即可使用 Web UI（默认地址：http://127.0.0.1:7860）。

---

## 🧠 How It Works

### 1. 文本拆分 (Chunking)

将文档分为大小约 300 tokens 的片段，并加入 50 token 重叠，增强语义连续性。

### 2. Embedding & 向量检索

使用 MiniLM 编码 → FAISS 建立向量索引 → 根据 query 找到 Top-k 相关 chunks（默认 top_k=3）。

### 3. RAG Prompting

将检索到的内容打包为 Prompt，并交给大模型生成最终回答。如果上下文未包含答案，模型会回复"文档中未找到相关信息"。

---

## 🔧 Configuration

你可以轻松修改以下组件：

| 模块        | 可替换项                   | 示例                                                 |
| --------- | ---------------------- | -------------------------------------------------- |
| Embedding | bge-small / jina / m3  | `model = SentenceTransformer("BAAI/bge-small-en")` |
| LLM       | GPT、Qwen、DeepSeek、Ark | 修改 `.env` 中的配置即可                              |
| 检索        | FAISS / HNSW / Elastic | 可替换成混合检索                                           |
| API 服务    | FastAPI / Flask        | 默认 FastAPI                                         |

### 修改检索数量

编辑 `app/rag.py` 中的 `retrieve(query)` 调用，修改 `top_k` 参数：

```python
contexts = retrieve(query, top_k=5)  # 默认是 3
```

### 修改文本块大小

编辑 `app/build_index.py` 中的 `split_text` 函数参数：

```python
chunks = split_text(text, chunk_size=500, overlap=100)  # 默认 300, 50
```

---

## 📈 Recommended Upgrades（快速从 MVP → 企业级）

### 1. 混合检索（向量 + BM25）

提升召回率，可用 Whoosh / Elasticsearch。

### 2. 重排序（Cross-Encoder）

让回答更精准。

### 3. 自动评估体系

基于：
* Recall@K
* F1
* BLEU / ROUGE
* GPT-as-a-judge

这是企业级 RAG 基本要求。

### 4. 多文档支持

扩展 `build_index.py` 支持批量处理多个文档。

### 5. 对话历史

在 RAG pipeline 中加入对话上下文管理。

---

## 🐛 Troubleshooting

### 中文乱码问题

已修复：API 响应使用 `JSONResponse` 并设置 `charset=utf-8`，确保中文正常显示。

### 索引构建失败

确保 `data/example.txt` 文件存在且包含内容。

### API 连接失败

检查 `.env` 文件中的配置是否正确，确保网络可以访问对应的 API 服务。

---

## 📜 License

MIT License

---
