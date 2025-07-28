import streamlit as st
import os

st.title("🔧 Debug Mode")

# Debug API Key
api_key = os.getenv("OPENAI_API_KEY")
st.write(f"**API Key found:** {bool(api_key)}")
if api_key:
    st.write(f"**API Key starts with:** {api_key[:10]}...")
else:
    st.error("❌ No API Key found!")
    st.write("**Available environment variables:**")
    for key in os.environ.keys():
        if 'OPENAI' in key:
            st.write(f"- {key}")

# Test OpenAI import
try:
    from openai import OpenAI
    st.success("✅ OpenAI library imported successfully")
    
    if api_key:
        try:
            client = OpenAI(api_key=api_key)
            st.success("✅ OpenAI client created successfully")
        except Exception as e:
            st.error(f"❌ OpenAI client error: {str(e)}")
except Exception as e:
    st.error(f"❌ OpenAI import error: {str(e)}")