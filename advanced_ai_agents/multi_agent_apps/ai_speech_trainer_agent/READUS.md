# 🎤 AI Speech Trainer Agent

Master the art of public speaking with a multi-agent coach that analyzes your facial expressions, vocal delivery, and content clarity. Receive personalized, data-driven feedback to build confidence and deliver impactful presentations.

---

### ✨ Key Features
- **Multimodal Analysis** of video, audio, and text for comprehensive speaking evaluation.
- **Facial Expression Tracking** to monitor engagement, emotion, and eye contact.
- **Vocal Performance Metrics** covering pace, pitch, clarity, and filler word detection.
- **Automated Content Scoring** based on professional rubrics for structure and tone.

---

### 🚀 Quick Start

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/ai_speech_trainer_agent
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
Create a `.env` file in the project root:
```env
TOGETHER_API_KEY=your_actual_key_here
```

**4. Run the Trainer**
```bash
# Start the backend
cd backend && uvicorn main:app --reload

# In a new terminal, start the frontend
cd frontend && streamlit run Home.py
```
