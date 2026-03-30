# 🔍 AI SEO Audit Team

Automate your technical and content SEO audits. Built with **Google ADK**, **Gemini 2.5 Flash**, and **Firecrawl (via MCP)**, this multi-agent workflow crawls any live webpage, researches real-time SERP competition, and generates a polished, prioritized SEO optimization roadmap.

### ✨ Key Features
- **End-to-End On-Page Audit:** Scrapes public URLs to evaluate titles, headings, content depth, and internal/external links.
- **Competitive SERP Intelligence:** Analyzes top competitors, content formats, and "People Also Ask" questions for your target keywords.
- **Actionable Roadmaps:** Delivers a clean Markdown report with prioritized recommendations, expected impact, and schema opportunities.

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/agent_teams/ai_seo_audit_team
```

**2. Install Dependencies**
*Note: You must have Python 3.10+ and Node.js installed.*
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
Export your keys in the terminal (or add them to a `.env` file):
```bash
export GOOGLE_API_KEY=your_gemini_key
export FIRECRAWL_API_KEY=your_firecrawl_key
```

**4. Run the ADK Web UI**
```bash
adk web
```
*(Open the local UI, select the `ai_seo_audit_team` app, enter your target URL, and watch the agents execute in the Trace panel!)*

---

### 🧠 How it Works (The Agent Pipeline)
This system uses ADK's `SequentialAgent` to pass data through three specialized stages:
1. **Page Auditor Agent:** Scrapes the page structure and infers target keywords.
2. **Serp Analyst Agent:** Extracts patterns, opportunities, and differentiation angles from Google Search.
3. **Optimization Advisor Agent:** Synthesizes everything into a clear, actionable Markdown report.