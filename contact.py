# contact.py
import streamlit as st

def get_form_html(email_url):
    """
    FormSubmit.co-এর জন্য একটি কাস্টম HTML ফর্ম জেনারেট করে।
    CSS স্টাইলগুলি আমাদের গ্লোবাল style.css ফাইল থেকে আসবে।
    """
    # HTML ফর্মের জন্য W3Schools থেকে অনুপ্রাণিত [44] এবং FormSubmit-এর জন্য কাস্টমাইজড [45]
    form_html = f"""
    <form action="{email_url}" method="POST" class="contact-form">
        <input type="hidden" name="_captcha" value="false">
        
        <label for="name">Your Name</label>
        <input type="text" id="name" name="name" placeholder="আপনার নাম..." required>

        <label for="email">Your Email</label>
        <input type="email" id="email" name="email" placeholder="আপনার ইমেল..." required>

        <label for="subject">Subject</label>
        <input type="text" id="subject" name="_subject" placeholder="বিষয়...">

        <label for="message">Message</label>
        <textarea id="message" name="message" placeholder="আপনার বার্তা লিখুন..." style="height:200px" required></textarea>

        <button type="submit" class="form-submit-btn">Send Message</button>
    </form>
    """
    return form_html

def get_form_css():
    """CSS স্টাইল যা শুধুমাত্র এই পেজের ফর্মের জন্য প্রযোজ্য"""
    return """
    <style>
       .contact-form {{
            background: #FFFFFF;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
       .contact-form input[type=text],
       .contact-form input[type=email],
       .contact-form textarea {{
            width: 100%;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 4px;
            margin-top: 6px;
            margin-bottom: 16px;
            resize: vertical;
        }}
       .contact-form label {{
            font-weight: 600;
        }}
       .contact-form button[type=submit] {{
            background-color: #3C7A89;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            font-size: 1rem;
            font-weight: 600;
        }}
       .contact-form button[type=submit]:hover {{
            background-color: #2E4756;
        }}
    </style>
    """

st.header("Contact Us")
st.write("আমাদের সাথে কাজ করতে আগ্রহী? নিচের ফর্মটি পূরণ করুন অথবা আমাদের সরাসরি ইমেল করুন।")

# গুরুত্বপূর্ণ: FormSubmit.co-তে আপনার ইমেল অ্যাড্রেস দিয়ে এটি প্রতিস্থাপন করুন
CONTACT_EMAIL_URL = "https://formsubmit.co/your-email@udps.com" # [42, 45]

# CSS এবং HTML ফর্ম রেন্ডার করুন
st.markdown(get_form_css(), unsafe_allow_html=True)
st.markdown(get_form_html(CONTACT_EMAIL_URL), unsafe_allow_html=True) #