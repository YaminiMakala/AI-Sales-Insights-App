# AI-Sales-Insights-App
# 💼 LLM-Powered Sales Dashboard

An interactive Streamlit dashboard that uses a local LLM (Mistral 7B Instruct - GGUF) to analyze sales data and answer natural language questions like:

> “What is the total revenue in April?”

---

## 🧠 Features

- 🧾 Query sales data using natural language
- 🤖 Powered by `llama-cpp-python` running **Mistral-7B-Instruct GGUF**
- 📊 Structured data stored in SQLite
- ⚡ Fast, offline, and open-source – no API keys required

---

## 🚀 How It Works

1. Streamlit provides a clean UI.
2. SQLite stores sales data.
3. LLM reads your question and analyzes sales data.
4. Optionally, custom Python logic handles direct calculations (e.g., total revenue).

---

## 🛠️ Tech Stack

| Component | Tool |
|----------|------|
| UI | Streamlit |
| LLM | [Mistral-7B-Instruct (GGUF)](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) via `llama-cpp-python` |
| DB | SQLite |
| Lang | Python 3.10+ |

---

## ⚙️ Installation

1. **Clone the repo**  
```bash
git clone https://github.com/your-username/llm_sales_dashboard.git
cd llm_sales_dashboard
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Download the Mistral model (GGUF)
Place mistral-7b-instruct-v0.1.Q4_K_M.gguf inside the models/ folder. You can download it from:

👉 TheBloke/Mistral-7B-Instruct-GGUF

Run the App

bash
Copy
Edit
streamlit run app.py
✨ Example Questions
What is the total revenue in April?

Who are the top customers?

What products sold the most?

How many unpaid orders do we have?

📈 Screenshot
![image](https://github.com/user-attachments/assets/cb0bd01b-5e3b-482d-ba8d-b95271b20ab6)


🙌 Author
Yamini – Passionate about AI, LLMs, and building smart apps.
📍 From Vizag | 🚀 Dreaming of the stars

