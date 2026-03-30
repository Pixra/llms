# 💻 Multimodal AI Coding Agent Team (o3-mini & Gemini)

Your ultimate AI pair programmer and problem solver. Upload a screenshot of a coding problem or type it out—this multi-agent system will analyze the logic, write the optimal code with best time/space complexity, and securely execute it in a live sandbox environment.

### ✨ The AI Engineering Team
- 👁️ **Vision Agent (Gemini-2.0-flash):** Extracts and understands coding problems directly from uploaded images.
- 🧠 **Coding Agent (OpenAI o3-mini):** Generates clean, well-documented Python solutions with proper type hints and edge-case handling.
- ⚡ **Execution Agent (OpenAI + E2B Sandbox):** Securely runs the code, provides real-time results, and explains any errors.

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_coding_agent_team
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
You will need three keys for full multimodal functionality. You can enter these securely in the app's sidebar:
- [OpenAI API Key](https://platform.openai.com/) (For coding & execution logic)
- [Google Gemini API Key](https://aistudio.google.com/app/apikey) (For image processing)
- [E2B API Key](https://e2b.dev/docs/getting-started/api-key) (For the secure code execution sandbox)

**4. Run your AI Programmer**
```bash
streamlit run ai_coding_agent_o3.py
```
*(Once the UI opens, enter your keys, upload your coding challenge screenshot, and hit "Generate & Execute Solution"!)*