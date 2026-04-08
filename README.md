# AI Health Chatbot

An intelligent chatbot application that allows users to upload medical PDF documents and ask questions about their content using advanced AI and natural language processing.

## 🚀 Features

- **Document Upload**: Upload medical PDF documents through an intuitive sidebar interface
- **AI-Powered Q&A**: Ask questions about the uploaded document and get accurate answers powered by GPT-4
- **Vector Search**: Uses FAISS vector database for efficient document retrieval
- **Streamlit Interface**: Clean, responsive web interface built with Streamlit
- **Real-time Processing**: Instant document processing and question answering
- **Chat History**: Maintains conversation history throughout the session
- **Clear Chat**: Option to reset the conversation and start fresh

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: OpenAI GPT-4o-mini, LangChain
- **Embeddings**: OpenAI Embeddings
- **Vector Database**: FAISS
- **Document Processing**: PyPDF for PDF parsing
- **Text Splitting**: RecursiveCharacterTextSplitter for optimal chunking

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher installed
- An OpenAI API key (sign up at [OpenAI](https://platform.openai.com/))

## 🔧 Installation

1. **Clone the repository** (if applicable) or download the project files:
   ```bash
   git clone <repository-url>
   cd AI-Health-Chatbot
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## 🚀 Usage

1. **Start the application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the app**:
   - Open your browser and navigate to `http://localhost:8501`

3. **Upload a document**:
   - Use the sidebar to upload a medical PDF document
   - Wait for the processing to complete (indicated by "✅ Document Ready!")

4. **Ask questions**:
   - Type your health-related questions in the chat input
   - Get AI-powered answers based on the uploaded document

5. **Clear chat** (optional):
   - Click "Clear Chat" in the sidebar to reset the conversation

## 🔍 How It Works

1. **Document Processing**:
   - Uploaded PDF is parsed using PyPDFLoader
   - Text is split into manageable chunks using RecursiveCharacterTextSplitter
   - OpenAI embeddings are generated for each chunk

2. **Vector Storage**:
   - Embeddings are stored in a FAISS vector database
   - Enables efficient similarity search for relevant content

3. **Question Answering**:
   - User queries are converted to embeddings
   - Similar document chunks are retrieved from the vector store
   - GPT-4o-mini generates answers based on retrieved context

## 📁 Project Structure

```
AI-Health-Chatbot/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
└── README.md             # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This application is for informational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical concerns.

## 🆘 Support

If you encounter any issues or have questions:

1. Check that all dependencies are installed correctly
2. Verify your OpenAI API key is valid and has sufficient credits
3. Ensure your PDF document is not corrupted and contains readable text
4. Check the console for any error messages

## 🔄 Future Enhancements

- Support for multiple document formats (DOCX, TXT, etc.)
- Multi-language support
- Advanced filtering and search options
- Integration with medical databases
- User authentication and session management
- Export chat history functionality