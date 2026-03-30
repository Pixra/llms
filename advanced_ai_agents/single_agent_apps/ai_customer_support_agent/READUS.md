# 🛒 AI Customer Support Agent with Memory

Deliver personalized customer service with an AI agent that remembers past interactions and user profiles. Built with Mem0 and Qdrant, this support system provides intelligent, context-aware responses to every query.

---

### ✨ Key Features
- **Persistent Interaction Memory** using Mem0 to track customer history and preferences.
- **Vector-Based Profile Storage** with Qdrant for fast, semantic context retrieval.
- **Intelligent GPT-4o Responses** that adapt to individual customer needs and tone.
- **Synthetic Data Generation** tools for testing and demonstrating agent performance.

---

### 🚀 Quick Start

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/single_agent_apps/ai_customer_support_agent
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup Infrastructure**
Ensure Qdrant is running on localhost:6333:
```bash
docker run -p 6333:6333 qdrant/qdrant
```

**4. Run the Support Agent**
```bash
export OPENAI_API_KEY=your_actual_key_here
streamlit run customer_support_agent.py
```
