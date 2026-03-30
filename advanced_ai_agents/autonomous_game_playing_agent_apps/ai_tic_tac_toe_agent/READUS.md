# 🎮 AI Tic-Tac-Toe: Agent vs Agent Battle

Watch AI models battle it out! This interactive Tic-Tac-Toe game pits two AI agents against each other, powered by different LLMs (GPT-4, Claude, Gemini, etc.). Built with the **Agno Agent Framework** and **Streamlit**.

### ✨ Key Features
- **Multi-Model Support:** Mix and match OpenAI, Anthropic, Google, and Groq models to see who wins.
- **3-Agent System:** One Master Agent (Referee) orchestrates the game between Two Player Agents.
- **Real-Time UI:** Live board visualization, move history, and strategy tracking.

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/autonomous_game_playing_agent_apps/ai_tic_tac_toe_agent
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
Create a `.env` file in the folder and add your desired keys:
```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key  # Optional (For Claude)
GOOGLE_API_KEY=your_google_key        # Optional (For Gemini)
GROQ_API_KEY=your_groq_key            # Optional (For Llama 3)
```

**4. Run the Game**
```bash
streamlit run app.py
```
*(Open the localhost link in your browser, select your AI players, and start the match!)*