# 💼 AI Recruitment Agent Team

Automate your hiring pipeline with a full-service AI recruitment team. Powered by the **Agno framework** and **OpenAI (GPT-4o)**, this system orchestrates specialized agents to screen resumes, evaluate technical skills, schedule Zoom interviews, and handle candidate email communications autonomously.

### ✨ The AI Recruitment Team
- 📄 **Technical Recruiter Agent:** Analyzes uploaded resumes, matches skills to job descriptions, verifies experience, and makes initial selection decisions.
- ✉️ **Communication Agent:** Drafts and sends professional emails, candidate feedback, and automated notifications.
- 📅 **Scheduling Coordinator Agent:** Automatically generates Zoom meeting links, handles calendar logistics, and manages timezones.

---

### 🔑 Important Prerequisites

Before running the app, you need to set up two external services for your AI agents to use:

1. **Recruiter Email (Gmail):** - Use a dedicated Gmail account. Enable 2-Step Verification and generate an [App Password](https://support.google.com/accounts/answer/185833?hl=en). Keep this 16-digit code handy (use it without spaces).
2. **Zoom API Credentials:** - Go to the [Zoom Marketplace](https://marketplace.zoom.us).
   - Create a **"Server-to-Server OAuth"** app to get your `Client ID`, `Client Secret`, and `Account ID`.
   - Add scopes: `meeting:write:invite_links:admin`, `meeting:write:meeting:admin`, `user:read:email:admin` (and related meeting write permissions).

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/agent_teams/ai_recruitment_agent_team
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Run your Virtual Recruitment Agency**
```bash
streamlit run ai_recruitment_agent_team.py
```

**4. Setup API Keys in the App**
Once the UI opens, enter your credentials in the sidebar:
- OpenAI API Key
- Zoom API credentials (Account ID, Client ID, Client Secret)
- Gmail App Password

---
*⚠️ **Disclaimer:** This tool is an AI assistant designed to streamline the hiring process. All automated screening decisions should be reviewed by human recruiters for final approval.*