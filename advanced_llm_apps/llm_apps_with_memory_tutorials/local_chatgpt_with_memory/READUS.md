# 🧠 Pixra AI Hub: Local Intelligence Layer

Experience the next generation of private, persistent AI. Pixra AI Hub provides a sovereign ChatGPT-like ecosystem, powered by Llama 3.1, designed to run entirely on your local infrastructure. No cloud dependencies, no data leaks—just pure, high-performance intelligence.

### Features
- **Llama 3.1 Core**: Harness the power of state-of-the-art inference via Ollama.
- **Persistent Memory**: Advanced **long-term context storage** tailored to individual user profiles.
- **Vectorized Search**: High-velocity retrieval-augmented generation (RAG) powered by **Qdrant**.
- **Privacy-First Embeddings**: Localized vector processing using **Nomic Embed**.
- **Zero-API Dependency**: Complete operational autonomy with no external subscription costs.

---

### 🚀 Getting Started

Follow these steps to deploy Pixra AI Hub on your local machine.

#### 1. Clone the Repository
Initialize your local environment by cloning the official Pixra repository.
```bash
git clone https://github.com/Pixra/llms.git
cd llms
```

#### 2. Install Dependencies
Ensure your environment is optimized with the necessary libraries and frameworks.
```bash
pip install -r requirements.txt
```

#### 3. Infrastructure & Model Pull
Deploy the local vector database and initialize the Llama 3.1 intelligence engine.
```bash
# Start Qdrant Vector DB via Docker
docker run -p 6333:6333 qdrant/qdrant

# Pull the Llama 3.1 model
ollama pull llama3.1
```

#### 4. Run the Application
Launch the high-tech Streamlit interface to begin your private AI session.
```bash
streamlit run app.py
```