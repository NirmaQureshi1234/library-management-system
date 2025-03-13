import json
import os
import streamlit as st

# 📂 File Path
DATA_FILE = "library.json"

# ✅ Load Data
def load_library():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# ✅ Save Data
def save_library(library):
    with open(DATA_FILE, "w") as file:
        json.dump(library, file, indent=4)

# ✅ Streamlit UI
st.set_page_config(page_title="📚 Library System", layout="wide", page_icon="📚")

# 🎨 Custom CSS for Dark Theme and Styling
st.markdown(
    """
    <style>
        body, .stApp {
            background-color: #0E0E0E;
            color: #F8F8F8;
        }
        .stSidebar, .css-1d391kg {
            background-color: #1A1A1A;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF;
        }
        .stButton > button {
            background: linear-gradient(135deg, #FFD700 10%, #FF6347 100%);
            color: black;
            font-weight: bold;
            border-radius: 10px;
            padding: 8px;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background: linear-gradient(135deg, #FF6347 10%, #FFD700 100%);
        }
        .metric-container {
            border: 2px solid #FFD700;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            background: #222;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📚 Library Management System")

# Load Books
library = load_library()

# 🎯 Sidebar: Add a New Book
st.sidebar.header("➕ Add New Book")
st.sidebar.markdown("<hr style='border:1px solid #FFD700'>", unsafe_allow_html=True)
title = st.sidebar.text_input("📖 Title")
author = st.sidebar.text_input("✍️ Author")
year = st.sidebar.text_input("📆 Year", max_chars=4)
genre = st.sidebar.text_input("🎭 Genre")
read = st.sidebar.checkbox("✅ Mark as Read")

if st.sidebar.button("Add Book"):
    if title and author and year.isdigit() and genre:
        new_book = {
            "title": title.title(),
            "author": author.title(),
            "year": year,
            "genre": genre.capitalize(),
            "read": read,
        }
        library.append(new_book)
        save_library(library)
        st.sidebar.success(f'📚 "{title}" added successfully!')
        st.rerun()
    else:
        st.sidebar.error("❌ Please fill all fields correctly!")

# 🎯 Sidebar: Remove a Book
st.sidebar.header("🗑 Remove Book")
remove_title = st.sidebar.text_input("Enter title to remove")

if st.sidebar.button("Remove Book"):
    updated_library = [book for book in library if book["title"].lower() != remove_title.lower()]
    if len(updated_library) < len(library):
        save_library(updated_library)
        st.sidebar.success(f'🗑 "{remove_title}" removed!')
        st.rerun()
    else:
        st.sidebar.error("❌ Book not found!")

# 🎯 Sidebar: Search Book
st.sidebar.header("🔍 Search Books")
st.sidebar.markdown("<hr style='border:1px solid #FFD700'>", unsafe_allow_html=True)
search_by = st.sidebar.radio("Search by", ["Title", "Author"])
search_term = st.sidebar.text_input(f"Enter {search_by.lower()}")

if st.sidebar.button("Search"):
    results = [book for book in library if search_term.lower() in book[search_by.lower()].lower()]
    if results:
        st.subheader("🔎 Search Results")
        for book in results:
            st.write(
                f'📘 **{book["title"]}** by *{book["author"]}* ({book["year"]}) - {"✅ Read" if book["read"] else "❌ Not Read"}'
            )
    else:
        st.warning("❌ No books found!")

# 📌 Display Books Collection
st.write("## 📚 Library Collection")
if library:
    for book in library:
        st.write(
            f'📘 **{book["title"]}** by *{book["author"]}* ({book["year"]}) - {"✅ Read" if book["read"] else "❌ Not Read"}'
        )
else:
    st.info("📭 No books available.")

# 📊 Display Statistics
st.write("## 📊 Library Statistics")
total_books = len(library)
read_books = sum(1 for book in library if book["read"])
perc_read = (read_books / total_books) * 100 if total_books > 0 else 0

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='metric-container'>📖 Total Books</div>", unsafe_allow_html=True)
    st.metric("", total_books)
with col2:
    st.markdown("<div class='metric-container'>✅ Books Read</div>", unsafe_allow_html=True)
    st.metric("", read_books)
with col3:
    st.markdown("<div class='metric-container'>📈 Read Percentage</div>", unsafe_allow_html=True)
    st.metric("", f"{perc_read:.2f}%")


 
  

  
