import streamlit as st

# ---------------------------------------------------------
# ১. হিরো সেকশন টাইটেল
# ---------------------------------------------------------
st.title("Urban Data & Planning Solutions (UDPS)")
st.subheader("Data-Driven Insights for Smarter Cities")

st.markdown("---") # বিভাজক লাইন

# ---------------------------------------------------------
# ২. মেইন কন্টেন্ট (কলাম ফিক্স করা হয়েছে)
# ---------------------------------------------------------
container = st.container()

with container:
    # সমস্যা সমাধান: st.columns(2) দেওয়া হয়েছে (আগে খালি ছিল)
    col1, col2 = st.columns(2, gap="medium") 

    with col1:
        st.write("""
        ### আমাদের লক্ষ্য
        UDPS হলো একটি নেতৃস্থানীয় কনসালটেন্সি ফার্ম যা আরবান প্ল্যানিং এবং ডেটা সায়েন্সের সমন্বয় ঘটায়। 
        
        আমরা **GIS ম্যাপিং**, **ট্র্যাফিক অ্যানালাইসিস** এবং **ডেমোগ্রাফিক মডেলিং** ব্যবহার করে 
        টেকসই এবং দক্ষ শহুরে পরিবেশ তৈরিতে সহায়তা করি।
        """)
        
        st.write("") # একটু স্পেস
        if st.button("আমাদের কাজ দেখুন", type="primary"):
            st.switch_page("portfolio.py") # বাটনে ক্লিক করলে পোর্টফোলিও পেজে নিয়ে যাবে

    with col2:
        # এখানে একটি ডেমো সিটি ইমেজ ব্যবহার করা হয়েছে
        st.image(
            "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?q=80&w=1000&auto=format&fit=crop",
            caption="Smarter Urban Environments",
            use_container_width=True
        )