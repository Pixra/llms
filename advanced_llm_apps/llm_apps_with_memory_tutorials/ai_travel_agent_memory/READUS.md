# ✈️ Smart Travel Concierge

Experience the future of personalized journey planning with the **Pixra AI Hub** Travel Agent. This isn't just a chatbot; it's a sophisticated digital consultant that evolves with you. By integrating long-term cognitive memory, the agent remembers your unique preferences, past destinations, and specific travel requirements to provide a truly bespoke experience.

### Features
*   **Persistent Cognitive Memory:** Leverages **Mem0 and Qdrant** to retain user preferences and context across multiple sessions.
*   **Advanced GPT-4o Intelligence:** Powered by OpenAI’s flagship model for human-like reasoning and hyper-accurate itinerary generation.
*   **Vectorized Data Retrieval:** Utilizes high-performance vector storage for lightning-fast memory recall and contextual awareness.
*   **Seamless Interface:** A minimalist, premium Streamlit UI designed for intuitive interaction and real-time memory monitoring.

---

### Setup Guide

#### 1. Clone the Repository
Begin by pulling the Pixra AI Hub architecture to your local environment:
```bash
git clone https://github.com/Pixra/llms.git
cd llms
```

#### 2. Install Dependencies
Initialize your environment by installing the high-performance requirements:
```bash
pip install -r requirements.txt
```

#### 3. Configure API Keys & Infrastructure
Set your OpenAI API key in your environment variables and launch the **Qdrant** vector engine via Docker:

```bash
# Set your API Key
export OPENAI_API_KEY='your_api_key_here'

# Pull and run Qdrant Vector Database
docker pull qdrant/qdrant
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```

#### 4. Launch the AI Hub
Deploy the application locally using the Streamlit engine:
```bash
streamlit run travel_agent_memory.py
```