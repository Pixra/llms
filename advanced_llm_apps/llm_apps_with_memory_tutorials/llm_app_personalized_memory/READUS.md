# 🧠 Pixra AI Hub: Persistent Context Engine

Elevate your AI interactions with **Pixra AI Hub**, a sophisticated interface designed for hyper-personalized digital conversations. By integrating state-of-the-art reasoning with long-term neural memory, Pixra ensures your AI doesn't just respond—it remembers, learns, and evolves with every interaction.

### 💎 Key Features

*   **Next-Gen Reasoning**: Harnesses the full power of **GPT-4o** for high-precision, human-like responses.
*   **Neural Memory**: Implements a robust persistent memory layer using **Mem0** and **Qdrant Vector Store** for long-term context retention.
*   **Contextual Continuity**: Seamlessly track and manage conversation history through an intuitive, high-tech interface.
*   **Sleek Architecture**: Built on a reactive **Streamlit** framework, providing a professional and responsive user experience.

---

### 🚀 Quick Start Guide

Deploy your personalized AI instance in four streamlined steps.

#### 1. Clone the Repository
Initialize your local environment by fetching the core architecture.
```bash
git clone https://github.com/Pixra/llms.git
cd llms
```

#### 2. Install Dependencies
Install the enterprise-grade library stack required to power the engine.
```bash
pip install -r requirements.txt
```

#### 3. Infrastructure & Keys
Ensure your vector database is active and your environment variables (OpenAI API Key) are configured. Pixra utilizes Qdrant for high-performance memory retrieval.

**Start Qdrant via Docker:**
```bash
docker pull qdrant/qdrant

docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```

#### 4. Launch the Hub
Orchestrate the application and begin your first persistent session.
```bash
streamlit run llm_app_memory.py
```