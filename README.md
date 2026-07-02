# 🤖 RAG Assistant with Typesense & Groq AI

A Retrieval-Augmented Generation (RAG) application built using **LangChain**, **Typesense**, **Groq AI**, **Hugging Face Embeddings**, and **Streamlit**.

The application retrieves relevant document chunks from Typesense using vector search and generates accurate answers using Groq's Large Language Model.

---

## 🚀 Features

- 📄 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic Search using Typesense Vector Database
- 🤖 AI-powered responses using Groq LLM
- 🧠 Hugging Face sentence embeddings
- 💬 Interactive Streamlit interface
- 📚 Context-aware question answering
- 📑 Displays source documents used for generating answers

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangChain | RAG Framework |
| Typesense | Vector Database |
| Groq AI | Large Language Model |
| Hugging Face | Embedding Model |
| Streamlit | Web Interface |
| python-dotenv | Environment Variable Management |

---

## 📂 Project Structure

```
RAG/
│
├── app.py
├── .env
├── requirements.txt
│
├── src/
│   ├── config.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── prompt.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   └── utils.py
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/RAG.git
cd RAG
```

---

### 2. Create a virtual environment

Using UV

```bash
uv venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

Using UV

```bash
uv sync
```

or

```bash
uv add -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key

TYPESENSE_HOST=your_typesense_host
TYPESENSE_PORT=443
TYPESENSE_API_KEY=your_typesense_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔄 Application Workflow

```
User Question
      │
      ▼
Streamlit UI
      │
      ▼
Retriever
      │
      ▼
Typesense Vector Search
      │
      ▼
Relevant Documents
      │
      ▼
Prompt Template
      │
      ▼
Groq LLM
      │
      ▼
Final Answer
```

---

## 📁 Modules

### `config.py`

Stores project configuration and environment variables.

---

### `embeddings.py`

Loads the Hugging Face embedding model.

Model used:

```
sentence-transformers/all-MiniLM-L6-v2
```

---

### `retriever.py`

- Connects to Typesense
- Loads the vector collection
- Performs similarity search
- Returns relevant documents

---

### `prompt.py`

Creates the prompt template used by the language model.

---

### `llm.py`

Initializes the Groq language model.

Current model:

```
openai/gpt-oss-20b
```

---

### `rag_pipeline.py`

Coordinates the complete RAG workflow:

1. Retrieve documents
2. Build context
3. Generate prompt
4. Query Groq
5. Return answer and sources

---

### `utils.py`

Helper functions for:

- Formatting retrieved context
- Extracting source document names

---

## 📸 User Interface

The Streamlit application provides:

- Question input box
- AI-generated answers
- Source document display
- Loading spinner while retrieving information

---

## 📌 Current Capabilities

- Semantic document retrieval
- Context-aware AI responses
- Typesense vector search
- Groq AI integration
- Modular project architecture
- Streamlit web interface

---

## 🚧 Upcoming Features

- Upload PDF files
- Upload TXT files
- Automatic document chunking
- Automatic embedding generation
- Automatic indexing into Typesense
- Chat history
- Document management
- Multiple document support
- Source chunk visualization

---

## 👨‍💻 Author

**Parthiban P**

GitHub: https://github.com/parthi-prabha