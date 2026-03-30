# 🔍 AI Domain Deep Research Agent

Conduct high-level, professional research on any topic automatically. Powered by **Together AI (Qwen)**, **Agno**, and **Composio**, this agent generates targeted research questions, scours the web via Tavily and Perplexity, and compiles its findings into a structured report directly in your Google Docs.

### ✨ Key Features
- 🧠 **Intelligent Logic:** Automatically generates 5 domain-specific research questions to guide the investigation.
- 🔎 **Deep Search Integration:** Combines **Tavily** (for web results) and **Perplexity AI** (for deep analysis) to ensure no stone is left unturned.
- 📊 **McKinsey-Style Reports:** Synthesizes raw data into a professional report with an executive summary, deep analysis, and conclusions.
- 📝 **Google Docs Export:** Uses Composio to create and save the final report directly to your Google Drive.

---

### 🔑 Crucial Pre-requisites (Setup)

This agent needs to talk to Google Docs and Perplexity. Follow these steps:
1. Get a [Together AI API Key](https://together.ai) (for the Qwen model).
2. Get a [Composio API Key](https://composio.ai).
3. **Link your tools in the terminal:**
   ```bash
   pip install composio_agno
   composio add googledocs
   composio add perplexityai
   ```
   *(Follow the browser prompts to authenticate your Google and Perplexity accounts).*

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/single_agent_apps/ai_domain_deep_research_agent
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Research Agent**
```bash
streamlit run ai_domain_deep_research_agent.py
```
*(Once the UI opens, enter your keys in the sidebar, input your research topic/domain, and watch the agent generate questions, research, and compile your report!)*

---

### 📂 Technical Stack
* **LLM:** Together AI (Qwen 3 235B)
* **Orchestration:** Agno Agent Framework
* **Tools:** Composio (Google Docs & Perplexity), Tavily Search
* **UI:** Streamlit