# 📊 AI VC Due Diligence Agent Team

Automate your startup investment analysis like a top-tier Venture Capitalist. Built with **Google ADK** and **Gemini 3**, this 7-stage multi-agent pipeline researches any startup (via name or URL) and generates professional, McKinsey-style HTML investment reports, financial projections, and visual infographics.

### ✨ Key Features
- **Deep Research & Risk Analysis:** Real-time web search for market size, competitors, and comprehensive risk assessments (Execution, Financial, Regulatory).
- **Financial Projections:** Automatically generates Bear/Base/Bull revenue projection charts.
- **Professional Artifacts:** Outputs a highly structured Investor Memo, a beautiful HTML report, and a visual TL;DR infographic.

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/agent_teams/ai_vc_due_diligence_agent_team
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

**4. Generate a Due Diligence Report**
*(Open `http://localhost:8000` in your browser and try a prompt like: "Analyze [https://agno.com](https://agno.com) for Series A investment of $30-50M")*

---

### 🧠 The 7-Stage AI Pipeline
1. **Company Research Agent**
2. **Market Analysis Agent**
3. **Financial Modeling Agent** (Generates Revenue Charts)
4. **Risk Assessment Agent**
5. **Investor Memo Agent**
6. **Report Generator Agent** (Generates HTML Report)
7. **Infographic Generator Agent** (Generates Visual Summary)