# 🗞️ AI Journalist Agent

Instantly generate high-quality, professional articles on any subject by automating web research and content refinement. This agent leverages GPT-4o and SerpAPI to maintain journalistic standards.

---

### ✨ Key Features
- **Automated Research & Source Gathering** using SerpAPI for timely, relevant information.
- **High-Fidelity Article Drafting** focused on clarity, structure, and engaging narrative.
- **AI Editing Pass** to refine tone and ensure adherence to professional publishing standards.
- **Streamlit Interface** for easy topic input and viewing of final published-ready content.

---

### 🚀 Quick Start

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/single_agent_apps/ai_journalist_agent
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
Configure your API keys in a `.env` file:
```env
OPENAI_API_KEY=your_openai_key
SERPAPI_API_KEY=your_serpapi_key
```

**4. Run the Journalist Agent**
```bash
streamlit run journalist_agent.py
```
