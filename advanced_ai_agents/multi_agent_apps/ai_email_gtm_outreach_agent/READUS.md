# 📧 AI Email GTM Outreach Agent

Automate your entire B2B sales pipeline from discovery to draft. Powered by **GPT-5** and **Exa**, this multi-agent system discovers relevant companies, finds the right decision-makers, researches deep insights from Reddit/Web, and writes highly personalized outreach emails in your chosen style.

### ✨ The Sales Outreach Team
- 🔍 **Company Finder:** Uses Exa to discover companies matching your specific targeting and offering.
- 👤 **Contact Finder:** Identifies key decision-makers (Founders, GTM/Sales Leads) and their emails.
- 🧠 **Deep Researcher:** Pulls 2–4 unique insights from the company's website and Reddit for genuine personalization.
- ✍️ **Email Writer:** Crafts concise, tailored outreach emails based on the gathered research.

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/ai_email_gtm_outreach_agent
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
You will need these keys to power the discovery and the reasoning. Enter them in the app's sidebar:
- [OpenAI API Key](https://platform.openai.com/) (Uses `gpt-5` or your preferred model)
- [Exa API Key](https://dashboard.exa.ai/) (For deep web discovery)

**4. Run the Outreach Agent**
```bash
streamlit run ai_email_gtm_outreach_agent.py
```
*(Once the UI opens, enter your keys, describe your target audience and your product offering, and watch the agents build your outreach list!)*

---

### 💡 Pro-Tips for Success
- **Personalize your Style:** Choose between Professional, Casual, Cold, or Consultative styles to match your brand voice.
- **Scale Smartly:** Start with 3–5 companies to test the research quality before scaling to 10.
- **Reddit Insights:** Use the research findings to mention specific pain points or discussions found on Reddit for a 10x higher response rate.