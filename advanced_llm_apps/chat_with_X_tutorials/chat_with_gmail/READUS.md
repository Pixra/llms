# 📩 Pixra Gmail Intelligence

Transform your email archive into a searchable, conversational knowledge base. **Pixra AI Hub** leverages advanced Retrieval-Augmented Generation (RAG) to bridge the gap between your Gmail inbox and Large Language Models, allowing you to extract insights and synthesize information in seconds.

### ⚡ Features

- **Contextual Retrieval**: Utilize high-fidelity **RAG technology** to ground AI responses in your actual email data.
- **Secure OAuth Integration**: Connect directly to the **Gmail API** with enterprise-grade authentication.
- **Seamless Interface**: A high-performance **Streamlit dashboard** designed for rapid querying and real-time synthesis.
- **Optimized Architecture**: Minimalist codebase engineered for **maximum efficiency** and low-latency processing.

### 🛠️ Setup

Follow these steps to deploy the Pixra Gmail Intelligence module:

#### 1. Clone the Repository
```bash
git clone https://github.com/Pixra/llms.git
cd llms/chat_with_gmail
```

#### 2. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

#### 3. Configure API Credentials
To enable secure communication between Pixra and Google:
- **Google Cloud**: Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
- **Enable API**: Activate the **Gmail API** and configure your OAuth consent screen.
- **Credentials**: Generate an **OAuth client ID**, download the JSON file, and save it as `credentials.json` in the root directory.
- **LLM Key**: Obtain your OpenAI API key (or preferred provider) and set it in your environment variables.

#### 4. Launch Application
Initialize the AI Hub locally:
```bash
streamlit run chat_gmail.py
```