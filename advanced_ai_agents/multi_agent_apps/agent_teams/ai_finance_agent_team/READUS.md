# 💲 AI Finance Agent Team (with Web Access)

Build a complete AI Financial Analyst team in just 20 lines of Python code! Powered by GPT-4o, this multi-agent system combines real-time web search with deep financial data analysis to provide comprehensive market insights.

### ✨ Key Features
- **Multi-Agent System:** - *Web Agent:* Handles general internet research (via DuckDuckGo).
  - *Finance Agent:* Dives deep into financial data and stock metrics (via YFinance).
  - *Team Leader:* Coordinates both agents to deliver a unified, highly accurate response.
- **Real-Time Data:** Access live stock prices, company fundamentals, and financial news.
- **Persistent Memory:** Uses SQLite to store and remember agent interactions.

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/agent_teams/ai_finance_agent_team
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
Get your [OpenAI API Key](https://platform.openai.com/) and export it in your terminal:
```bash
export OPENAI_API_KEY='your-api-key-here'
```
*(Windows users: use `set OPENAI_API_KEY='your-api-key-here'`)*

**4. Run the Agent Team**
```bash
python3 finance_agent_team.py
```
*(Once it runs, open your web browser and navigate to the Playground URL provided in the console to interact with your AI Finance Team!)*