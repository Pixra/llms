# 👨🏻‍💼 AI Sales Intelligence Agent Team

Empower your sales team with an automated competitive intelligence pipeline. Built with **Google ADK** and **Gemini 3**, this multi-agent system researches competitors in real-time and generates battle-ready sales assets, including objection-handling scripts, SWOT analyses, HTML battle cards, and visual comparison infographics.

### ✨ Key Features
- **Live Competitor Research:** Deep-dives into features, pricing, and market positioning via web search.
- **7-Stage AI Pipeline:** Sequentially processes data from raw research to final visual assets.
- **Battle-Ready Assets:** Generates a professional HTML Battle Card and a visual Comparison Chart (via Gemini Image generation).
- **Objection Handling:** Provides instant, scripted responses and trap-setting questions for sales calls.

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/agent_teams/ai_sales_intelligence_agent_team
```

**2. Setup API Key**
You will need a Google Gemini API key to power the ADK models. Export it in your terminal:
```bash
export GOOGLE_API_KEY=your_google_api_key
```

**3. Install & Run**
```bash
pip install -r requirements.txt
adk web
```

**4. Generate Your First Battle Card**
*(Open `http://localhost:8000` in your browser and try a prompt like: "Create a battle card for Salesforce. We sell HubSpot.")*

---

### 🧠 How it Works (The 7-Stage Pipeline)
This application uses a `SequentialAgent` architecture to pass data through 7 specialized experts:
1. **Competitor Research Agent** (Gathers web intelligence)
2. **Product Feature Agent** (Analyzes capabilities)
3. **Positioning Analyzer** (Uncovers messaging strategy)
4. **SWOT Analysis Agent** (Identifies strengths & weaknesses)
5. **Objection Handler** (Creates sales scripts)
6. **Battle Card Generator** (Exports professional HTML)
7. **Comparison Chart Agent** (Generates a visual infographic)