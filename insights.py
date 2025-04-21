from llama_cpp import Llama
from db import get_all_sales
from datetime import datetime

def load_llm():
    return Llama(
        model_path="mistral-7b-instruct-v0.1.Q4_K_M.gguf",
        n_ctx=2048,
        n_threads=4
    )

def get_total_revenue_april():
    sales_data = get_all_sales()
    april_sales = [
        s.amount for s in sales_data
        if s.date.month == 4
    ]
    return sum(april_sales)


def get_sales_summary(question, llm):
    # Shortcut if the question is about April total revenue
    if question.strip().lower() in [
        "what is the total revenue in april?",
        "total revenue in april?",
        "april revenue?",
        "how much revenue in april?"
    ]:
        total_april = get_total_revenue_april()
        return f"The total revenue in April is ₹{total_april}"

    # Otherwise use LLM
    sales_data = get_all_sales()

    # Format the sales data for the LLM prompt
    data_str = "\n".join(
        f"{s.date}, {s.customer_name}, {s.product_name}, {s.amount}, {s.status}"
        for s in sales_data
    )

    prompt = f"""
### Context:
You are a helpful AI assistant who analyzes sales data.

Sales data:
date, customer_name, product_name, amount, status
{data_str}

### Instruction:
Based on the above sales data, answer the following question:

### User: {question}
### Assistant:
"""

    # Generate answer using the LLM
    response = llm(prompt, max_tokens=512, stop=["###", "User:", "Assistant:"])
    return response['choices'][0]['text'].strip()
