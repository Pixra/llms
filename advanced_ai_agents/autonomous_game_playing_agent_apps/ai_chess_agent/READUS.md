# 🎮 AI 3D PyGame Visualizer (Powered by DeepSeek R1)

Generate and visualize 3D PyGame code instantly from natural language. This system uses **DeepSeek R1** for deep reasoning, **OpenAI** for clean code extraction, and autonomous browser agents to run the code live on Trinket.io.

### ✨ Key Features
- **Text-to-Game:** Describe a 3D game/visual, and watch it generate.
- **DeepSeek Reasoner:** Handles complex game logic and physics.
- **Auto-Execution:** Browser agents automatically navigate to Trinket.io, paste the code, and run the visualization for you.
- **Clean UI:** Streamlined Streamlit interface for effortless interaction.

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone [https://github.com/Pixra/llms.git](https://github.com/Pixra/llms.git)
cd llms/advanced_ai_agents/autonomous_game_playing_agent_apps/ai_3dpygame_r1
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
You will need API keys from both providers:
- Get [DeepSeek API Key](https://platform.deepseek.com/)
- Get [OpenAI API Key](https://platform.openai.com/)

**4. Run the Visualizer**
```bash
streamlit run ai_3dpygame_r1.py
```
*(The browser agent will automatically open a window and navigate to the execution URL provided in the console).*

---

### 🧠 How it Works (Under the Hood)
1. **Query:** You type what you want to see (e.g., "A rotating 3D cube").
2. **Logic & Code:** DeepSeek analyzes the physics/math, and GPT-4o extracts the pure Python (PyGame) code.
3. **Multi-Agent Automation:** Specialized browser agents take over—navigating to a Python compiler, typing the code, and hitting run.