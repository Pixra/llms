# 🔎 Deep Research Agent

Conduct comprehensive web research and synthesis powered by the OpenAI Agents SDK and Firecrawl. This system delivers in-depth, elaborated reports on complex topics with verifiable sources.

---

### ✨ Key Features
- **Multi-Agent Research Pipeline** ensures comprehensive coverage of the research topic.
- **Contextual Elaboration** on initial findings for added depth and insight.
- **Automated TL;DR Infographics** generated via Gemini for quick comprehension.
- **Exportable Markdown Reports** for easy sharing and archival of research findings.

---

### 🚀 Quick Start

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/single_agent_apps/ai_deep_research_agent
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
Configure your API keys in the sidebar or a `.env` file:
```env
OPENAI_API_KEY=your_openai_key
FIRECRAWL_API_KEY=your_firecrawl_key
```

**4. Run the Research Agent**
```bash
streamlit run deep_research_openai.py
```
