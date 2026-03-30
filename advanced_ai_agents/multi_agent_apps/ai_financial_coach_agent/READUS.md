# 💰 AI Financial Coach Agent (with Google ADK)

Take control of your personal finances with a specialized AI coaching team. Built with **Google ADK** and **Gemini**, this application analyzes your spending patterns, creates personalized savings plans, and develops optimized debt-payoff strategies (Avalanche/Snowball) to help you reach your financial goals faster.

### ✨ The Financial Coaching Team
- 📊 **Budget Analysis Agent:** Scrutinizes your spending habits and identifies areas for instant optimization.
- 🏦 **Savings Strategy Agent:** Crafts personalized emergency fund plans and long-term savings milestones.
- 📉 **Debt Reduction Agent:** Optimizes your debt payoff using mathematical models to minimize interest payments.

### 🛠️ Key Capabilities
- **Smart Expense Tracking:** Upload a CSV or enter expenses manually for automated categorization.
- **Visual Analytics:** Interactive pie charts and bar graphs for income vs. expense breakdowns.
- **Strategy Comparison:** Compare different debt-repayment methods to see exactly how much interest you'll save.

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/ai_financial_coach_agent
```

**2. Setup API Key**
Get a free Gemini API Key from [Google AI Studio](https://aistudio.google.com/apikey). Create a `.env` file in the folder:
```env
GOOGLE_API_KEY=your_actual_key_here
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the Financial Coach**
```bash
streamlit run ai_financial_coach_agent.py
```
*(Once the UI opens, upload your transactions or enter your budget manually to receive your personalized financial roadmap!)*

---

### 📂 CSV Data Format
If you want to upload your bank statements, ensure your CSV has these columns:
- **Date:** (YYYY-MM-DD)
- **Category:** (e.g., Housing, Food, Transport)
- **Amount:** (Transaction value)

*Note: You can download a sample template directly from the app's sidebar.*