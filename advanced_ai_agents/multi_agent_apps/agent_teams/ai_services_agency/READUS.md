# 👨‍💼 AI Services Agency

Launch your own virtual digital agency! This application simulates a full-service software agency using a team of specialized AI agents. From strategic planning and product-market fit to technical architecture and go-to-market strategy, this AI team analyzes and plans your entire software project autonomously.

### ✨ The Agency Team
- 👑 **CEO Agent:** Drives strategic oversight, evaluates startup ideas, and makes final executive decisions.
- 🏗️ **CTO Agent:** Evaluates technical feasibility and dictates the core system architecture.
- 📦 **Product Manager Agent:** Defines the product strategy, roadmap, and coordinates between tech and marketing.
- 💻 **Developer Agent:** Provides detailed technical implementation guidance, tech stack selection, and cost estimations.
- 🤝 **Client Success Agent:** Develops the go-to-market (GTM) strategy and customer acquisition plans.

### 🛠️ Custom Tools & Collaboration
The agency uses structured tools (`AnalyzeProjectRequirements`, `CreateTechnicalSpecification`) to ensure rigorous, data-driven outputs. Agents collaborate seamlessly (e.g., CTO ↔️ Developer for tech specs, PM ↔️ Client Success for marketing) to deliver a cohesive project plan.

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/agent_teams/ai_services_agency
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
You will need an [OpenAI API Key](https://platform.openai.com/api-keys). You can securely enter this directly inside the app's sidebar.

**4. Run Your Virtual Agency**
```bash
streamlit run agency.py
```
*(Open the UI, enter your API key, describe your startup idea, and watch your agency team build your complete business plan!)*