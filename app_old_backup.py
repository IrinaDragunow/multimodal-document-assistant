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

# Custom CSS for Apple-style minimalist design
st.markdown("""
<style>
    /* Import Inter font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styling */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom color variables based on your palette */
    :root {
        --black-chocolate: #221512;
        --bole: #72463B;
        --pale-silver: #D9C4B9;
        --tuscany: #B49E94;
        --rocket-metallic: #8B8282;
        --background: #FAFAFA;
        --surface: #FFFFFF;
        --text-primary: #221512;
        --text-secondary: #72463B;
        --accent: #B49E94;
    }
    
    /* Main container */
    .stApp {
        background: linear-gradient(135deg, #FAFAFA 0%, #F5F3F0 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Title styling */
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: var(--black-chocolate);
        text-align: center;
        margin: 2rem 0;
        letter-spacing: -0.02em;
        line-height: 1.1;
    }
    
    .subtitle {
        font-size: 1.2rem;
        font-weight: 400;
        color: var(--text-secondary);
        text-align: center;
        margin-bottom: 3rem;
        line-height: 1.5;
    }
    
    /* Card styling */
    .upload-card, .chat-card, .response-card {
        background: var(--surface);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(34, 21, 18, 0.08);
        border: 1px solid rgba(180, 158, 148, 0.15);
        backdrop-filter: blur(10px);
    }
    
    /* Upload area styling */
    .upload-area {
        border: 2px dashed var(--accent);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        background: linear-gradient(135deg, rgba(217, 196, 185, 0.1) 0%, rgba(180, 158, 148, 0.1) 100%);
        transition: all 0.3s ease;
    }
    
    .upload-area:hover {
        border-color: var(--bole);
        background: linear-gradient(135deg, rgba(217, 196, 185, 0.2) 0%, rgba(180, 158, 148, 0.2) 100%);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, var(--bole) 0%, var(--black-chocolate) 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(34, 21, 18, 0.2);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(34, 21, 18, 0.3);
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background: var(--surface);
        border: 2px solid rgba(180, 158, 148, 0.3);
        border-radius: 12px;
        padding: 1rem;
        font-size: 1rem;
        color: var(--text-primary);
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--bole);
        box-shadow: 0 0 0 3px rgba(114, 70, 59, 0.1);
    }
    
    /* File uploader styling */
    .uploadedFile {
        background: var(--surface);
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem 0;
        border: 1px solid rgba(180, 158, 148, 0.2);
    }
    
    /* Status indicators */
    .status-success {
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.1) 0%, rgba(56, 142, 60, 0.1) 100%);
        border: 1px solid rgba(76, 175, 80, 0.3);
        border-radius: 12px;
        padding: 1rem;
        color: #2E7D32;
        margin: 0.5rem 0;
        font-weight: 500;
    }
    
    .status-info {
        background: linear-gradient(135deg, rgba(180, 158, 148, 0.1) 0%, rgba(114, 70, 59, 0.1) 100%);
        border: 1px solid rgba(180, 158, 148, 0.3);
        border-radius: 12px;
        padding: 1rem;
        color: var(--bole);
        margin: 0.5rem 0;
        font-weight: 500;
    }
    
    /* Response styling */
    .ai-response {
        background: linear-gradient(135deg, rgba(217, 196, 185, 0.1) 0%, rgba(180, 158, 148, 0.05) 100%);
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        border-left: 4px solid var(--bole);
        font-size: 1.1rem;
        line-height: 1.6;
        color: var(--text-primary);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, var(--surface) 0%, rgba(217, 196, 185, 0.1) 100%);
        border-right: 1px solid rgba(180, 158, 148, 0.2);
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--black-chocolate);
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid rgba(180, 158, 148, 0.2);
    }
    
    /* Feature cards */
    .feature-card {
        background: var(--surface);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
        border: 1px solid rgba(180, 158, 148, 0.15);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(34, 21, 18, 0.1);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    /* Loading animation */
    .stSpinner {
        border-top-color: var(--bole) !important;
    }
    
    /* Custom spacing */
    .spacer {
        height: 2rem;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 3rem 0 2rem 0;
        color: var(--text-secondary);
        font-size: 0.9rem;
        border-top: 1px solid rgba(180, 158, 148, 0.2);
        margin-top: 4rem;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: var(--surface);
        border-radius: 12px;
        border: 1px solid rgba(180, 158, 148, 0.2);
    }
    
    /* Success/Error message styling */
    .stAlert {
        border-radius: 12px;
        border: none;
    }
    
    /* Metric styling */
    .metric-card {
        background: var(--surface);
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid rgba(180, 158, 148, 0.15);
        text-align: center;
    }
    
    /* Image styling */
    .stImage {
        border-radius: 12px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF with elegant error handling"""
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
    """Convert image to base64 for API"""
    try:
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return img_str
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")
        return ""

def get_response(text_content, image_content, question):
    """Get AI response with elegant error handling"""
    try:
        messages = [
            {
                "role": "system", 
                "content": "You are a sophisticated AI assistant. Provide clear, insightful responses. Format your answers beautifully with proper structure and use markdown when appropriate."
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
        return f"❌ Error: {str(e)}\n\nPlease check your API key and credit balance."

# Main Title
st.markdown('<h1 class="main-title">AI Document Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Intelligent document analysis with multimodal AI capabilities</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="section-header">💡 Example Queries</div>', unsafe_allow_html=True)
    
    # Feature cards
    examples = [
        ("📄", "PDF Analysis", "• Summarize this document<br>• Extract key information<br>• Find specific details"),
        ("🖼️", "Image Analysis", "• Describe this image<br>• Extract visible text<br>• Analyze content"),
        ("🧠", "General AI", "• Explain concepts<br>• Answer questions<br>• Provide insights")
    ]
    
    for icon, title, description in examples:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <h4 style="margin: 0.5rem 0; color: var(--black-chocolate);">{title}</h4>
            <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.4; margin: 0;">{description}</p>
        </div>
        """, unsafe_allow_html=True)

# Main Content Area - Full Width
st.markdown('<div class="section-header">💬 Ask a Question</div>', unsafe_allow_html=True)

# Upload Section
st.markdown("### 📁 Upload Documents")
col_upload1, col_upload2 = st.columns(2)

# PDF Upload
with col_upload1:
    st.markdown("**📄 PDF Document**")
    pdf_file = st.file_uploader(
        "Choose a PDF file",
        type="pdf",
        help="Upload any PDF document for analysis",
        key="pdf_uploader"
    )
    
    pdf_text = ""
    if pdf_file:
        with st.spinner("Processing PDF..."):
            pdf_text = extract_text_from_pdf(pdf_file)
        
        if pdf_text:
            st.markdown('<div class="status-success">✅ PDF loaded successfully</div>', unsafe_allow_html=True)
            st.markdown(f"**Length:** {len(pdf_text):,} characters")
            preview = pdf_text[:150] + "..." if len(pdf_text) > 150 else pdf_text
            with st.expander("📖 Preview"):
                st.text(preview)
        else:
            st.error("❌ Could not process PDF")

# Image Upload  
with col_upload2:
    st.markdown("**🖼️ Image**")
    image_file = st.file_uploader(
        "Choose an image file",
        type=["png", "jpg", "jpeg"],
        help="Upload any image for AI analysis",
        key="image_uploader"
    )
    
    image_base64 = ""
    if image_file:
        image = Image.open(image_file)
        st.image(image, use_column_width=True, caption="Uploaded Image")
        
        with st.spinner("Processing image..."):
            image_base64 = encode_image(image)
        
        if image_base64:
            st.markdown('<div class="status-success">✅ Image ready for analysis</div>', unsafe_allow_html=True)
        else:
            st.error("❌ Could not process image")

# Status indicators
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
    
# Question input
question = st.text_input(
    "Your question:",
    placeholder="What would you like to know about your documents?",
    help="Ask anything about your uploaded documents or general questions"
)

# Generate button
if st.button("✨ Generate Answer", type="primary", use_container_width=True):
    if question and question.strip():
        with st.spinner("AI is analyzing..."):
            response = get_response(pdf_text, image_base64, question)
        
        st.markdown('<div class="section-header">🎯 Response</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="ai-response">{response}</div>', unsafe_allow_html=True)
        
        # Sources used
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

with col2:
    st.markdown('<div class="section-header">💡 Example Queries</div>', unsafe_allow_html=True)
    
    # Feature cards
    examples = [
        ("📄", "PDF Analysis", "• Summarize this document<br>• Extract key information<br>• Find specific details"),
        ("🖼️", "Image Analysis", "• Describe this image<br>• Extract visible text<br>• Analyze content"),
        ("🧠", "General AI", "• Explain concepts<br>• Answer questions<br>• Provide insights")
    ]
    
    for icon, title, description in examples:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <h4 style="margin: 0.5rem 0; color: var(--black-chocolate);">{title}</h4>
            <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.4; margin: 0;">{description}</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-header">💡 Example Queries</div>', unsafe_allow_html=True)
    
    # Feature cards
    examples = [
        ("📄", "PDF Analysis", "• Summarize this document<br>• Extract key information<br>• Find specific details"),
        ("🖼️", "Image Analysis", "• Describe this image<br>• Extract visible text<br>• Analyze content"),
        ("🧠", "General AI", "• Explain concepts<br>• Answer questions<br>• Provide insights")
    ]
    
    for icon, title, description in examples:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <h4 style="margin: 0.5rem 0; color: var(--black-chocolate);">{title}</h4>
            <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.4; margin: 0;">{description}</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    <p><strong>AI Document Assistant</strong> • Built with Streamlit & OpenAI GPT-4o</p>
    <p>Designed for intelligent document analysis and multimodal AI interaction</p>
</div>
""", unsafe_allow_html=True)

# Debug panel (collapsible)
with st.expander("🔧 Debug Information", expanded=False):
    debug_info = {
        "API Key Status": "✅ Connected" if os.getenv("OPENAI_API_KEY") else "❌ Missing",
        "PDF Loaded": "✅ Yes" if pdf_text else "❌ No", 
        "Image Loaded": "✅ Yes" if image_base64 else "❌ No",
        "PDF Length": f"{len(pdf_text):,} characters" if pdf_text else "0 characters",
        "Streamlit Version": st.__version__,
        "Python Version": f"{os.sys.version_info.major}.{os.sys.version_info.minor}"
    }
    
    for key, value in debug_info.items():
        st.markdown(f"**{key}:** {value}")