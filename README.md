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

## 📂 Project Structure

