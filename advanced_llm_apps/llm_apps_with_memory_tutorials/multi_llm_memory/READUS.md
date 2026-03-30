# 🧠 Pixra AI Hub

Experience the next evolution of multi-model orchestration. Pixra AI Hub is a high-performance interface that bridges the gap between different language models through a sophisticated shared memory layer, ensuring your AI interactions are always contextually aware and persistent.

### Features

*   **Multi-Model Ecosystem**: Seamlessly toggle between industry-leading models, including **OpenAI’s GPT-4o** and **Anthropic’s Claude 3.5 Sonnet**, within a single unified interface.
*   **Neural Memory Layer**: Powered by **Qdrant Vector Store**, the system maintains a persistent cognitive memory, allowing the AI to recall past interactions across different sessions.
*   **Dynamic Context Retrieval**: Automatically fetches relevant historical data to provide high-fidelity, personalized responses based on user-specific history.
*   **Enterprise-Grade UI**: A clean, minimalist Streamlit architecture designed for speed, clarity, and professional AI workflows.

---

### Setup Guide

Follow these steps to deploy your local instance of Pixra AI Hub.

#### 1. Clone the Repository
Begin by cloning the official Pixra repository to your local environment:
```bash
git clone https://github.com/Pixra/llms.git
cd llms
```

#### 2. Install Dependencies
Initialize your environment by installing the required high-performance libraries:
```bash
pip install -r requirements.txt
```

#### 3. Configure Infrastructure & Keys
Pixra AI Hub utilizes Qdrant for its memory layer. Ensure you have Docker running, then pull and start the Qdrant engine:
```bash
# Start the vector database
docker pull qdrant/qdrant
docker run -p 6333:6333 qdrant/qdrant
```
*Note: Ensure your `.env` file or environment variables are configured with your OpenAI and Anthropic API keys.*

#### 4. Launch the Application
Start the engine and begin interacting with your persistent AI ecosystem:
```bash
streamlit run multi_llm_memory.py
```