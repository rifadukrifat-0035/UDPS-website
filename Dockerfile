# ১. বেস ইমেজ
FROM python:3.10-slim

# ২. ওয়ার্কিং ডিরেক্টরি
WORKDIR /app

# ৩. রিকোয়ারমেন্টস কপি এবং ইনস্টল
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ৪. বাকি সব ফাইল কপি
COPY . .

# ৫. পোর্ট এক্সপোজ
EXPOSE 8501

# ৬. হেলথ চেক (অপশনাল)
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# ৭. অ্যাপ রান কমান্ড (পরিবর্তন করা হয়েছে)
# আমরা সরাসরি "streamlit" এর বদলে "python -m streamlit" ব্যবহার করছি
ENTRYPOINT ["python", "-m", "streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]