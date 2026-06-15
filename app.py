import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛒",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS Styling
# ---------------------------------------------------
st.markdown("""
<style>
    /* Main background */
    .main {
        background-color: #f8fafc;
    }

    /* Header */
    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: #0f172a;
        text-align: center;
    }

    .sub-title {
        text-align: center;
        color: #475569;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Product cards */
    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        transition: 0.3s;
        min-height: 280px;
    }

    .product-card:hover {
        transform: translateY(-5px);
    }

    .product-name {
        font-size: 22px;
        font-weight: bold;
        color: #111827;
    }

    .product-category {
        color: #2563eb;
        font-size: 14px;
        font-weight: 600;
    }

    .product-price {
        font-size: 24px;
        color: #16a34a;
        font-weight: bold;
        margin-top: 10px;
    }

    .product-desc {
        color: #4b5563;
        margin-top: 10px;
        font-size: 15px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111827;
        color: white;
    }

    .cart-box {
        background-color: #1f2937;
        padding: 15px;
        border-radius: 10px;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Sample Product Data
# ---------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 79.99,
        "description": "Noise-cancelling Bluetooth headphones with premium sound.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 129.99,
        "description": "Track fitness, calls, and notifications with style.",
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "price": 59.99,
        "description": "Lightweight and comfortable shoes for everyday running.",
        "category": "Fashion"
    },
    {
        "name": "Backpack",
        "price": 39.99,
        "description": "Durable waterproof backpack for school, work, or travel.",
        "category": "Accessories"
    },
    {
        "name": "Gaming Mouse",
        "price": 45.50,
        "description": "Ergonomic RGB gaming mouse with high precision tracking.",
        "category": "Gaming"
    },
    {
        "name": "Coffee Maker",
        "price": 89.99,
        "description": "Automatic coffee machine with quick brew technology.",
        "category": "Home Appliances"
    }
]

# ---------------------------------------------------
# Initialize Cart
# ---------------------------------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# ---------------------------------------------------
# Sidebar Section
# ---------------------------------------------------
st.sidebar.title("🛍 Categories")

categories = ["All"] + list(set([p["category"] for p in products]))
selected_category = st.sidebar.radio("Select Category", categories)

# Shopping cart summary
st.sidebar.markdown("---")
st.sidebar.subheader("🛒 Shopping Cart")

cart_items = len(st.session_state.cart)
cart_total = sum(item["price"] for item in st.session_state.cart)

st.sidebar.markdown(f"""
<div class="cart-box">
    <p><b>Items:</b> {cart_items}</p>
    <p><b>Total:</b> ${cart_total:.2f}</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Homepage Header
# ---------------------------------------------------
st.markdown('<div class="main-title">🛒 MiniStore</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Your one-stop shop for the best products online</div>',
    unsafe_allow_html=True
)

# Welcome Section
st.markdown("## Welcome to MiniStore")
st.write("""
Discover premium products across multiple categories.
Enjoy a clean shopping experience with modern design and easy browsing.
""")

st.markdown("---")

# ---------------------------------------------------
# Featured Products Section
# ---------------------------------------------------
st.markdown("## ⭐ Featured Products")

# Filter products based on selected category
filtered_products = products
if selected_category != "All":
    filtered_products = [
        product for product in products
        if product["category"] == selected_category
    ]

# Create responsive product layout using columns
cols = st.columns(3)

for index, product in enumerate(filtered_products):
    with cols[index % 3]:
        st.markdown(f"""
        <div class="product-card">
            <div class="product-category">{product['category']}</div>
            <div class="product-name">{product['name']}</div>
            <div class="product-price">${product['price']}</div>
            <div class="product-desc">{product['description']}</div>
        </div>
        """, unsafe_allow_html=True)

        # Add to cart button
        if st.button(f"Add to Cart - {product['name']}", key=index):
            st.session_state.cart.append(product)
            st.success(f"{product['name']} added to cart!")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("---")
st.markdown(
    "<center>© 2026 MiniStore | Built with Streamlit</center>",
    unsafe_allow_html=True
)



























































































































































































































































































































