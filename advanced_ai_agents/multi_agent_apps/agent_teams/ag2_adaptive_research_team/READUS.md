# 🧭 AG2 Adaptive Research Team

A smart, adaptive application that blends AI teamwork, intelligent routing, and fallback mechanisms. Built entirely on the **AG2 framework**, this multi-agent system autonomously decides whether to answer questions from your local documents or search the live web.

### ✨ Key Features
- **Smart Routing:** Automatically decides between analyzing local documents (PDF, TXT, MD) or using web fallback (SearxNG).
- **Multi-Agent Teamwork:** Coordinated handoffs between Triage, Research, Verifier, and Synthesizer agents.
- **Pure AG2 Implementation:** Built AG2-first (`ag2[openai]`) with zero Microsoft AutoGen dependency.
- **Evidence Verification:** Built-in verifier agent checks evidence strength before producing the final cited answer.

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/agent_teams/ag2_adaptive_research_team
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the App**
```bash
streamlit run app.py
```
*(Once the UI opens, enter your OpenAI API key in the sidebar, choose your model, and start asking questions!)*

---

### 🧠 How it Works (The Agent Pipeline)
1. **Triage Agent:** Analyzes the question to route it either to local documents or the web.
2. **Research Agent:** Collects targeted evidence from the chosen source.
3. **Verifier Agent:** Cross-checks the collected evidence for accuracy and strength.
4. **Synthesizer Agent:** Drafts the final, professional response complete with citations.

*Note: The app supports optional AG-UI protocol integration and OpenTelemetry tracing for advanced debugging.*