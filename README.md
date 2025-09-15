# 🧠 ChatGPT-Powered Personal Assistant (RAG App)

A smart assistant that can read PDFs and answer your questions using GPT-4 + Retrieval-Augmented Generation (RAG).

## 🚀 Demo

Coming soon via Streamlit Cloud...

---

## 🧩 Features

- 📄 Upload PDFs and extract clean text
- ✂️ Smart text chunking with overlap
- 🧠 Embedding via OpenAI’s `text-embedding-ada-002`
- 🔍 FAISS-based similarity search
- 💬 GPT-generated responses with context
- 🖥️ Streamlit-powered interactive UI

---

## 📁 Folder Structure
chatgpt-rag-assistant/
├── data/                  # Uploaded documents
├── src/
│   ├── embedder.py
│   ├── vectordb.py
│   ├── retriever.py
│   └── app.py
├── .env                   # API key (not tracked)
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/yasaswinim31/chatgpt-rag-assistant.git
cd chatgpt-rag-assistant
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run src/app.py

🙋‍♀️ Author

Yasaswini M
Sr. DevOps + Aspiring AI/ML Engineer
GitHub

📄 License

MIT License
✅ Save and close the file.

---

### 📍 Step 3: Push to GitHub

In your terminal:
```bash
git add README.md
git commit -m "Add cleaned-up README.md"
git push