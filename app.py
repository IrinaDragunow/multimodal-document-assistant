import streamlit as st

# Configure page FIRST - before any other Streamlit commands
st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="⚫",
    layout="wide",
    initial_sidebar_state="expanded"
)

import openai
from dotenv import load_dotenv
import os
import PyPDF2
from PIL import Image
import base64
import io

# Load environment variables
load_dotenv()

# Initialize OpenAI client
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    :root {
        --black-chocolate: #221512;
        --bole: #72463B;
        --pale-silver: #D9C4B9;
        --tuscany: #B49E94;
        --text-primary: #221512;
        --text-secondary: #72463B;
    }
    
    .stApp {
        background: linear-gradient(135deg, #FAFAFA 0%, #F5F3F0 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: var(--black-chocolate);
        text-align: center;
        margin: 2rem 0;
        letter-spacing: -0.02em;
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: var(--text-secondary);
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, var(--bole) 0%, var(--black-chocolate) 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .status-success {
        background: rgba(76, 175, 80, 0.1);
        border: 1px solid rgba(76, 175, 80, 0.3);
        border-radius: 12px;
        padding: 1rem;
        color: #2E7D32;
        margin: 0.5rem 0;
    }
    
    .status-info {
        background: rgba(180, 158, 148, 0.1);
        border: 1px solid rgba(180, 158, 148, 0.3);
        border-radius: 12px;
        padding: 1rem;
        color: var(--bole);
        margin: 0.5rem 0;
    }
    
    .ai-response {
        background: rgba(217, 196, 185, 0.1);
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        border-left: 4px solid var(--bole);
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    .feature-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(180, 158, 148, 0.15);
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(34, 21, 18, 0.1);
    }
</style>
""", unsafe_allow_html=True)

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF"""
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num, page in enumerate(reader.pages):
            page_text = page.extract_text()
            text += f"\n--- Page {page_num + 1} ---\n{page_text}"
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return ""

def encode_image(image):
    """Convert image to base64"""
    try:
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return img_str
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")
        return ""

def get_response(text_content, image_content, question):
    """Get AI response"""
    try:
        messages = [
            {
                "role": "system", 
                "content": "You are a helpful AI assistant. Provide clear, insightful responses."
            }
        ]
        
        user_message = {"role": "user", "content": []}
        
        if text_content and text_content.strip():
            user_message["content"].append({
                "type": "text", 
                "text": f"DOCUMENT CONTENT:\n{text_content}\n\nQUESTION: {question}"
            })
        
        if image_content:
            user_message["content"].append({
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{image_content}"}
            })
        
        if not text_content and not image_content:
            user_message["content"].append({
                "type": "text",
                "text": question
            })
        
        messages.append(user_message)
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=1500,
            temperature=0.3
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Main Title
st.markdown('<h1 class="main-title">AI Document Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Intelligent document analysis with multimodal AI capabilities</p>', unsafe_allow_html=True)

# Sidebar with Examples
with st.sidebar:
    st.markdown("### 💡 Example Queries")
    
    examples = [
        ("📄", "PDF Analysis", "Summarize documents\nExtract key information\nFind specific details"),
        ("🖼️", "Image Analysis", "Describe images\nExtract visible text\nAnalyze content"),
        ("🧠", "General AI", "Explain concepts\nAnswer questions\nProvide insights")
    ]
    
    for icon, title, description in examples:
        st.markdown(f"""
        <div class="feature-card">
            <div style="font-size: 2rem; margin-bottom: 1rem;">{icon}</div>
            <h4 style="margin: 0.5rem 0; color: var(--black-chocolate);">{title}</h4>
            <p style="font-size: 0.9rem; color: var(--text-secondary); margin: 0;">{description}</p>
        </div>
        """, unsafe_allow_html=True)

# Main Content
st.markdown("### 📁 Upload Documents")

# Upload areas
col1, col2 = st.columns(2)

# PDF Upload
with col1:
    st.markdown("**📄 PDF Document**")
    pdf_file = st.file_uploader("Choose PDF", type="pdf", key="pdf")
    
    pdf_text = ""
    if pdf_file:
        with st.spinner("Processing PDF..."):
            pdf_text = extract_text_from_pdf(pdf_file)
        
        if pdf_text:
            st.markdown('<div class="status-success">✅ PDF loaded successfully</div>', unsafe_allow_html=True)
            st.markdown(f"**Length:** {len(pdf_text):,} characters")

# Image Upload  
with col2:
    st.markdown("**🖼️ Image**")
    image_file = st.file_uploader("Choose Image", type=["png", "jpg", "jpeg"], key="image")
    
    image_base64 = ""
    if image_file:
        image = Image.open(image_file)
        st.image(image, use_column_width=True)
        
        with st.spinner("Processing image..."):
            image_base64 = encode_image(image)
        
        if image_base64:
            st.markdown('<div class="status-success">✅ Image ready</div>', unsafe_allow_html=True)

# Status
st.markdown("### 📊 Status")
col_status1, col_status2 = st.columns(2)

with col_status1:
    if pdf_text:
        st.markdown('<div class="status-success">📄 PDF Ready</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-info">📄 No PDF loaded</div>', unsafe_allow_html=True)

with col_status2:
    if image_base64:
        st.markdown('<div class="status-success">🖼️ Image Ready</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-info">🖼️ No image loaded</div>', unsafe_allow_html=True)

# Question Section
st.markdown("### 💬 Ask a Question")

question = st.text_input(
    "Your question:",
    placeholder="What would you like to know?"
)

if st.button("✨ Generate Answer", type="primary"):
    if question and question.strip():
        with st.spinner("AI is analyzing..."):
            response = get_response(pdf_text, image_base64, question)
        
        st.markdown("### 🎯 Response")
        st.markdown(f'<div class="ai-response">{response}</div>', unsafe_allow_html=True)
        
        # Sources
        sources = []
        if pdf_text:
            sources.append("📄 PDF Document")
        if image_base64:
            sources.append("🖼️ Image")
        
        if sources:
            st.markdown(f"**Sources:** {' • '.join(sources)}")
        else:
            st.markdown("**Source:** General AI Knowledge")
            
    else:
        st.warning("⚠️ Please enter a question")

# Debug Info
with st.expander("🔧 Debug Information"):
    st.markdown(f"**API Key:** {'✅ Connected' if os.getenv('OPENAI_API_KEY') else '❌ Missing'}")
    st.markdown(f"**PDF:** {'✅ Loaded' if pdf_text else '❌ None'}")
    st.markdown(f"**Image:** {'✅ Loaded' if image_base64 else '❌ None'}")