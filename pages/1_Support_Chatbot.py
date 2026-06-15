import streamlit as st
from openai import OpenAI
from data import products

st.set_page_config(page_title="MiniStore Support")

st.title("💬 MiniStore Support Chatbot")

# OpenAI API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Product catalog for AI context
product_catalog = "\n".join([
    f"{p['name']} - ${p['price']} - {p['description']} ({p['category']})"
    for p in products
])

# System prompt
system_prompt = f"""
You are a professional customer support assistant for MiniStore.

Store Catalog:
{product_catalog}

You can ONLY answer questions related to:
- Products
- Orders
- Delivery
- Refunds
- Returns
- Payment methods

If the user asks unrelated questions, politely redirect them back to MiniStore support topics.
"""

# Display old chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask about products, delivery, refunds...")

if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # OpenAI response
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ]
    )

    reply = response.choices[0].message.content

    # Save assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    with st.chat_message("assistant"):
        st.markdown(reply)