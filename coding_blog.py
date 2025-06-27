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
        
st.markdown("---")
st.header("📬 Contact Me")

st.markdown("""
- 📧 *Email:* [spurthi821@gmail.com](mailto:spurthi821@gmail.com)  
- 🐙 *GitHub:* [@SpurthySpu](https://github.com/SpurthySpu)  
- 📷 *Instagram:* [@spu_offical](https://www.instagram.com/_spu_offical_/)
""")

st.markdown("---")
st.header("🔗 My Projects")

st.markdown("""
- 📘 *Personal Blog (GitHub Pages):* [spurthy-m.github.io/myblog](https://spurthy-m.github.io/myblog/)
- 🎮 *Fun Quiz App (Streamlit):* [fun-quiz-app.streamlit.app](https://fun-quiz-app-y7zyflyqfhgagwe22kmdsc.streamlit.app/)
- 📝 *Coding Blog App (Streamlit):* [app-blog.streamlit.app](https://app-blog-g4fqwibfxplxxss9xfnpbn.streamlit.app/)
""")
