import streamlit as st
from data import products

st.set_page_config(
    page_title="MiniStore",
    page_icon="🛒",
    layout="wide"
)

# Initialize cart
if "cart" not in st.session_state:
    st.session_state.cart = []

# CSS Styling
st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
}

.sub-title {
    text-align: center;
    color: gray;
}

.product-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.product-name {
    font-size: 22px;
    font-weight: bold;
}

.product-price {
    font-size: 24px;
    color: green;
}

.support-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #2563eb;
    color: white;
    padding: 15px 20px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    z-index: 999;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🛍 Categories")
categories = ["All"] + list(set([p["category"] for p in products]))
selected_category = st.sidebar.radio("Select Category", categories)

st.sidebar.markdown("---")
st.sidebar.subheader("🛒 Shopping Cart")

cart_items = len(st.session_state.cart)
cart_total = sum(item["price"] for item in st.session_state.cart)

st.sidebar.write(f"Items: {cart_items}")
st.sidebar.write(f"Total: ${cart_total:.2f}")

# Header
st.markdown('<div class="main-title">🛒 MiniStore</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Your one-stop shop</div>', unsafe_allow_html=True)

# Welcome Section
st.markdown("## Welcome to MiniStore")
st.write("Discover premium products at affordable prices.")

st.markdown("## ⭐ Featured Products")

# Filtering
filtered_products = products
if selected_category != "All":
    filtered_products = [
        p for p in products if p["category"] == selected_category
    ]

# Product cards
cols = st.columns(3)

for index, product in enumerate(filtered_products):
    with cols[index % 3]:
        st.markdown(f"""
        <div class="product-card">
            <div>{product['category']}</div>
            <div class="product-name">{product['name']}</div>
            <div class="product-price">${product['price']}</div>
            <p>{product['description']}</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Add {product['name']}", key=index):
            st.session_state.cart.append(product)
            st.success("Added to cart")

# Floating support button
st.markdown("""
<a href="/Support_Chatbot" target="_self" class="support-button">
💬 Support
</a>
""", unsafe_allow_html=True)