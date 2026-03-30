# 👨‍⚖️ AI Legal Agent Team

Simulate a full-service law firm right on your local machine! This powerful Streamlit application uses a coordinated team of specialized AI agents to analyze contracts, conduct deep legal research, and provide strategic, actionable recommendations.

### ✨ The AI Legal Team
- 🔍 **Legal Researcher:** Uses DuckDuckGo to find precedents, cite relevant cases, and summarize legal history.
- 📝 **Contract Analyst:** Thoroughly reviews agreements to identify key terms, obligations, and potential loopholes.
- 🎯 **Legal Strategist:** Develops actionable legal strategies by assessing both risks and opportunities.
- 👨‍💼 **Team Lead:** Orchestrates the entire team, ensuring all final reports are comprehensive, accurate, and properly sourced.

### 📑 Built-in Analysis Modes
- **Contract Review** (Handled by Contract Analyst)
- **Legal Research** (Handled by Legal Researcher)
- **Risk Assessment** (Strategist + Analyst)
- **Compliance Check** (Researcher + Analyst + Strategist)

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/agent_teams/ai_legal_agent_team
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
You will need credentials for the LLM brain and the Vector Database. Enter these securely in the app's sidebar:
- [OpenAI API Key](https://platform.openai.com/) (Uses `gpt-4o` and `text-embedding-3-small`)
- [Qdrant API Key & URL](https://cloud.qdrant.io/) (For secure document embeddings)

**4. Run your Virtual Law Firm**
```bash
streamlit run legal_agent_team.py
```
*(Once the UI opens, enter your keys, upload your legal PDFs, choose your analysis type, and let your AI legal team get to work!)*