# 🤖 Multimodal RAG System

<style>
h1, h2, h3, h4, h5, h6 {
  color: #221512 !important;
}
h2 {
  color: #72463B !important;
}
a {
  color: #B49E94 !important;
}
strong {
  color: #221512 !important;
}
</style>

An intelligent document chat system that processes PDFs and images using OpenAI GPT-4o.

## 🌐 **<a href="https://multimodal-rag-system-demo.streamlit.app/" target="_blank">🚀 LIVE DEMO - TRY IT NOW!</a>**

*Experience AI-powered document analysis in action! Upload PDFs and images to see multimodal capabilities.*

---

## 🚀 Features

- **📄 PDF Processing:** Upload PDFs and ask questions about their content
- **🖼️ Image Analysis:** AI analyzes and describes images in detail
- **💬 Intelligent Chat:** GPT-4o answers questions based on your documents
- **🎨 Modern UI:** Clean, Apple-inspired minimalist design
- **🔒 Secure:** Environment variables for API key protection
- **☁️ Cloud Ready:** Deployed on Streamlit Cloud for instant access

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **AI Model:** OpenAI GPT-4o (multimodal)
- **PDF Processing:** PyPDF2
- **Image Processing:** Pillow
- **Design:** Custom CSS with Apple-style aesthetics
- **Deployment:** Streamlit Cloud

## 📋 Installation

### Prerequisites
- Python 3.9+
- OpenAI API Key with credit balance

### Local Setup
```bash
# Clone repository
git clone https://github.com/IrinaDragunow/multimodal-rag-system.git
cd multimodal-rag-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
echo "OPENAI_API_KEY=your-api-key-here" > .env

# Start application
streamlit run app.py
```

## 🎯 Usage

1. **🌐 <a href="https://multimodal-rag-system-demo.streamlit.app/" target="_blank">Visit the Live Demo</a>**
2. **Upload documents:** Use the upload areas for PDF files or images
3. **Ask questions:** Enter your question in the text field
4. **Get AI responses:** The system analyzes your documents and provides intelligent answers

## 📊 Example Use Cases

### PDF Analysis
- Contract review and summarization
- Research paper analysis
- Invoice and document processing
- Legal document examination

### Image Analysis
- Product description generation
- Content moderation
- Visual content understanding
- Text extraction from images

## 🎨 User Interface

The application features a clean, Apple-inspired design with:
- **Minimalist color palette** using carefully selected tones
- **Smooth animations** and hover effects
- **Responsive layout** that works on all devices
- **Intuitive user experience** with clear visual feedback

## 🔗 Links

- **🌐 <a href="https://multimodal-rag-system-demo.streamlit.app/" target="_blank">Live Demo</a>**
- **📂 [GitHub Repository](https://github.com/IrinaDragunow/multimodal-rag-system)**
- **👩‍💻 [Developer Profile](https://github.com/IrinaDragunow)**

## 🚀 Deployment

### Streamlit Cloud
This application is deployed on Streamlit Cloud with:
- Automatic deployments from GitHub
- Environment variable management
- SSL certificates and custom domains
- Scalable cloud infrastructure

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable
export OPENAI_API_KEY="your-api-key"

# Run application
streamlit run app.py
```

## 🔧 Configuration

### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for GPT-4o access | Yes |

### Model Configuration
- **Model:** GPT-4o (supports text and images)
- **Max Tokens:** 1500
- **Temperature:** 0.3 (balanced creativity/consistency)

## 📈 Performance & Costs

### Response Times
- **Text-only queries:** 1-3 seconds
- **PDF processing:** 2-5 seconds
- **Image analysis:** 3-7 seconds

### API Costs (Approximate)
- **Text queries:** ~$0.005 per request
- **Image queries:** ~$0.01-0.05 per request
- **Monthly usage (demo):** $5-15

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👩‍💻 Author

**Irina Dragunow**
- GitHub: [@IrinaDragunow](https://github.com/IrinaDragunow)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)
- Live Demo: <a href="https://multimodal-rag-system-demo.streamlit.app/" target="_blank">multimodal-rag-system-demo.streamlit.app</a>

## 🎯 Project Goals

This project demonstrates:
- **Practical AI Application Development**
- **Multimodal AI Integration**
- **Production-Ready Code Structure**
- **User Experience Design**
- **Cloud Deployment Skills**

---

## 🔮 Future Enhancements

- Vector database integration for better document search
- Multiple file format support (DOCX, TXT, etc.)
- Chat history persistence
- Batch document processing
- Advanced image OCR capabilities
- User authentication system

---

*Built as a portfolio project for Machine Learning Engineer job applications. Showcases practical skills in AI integration, web development, and cloud deployment.*

## 📞 Contact

For questions about this project or collaboration opportunities, please reach out via:
- **Email:** [your.email@example.com]
- **LinkedIn:** [Your LinkedIn Profile]
- **GitHub Issues:** [Create an issue](https://github.com/IrinaDragunow/multimodal-rag-system/issues)

---

**⭐ If you found this project helpful, please give it a star!**