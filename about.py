# about.py
import streamlit as st

st.header("About Urban Data & Planning Solutions (UDPS)")
st.write("""
UDPS-এ, আমরা বিশ্বাস করি যে ডেটা হলো আধুনিক শহর পরিকল্পনার প্রাণ। 
আমাদের লক্ষ্য হলো শহরগুলিকে আরও বাসযোগ্য, টেকসই এবং দক্ষ করে তোলার জন্য 
অ্যাডভান্সড ডেটা অ্যানালিটিক্স এবং GIS প্রযুক্তি সরবরাহ করা।
""")

st.markdown("---")

st.subheader("Our Team")
st.write("আমাদের টিমে রয়েছেন অভিজ্ঞ আরবান প্ল্যানার, ডেটা সায়েন্টিস্ট এবং GIS বিশেষজ্ঞরা।")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/team_member_1.jpg", caption="ডঃ জেন ডো - প্রধান আরবান প্ল্যানার", use_column_width=True)
    st.write("**ডঃ জেন ডো**")
    st.write("১০+ বছরের অভিজ্ঞতাসম্পন্ন, টেকসই নগর উন্নয়নে বিশেষজ্ঞ।")

with col2:
    st.image("assets/team_member_2.jpg", caption="জন স্মিথ - লিড ডেটা সায়েন্টিস্ট", use_column_width=True)
    st.write("**জন স্মিথ**")
    st.write("প্রেডিক্টিভ মডেলিং এবং ট্র্যাফিক ফ্লো অপ্টিমাইজেশনে বিশেষজ্ঞ।")

with col3:
    st.image("assets/team_member_3.jpg", caption="আলিয়া খান - সিনিয়র GIS অ্যানালিস্ট", use_column_width=True)
    st.write("**আলিয়া খান**")
    st.write("জিওস্পেশিয়াল ডেটা ভিজ্যুয়ালাইজেশন এবং রিমোট সেন্সিং-এ দক্ষ।")