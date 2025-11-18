import streamlit as st
from PIL import Image

# ---------------------------------------------------------
# ১. পেজ কনফিগারেশন
# ---------------------------------------------------------
try:
    favicon = Image.open("favicon.ico") 
except:
    favicon = "🏙️"

st.set_page_config(
    page_title="UDPS - Urban Data & Planning Solutions", 
    page_icon=favicon,                                  
    layout="wide",                                      
    initial_sidebar_state="collapsed"                   
)

# ---------------------------------------------------------
# ২. CSS লোডিং ফাংশন (সংশোধিত: utf-8 এনকোডিং যুক্ত করা হয়েছে)
# ---------------------------------------------------------
def load_css(file_name):
    """স্থানীয় CSS ফাইল লোড এবং ইনজেক্ট করার ফাংশন।"""
    try:
        # এখানে encoding='utf-8' যোগ করা হয়েছে যাতে এরর না আসে
        with open(file_name, encoding='utf-8') as f:
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file '{file_name}' not found. Please create it.")
    except Exception as e:
        st.error(f"Error reading CSS file: {e}")

# CSS ফাইলটি লোড করুন (ব্র্যাকেট বা নম্বর ছাড়া)
load_css("style.css")

# ---------------------------------------------------------
# ৩. নেভিগেশন সেটআপ
# ---------------------------------------------------------
pages = {
    "Main": [
        st.Page("home.py", title="Home", icon=":material/home:"),
    ],
    "About UDPS": [
        st.Page("about.py", title="About Us", icon=":material/groups:"),
    ],
    "Work": [
        st.Page("portfolio.py", title="Portfolio", icon=":material/work:"),
    ],
    "Connect": [
        st.Page("contact.py", title="Contact", icon=":material/email:"),
    ]
}

# ৪. নেভিগেশন তৈরি করা
pg = st.navigation(pages, position="top")

# ---------------------------------------------------------
# ৫. অ্যাপ রান করা
# ---------------------------------------------------------
pg.run()