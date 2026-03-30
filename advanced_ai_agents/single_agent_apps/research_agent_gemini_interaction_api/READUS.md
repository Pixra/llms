# 🔬 AI Research Planner & Executor Agent

Execute complex research goals with a multi-phase agent built on Google's Interactions API. Automate everything from research planning and task selection to executive reporting and infographic generation.

---

### ✨ Key Features
- **Structured Research Planning** using Gemini 3 Flash to create actionable task lists.
- **Deep Research Execution** leveraging specialized agents with built-in web search capabilities.
- **Stateful Conversational Context** that maintains information across multiple research phases.
- **Automated Infographic Generation** using Gemini 3 Pro Image for visual TL;DR summaries.

---

### 🚀 Quick Start

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/single_agent_apps/research_agent_gemini_interaction_api
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
Provide your Google API key in the sidebar or set it in a `.env` file:
```env
GOOGLE_API_KEY=your_actual_key_here
```

**4. Run the Research Planner**
```bash
streamlit run research_planner_executor_agent.py
```
*(Once the UI opens, enter your research goal to receive a structured plan and infographic summary!)*
