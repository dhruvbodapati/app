
import streamlit as st
from data import products

st.set_page_config(page_title="Support Chatbot")

st.title("💬 MiniStore Support Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# Rule-based chatbot logic
def get_response(user_input):
    user_input = user_input.lower()

    # Product Questions
    for product in products:
        if product["name"].lower() in user_input:
            return (
                f"{product['name']} costs ${product['price']}.\n"
                f"Category: {product['category']}.\n"
                f"{product['description']}"
            )

    # Delivery
    if "delivery" in user_input or "shipping" in user_input:
        return "Standard delivery takes 3-5 business days."

    # Refunds
    if "refund" in user_input:
        return "Refunds are processed within 5-7 business days after approval."

    # Returns
    if "return" in user_input:
        return "Returns are accepted within 30 days if the product is unused."

    # Payment
    if "payment" in user_input or "pay" in user_input:
        return "We accept Credit Card, Debit Card, UPI, PayPal, and Net Banking."

    # Order Status
    if "order" in user_input or "status" in user_input:
        return "Please provide your order ID to check status."

    # Product Listing
    if "products" in user_input or "show products" in user_input:
        product_names = ", ".join([p["name"] for p in products])
        return f"Available products: {product_names}"

    return "I can help with products, delivery, refunds, returns, payments, and order status."


# User input
prompt = st.chat_input("Ask your question...")

if prompt:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    response = get_response(prompt)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)