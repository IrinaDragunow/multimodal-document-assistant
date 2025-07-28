# 🤖 Multimodal RAG System

An intelligent document chat system that processes PDFs and images using AI.

## 🚀 Features
- **📄 PDF Processing:** Upload PDFs and ask questions about their content
- **🖼️ Image Analysis:** AI analyzes and describes images
- **💬 Intelligent Chat:** GPT-4 Vision answers questions based on your documents
- **🎨 Modern UI:** User-friendly Streamlit interface

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI Model:** OpenAI GPT-4 Vision
- **PDF Processing:** PyPDF2
- **Image Processing:** Pillow
- **Deployment:** Streamlit Cloud

## 📋 Installation

### Prerequisites
- Python 3.9+
- OpenAI API Key

### Setup
```bash
# Clone repository
git clone https://github.com/YOUR-USERNAME/multimodal-rag-system.git
cd multimodal-rag-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
echo "OPENAI_API_KEY=sk-your-api-key" > .env

# Start app
streamlit run app.py# multimodal-rag-system
