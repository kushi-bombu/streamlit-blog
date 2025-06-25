import streamlit as st
import os

st.set_page_config(page_title="Spurthy's Coding Blog")

st.title("👩‍💻 Spurthy's Coding Blog")
st.markdown("Welcome to my blog! I share beginner-friendly coding tutorials.")

# Load blog posts
post_dir = "posts"

for post_file in sorted(os.listdir(post_dir)):
    with open(os.path.join(post_dir, post_file), "r", encoding="utf-8") as f:
        content = f.read()
        st.markdown("---")
        st.markdown(content, unsafe_allow_html=True)
