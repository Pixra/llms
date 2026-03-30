# 🎬 Pixra Multimodal Video Search

Navigate video content with unprecedented precision. Pixra AI Hub’s Multimodal Video Search leverages state-of-the-art vector embeddings to enable instantaneous discovery of visual moments using either natural language or image-to-image matching.

---

### 🚀 The Next Generation of Video Discovery
Traditional search relies on metadata and manual tagging. Pixra transcends these limits by mapping video frames directly into a unified vector space. **Zero transcription. Zero captions. Pure visual intelligence.**

*   **Native Cross-Modal Search**: Bridge the gap between text and imagery using Gemini Embedding 2.
*   **Frame-Level Granularity**: High-precision frame extraction at 1fps via FFmpeg for frame-perfect results.
*   **Visual Similarity Engine**: Drop a screenshot to find exactly where that scene occurs in your library.
*   **Vectorized Persistence**: Powered by ChromaDB for lightning-fast similarity lookups and high-concurrency performance.
*   **Enterprise-Grade Stack**: A seamless integration of FastAPI, Next.js, and Google’s latest generative models.

---

### 🛠 Technical Architecture
The Pixra engine processes video through a sophisticated pipeline:
1.  **Ingestion**: FFmpeg decomposes video into temporal snapshots.
2.  **Intelligence**: Gemini 1.5 Flash generates contextual descriptions.
3.  **Vectorization**: Gemini Embedding 2 creates a multi-dimensional map of every frame.
4.  **Retrieval**: Cosine similarity identifies the highest-ranking moments for instant playback.

---

### ⚡ Quick Start

Follow these steps to deploy the Pixra Multimodal Video Search locally.

#### 1. Clone the Repository
```bash
git clone https://github.com/Pixra/llms.git
cd llms/multimodal_video_moment_finder
```

#### 2. Install Dependencies
**Backend Setup:**
```bash
cd backend
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

**Frontend Setup:**
```bash
cd ../frontend
npm install
```

#### 3. Configure API Keys
Create an environment file in the backend directory and set your Google AI credentials:
```bash
# In backend/
export GOOGLE_API_KEY="your_google_ai_studio_key"

# In frontend/.env.local
NEXT_PUBLIC_API_URL=http://localhost:8890
```

#### 4. Run the Application
**Start Backend:**
```bash
# In backend/
python server.py
```

**Start Frontend:**
```bash
# In frontend/
npm run dev
```
Access the dashboard at `http://localhost:3000`.

---

### 🌐 API Overview

| Method | Endpoint | Function |
| :--- | :--- | :--- |
| `POST` | `/upload-video` | Stream video for automated frame indexing |
| `POST` | `/find-moment` | Execute search via image-to-video similarity |
| `POST` | `/find-moment-text` | Execute search via natural language query |
| `GET` | `/videos` | Retrieve library of indexed content |

---
*Built for the future of media intelligence. Powered by Pixra AI Hub.*