# 📄 Pixra: Chat with PDF

### Intro
Unlock the intelligence hidden within your documents. **Pixra AI Hub** provides a sophisticated interface to transform static PDFs into dynamic, conversational knowledge bases. By leveraging state-of-the-art Retrieval-Augmented Generation (RAG), Pixra ensures high-precision responses grounded directly in your private data.

### Features
- **RAG-Powered Intelligence**: Utilize advanced Retrieval-Augmented Generation to ensure accuracy and minimize hallucinations.
- **Seamless Document Integration**: Effortlessly upload complex PDF structures for immediate analysis.
- **Context-Aware Responses**: Get precise answers derived exclusively from the uploaded content.
- **High-Tech Interface**: A streamlined, professional UI designed for optimal user experience and productivity.

### Setup

#### 1. Clone the Repository
Begin by cloning the Pixra AI Hub core repository to your local environment:
```bash
git clone https://github.com/Pixra/llms.git
cd llms/chat_with_pdf
```

#### 2. Install Dependencies
Ensure your environment is ready by installing the necessary high-performance libraries:
```bash
pip install -r requirements.txt
```

#### 3. Configure API Keys
To power the intelligence engine, configure your OpenAI API Key:
- Secure your key from the [OpenAI Dashboard](https://platform.openai.com/).
- Export your key as an environment variable or add it to your configuration file.

#### 4. Launch the Application
Deploy the interface locally using the following command:
```bash
streamlit run chat_pdf.py
```