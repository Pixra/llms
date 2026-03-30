# 🔍 AI Fraud Investigation Agent

Detect anomalies in childcare provider licensing by cross-referencing public records against physical building data. This autonomous agent uses mathematical modeling and visual analysis to find discrepancies in official paperwork.

---

### ✨ Key Features
- **Public Data Cross-Referencing** of DCFS licensing, Cook County property records, and Google Maps.
- **Capacity Calculation Engine** that applies building codes to verify maximum legal occupancy.
- **Visual Verification** using Google Street View to analyze facility appearance and status.
- **Real-Time Reasoning Narrative** showing the agent's investigative process as it works.

---

### 🚀 Quick Start

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/single_agent_apps/ai_fraud_investigation_agent
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
Configure your API keys in the sidebar or a `.env` file:
```env
OPENROUTER_API_KEY=your_openrouter_key
GOOGLE_MAPS_API_KEY=your_google_maps_key # Optional
```

**4. Run the Investigation**
```bash
streamlit run fraud_investigation_agent.py
```
*(Note: This demo is specifically optimized for Cook County, Illinois neighborhoods.)*
