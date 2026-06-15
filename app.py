import streamlit as st
from data import products

# Page setup
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛒",
    layout="wide"
)

# Session cart
if "cart" not in st.session_state:
    st.session_state.cart = []

# Custom CSS
st.markdown("""
<style>
.main-title {
    text-align:center;
    font-size:42px;
    font-weight:bold;
}
.sub-title {
    text-align:center;
    color:gray;
    margin-bottom:30px;
}
.product-card {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}
.product-name {
    font-size:22px;
    font-weight:bold;
}
.product-price {
    color:green;
    font-size:24px;
    font-weight:bold;
}
.support-btn {
    position:fixed;
    bottom:20px;
    right:20px;
    background:#2563eb;
    color:white;
    padding:15px 20px;
    border-radius:50px;
    text-decoration:none;
    font-weight:bold;
    z-index:999;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🛍 Categories")

categories = ["All"] + list(set([p["category"] for p in products]))
selected_category = st.sidebar.radio("Select Category", categories)

# Cart Summary
st.sidebar.markdown("---")
st.sidebar.subheader("🛒 Shopping Cart")

cart_count = len(st.session_state.cart)
cart_total = sum(item["price"] for item in st.session_state.cart)

st.sidebar.write(f"Items: {cart_count}")
st.sidebar.write(f"Total: ${cart_total:.2f}")

# Homepage Header
st.markdown('<div class="main-title">🛒 MiniStore</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Your one-stop shop for premium products</div>', unsafe_allow_html=True)

# Welcome
st.markdown("## Welcome to MiniStore")
st.write("Explore quality products across multiple categories.")

# Featured products
st.markdown("## ⭐ Featured Products")

filtered_products = products
if selected_category != "All":
    filtered_products = [p for p in products if p["category"] == selected_category]

# Responsive columns
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
            st.success(f"{product['name']} added to cart!")

# Floating Support Button
st.markdown("""
<a href="/Support_Chatbot" target="_self" class="support-btn">
💬 Support
</a>
""", unsafe_allow_html=True)