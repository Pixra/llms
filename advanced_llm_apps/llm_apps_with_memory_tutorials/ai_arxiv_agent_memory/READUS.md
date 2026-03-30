# 🧠 Intelligent Research Agent

Elevate your scholarly workflow with a research companion that learns. **Pixra AI Hub** delivers a high-performance interface for academic discovery, integrating advanced language models with long-term memory to transform how you search, synthesize, and store knowledge from arXiv.

### ⚡ Features

*   **Deep Academic Discovery:** Seamlessly query the **arXiv database** with natural language to find relevant papers instantly.
*   **Persistent Context:** Leverages **Mem0 and Qdrant** to create a "Research Brain" that remembers your interests and past interactions across sessions.
*   **Intelligent Synthesis:** Powered by **GPT-4o-mini** to process complex abstracts and technical data into readable, actionable insights.
*   **Autonomous Browsing:** Integrated with **MultiOn** for dynamic web-enabled research and enhanced information retrieval.
*   **Vectorized Memory:** Utilizes a high-performance vector database for lightning-fast retrieval of user preferences and historical context.

---

### 🚀 Getting Started

Follow these steps to deploy your local instance of the Pixra AI Hub Research Agent.

#### 1. Clone the Repository
Begin by cloning the official repository and navigating to the project directory:
```bash
git clone https://github.com/Pixra/llms.git
cd llms/ai_arxiv_agent_memory
```

#### 2. Install Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

#### 3. Configure Infrastructure & Keys
Ensure your API keys (OpenAI, MultiOn, Mem0) are configured in your environment. Additionally, launch the **Qdrant** vector engine via Docker:
```bash
docker pull qdrant/qdrant

docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```

#### 4. Run the Application
Launch the premium Streamlit interface:
```bash
streamlit run ai_arxiv_agent_memory.py
```