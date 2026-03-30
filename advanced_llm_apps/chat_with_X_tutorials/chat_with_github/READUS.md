# 🐙 Chat with GitHub Repo

Unlock the collective intelligence of any codebase. Transform static repositories into dynamic, conversational knowledge bases using state-of-the-art Retrieval Augmented Generation (RAG).

### Features

*   **Dynamic Repository Ingestion**: Seamlessly connect and index any GitHub repository to analyze codebases instantly.
*   **Context-Aware RAG**: Utilize advanced Retrieval Augmented Generation to provide high-precision answers based on actual repository content.
*   **Neural Search Capabilities**: Powered by **Embedchain** and **OpenAI**, ensuring the AI understands the architecture and logic of your projects.
*   **Streamlined Interface**: A minimalist, high-tech UI built for developers who need rapid insights without the overhead.

---

### Setup Guide

Follow these steps to deploy your local instance of the Pixra AI Hub repository analyzer.

#### 1. Clone the Repository
Begin by cloning the official Pixra LLM suite and navigating to the project directory:
```bash
git clone https://github.com/Pixra/llms.git
cd llms/chat_with_github
```

#### 2. Install Dependencies
Install the high-performance requirements needed to power the RAG engine:
```bash
pip install -r requirements.txt
```

#### 3. Configure Credentials
To enable the AI and repository access, you will need two keys:
*   **OpenAI API Key**: Obtain this from your [OpenAI Dashboard](https://platform.openai.com/).
*   **GitHub Access Token**: Generate a [Personal Access Token](https://github.com/settings/tokens) with `repo` permissions to allow the app to read your target repositories.

#### 4. Launch the Application
Start the Streamlit interface to begin chatting with your code:
```bash
streamlit run chat_github.py
```

---

### Engineering Overview
The Pixra AI Hub architecture leverages a **GithubLoader** to ingest source files, which are then processed into a vector database via **Embedchain**. When a query is issued, the system performs a semantic search to retrieve relevant code snippets, passing them as context to the LLM to generate technical, accurate responses.