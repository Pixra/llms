# 🎮 AI Negotiation Battle Simulator

Witness real-time agent-vs-agent showdowns in a high-stakes negotiation arena. This simulator uses Google ADK and AG-UI to stream live battles between buyers and sellers with unique AI personalities.

---

### ✨ Key Features
- **Dual AI Personalities** featuring 8 unique styles from "Shark Steve" to "Analytical Alex."
- **Real-Time AG-UI Protocol** for live streaming of agent actions and tool calls.
- **Interactive Battle Arena** with a live negotiation timeline and generative UI components.
- **Shared State Synchronization** that links backend agent logic with a reactive frontend.

---

### 🚀 Quick Start

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/ai_negotiation_battle_simulator
```

**2. Install Dependencies**
```bash
# Setup Backend
cd backend && pip install -r requirements.txt

# Setup Frontend
cd ../frontend && npm install
```

**3. Setup API Keys**
Configure your Google API key in the `backend/.env` file:
```env
GOOGLE_API_KEY=your_actual_key_here
```

**4. Run the Battle**
```bash
# Start Backend (in one terminal)
cd backend && python agent.py

# Start Frontend (in another terminal)
cd frontend && npm run dev
```
