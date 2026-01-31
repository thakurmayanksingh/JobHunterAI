import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from supabase import create_client, Client

# 1. Load Environment Variables
load_dotenv()
genai_api_key = os.getenv("GOOGLE_API_KEY")
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# 2. Page Configuration
st.set_page_config(page_title="Job Hunter AI Debugger", page_icon="🤖")
st.title("🔌 System Connection Check")

# 3. Test Gemini Connection (NEW SDK V2)
st.subheader("1. Gemini API Test")
if genai_api_key:
    try:
        # Initialize Client
        client = genai.Client(api_key=genai_api_key)

        # Send Request using gemini-2.5-flash
        # Inside the try block in app.py
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # gemini version
            contents="Say 'Hello Bunny, I am running on Gemini 2.5 Flash Free Tier!'"
        )
        st.success(f"Gemini Connected! Response: {response.text}")
    except Exception as e:
        st.error(f"Gemini Connection Failed: {e}")
else:
    st.warning("Gemini API Key not found in .env")

# 4. Test Supabase Connection
st.subheader("2. Supabase DB Test")
if supabase_url and supabase_key:
    try:
        # We are just initializing the client here to check formatting
        supabase: Client = create_client(supabase_url, supabase_key)
        st.success("Supabase Client Initialized Successfully!")
    except Exception as e:
        st.error(f"Supabase Connection Failed: {e}")
else:
    st.warning("Supabase Creds not found in .env")