# 📰 Multi-Agent AI Researcher

Research top stories and users on HackerNews using a coordinated team of AI assistants. Generate professional blog posts, reports, and social media content based on deep-dive technical research.

---

### ✨ Key Features
- **HackerNews Researcher** specialized in fetching top stories and trending discussions.
- **Web Searcher** to gather additional context and information using DuckDuckGo.
- **Article Reader** for extracting detailed content and insights from external URLs.
- **Coordinated Research Workflow** that synthesizes findings into engaging summaries and articles.

---

### 🚀 Quick Start

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/multi_agent_researcher
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
Provide your OpenAI API key in the app sidebar or set it in a `.env` file:
```env
OPENAI_API_KEY=your_actual_key_here
```

**4. Run the Researcher**
```bash
streamlit run research_agent.py
```
*(Once the UI opens, enter your query to begin the automated research process!)*
