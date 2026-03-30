# 🏠 AI Real Estate Agent Team

Your ultimate AI-powered property search and analysis platform. This application deploys a specialized team of AI agents that use **Firecrawl** to scrape real estate marketplaces (Zillow, Realtor.com, Trulia, Homes.com) and deliver comprehensive market insights, property valuations, and strategic recommendations.

### ✨ The AI Real Estate Team
- 🔎 **Property Search Agent:** Directly integrates with Firecrawl to scrape and extract structured data (price, beds, baths, sqft, links) matching your criteria.
- 📈 **Market Analysis Agent:** Analyzes neighborhood trends, determines if it's a buyer's/seller's market, and highlights investment potential.
- 💰 **Property Valuation Agent:** Assesses if properties are over/under-priced and provides a clear "High/Medium/Low" investment rating.

---

## 🚀 Choose Your Engine (Cloud vs. Local)

This repository includes two versions of the app. You can run it via Cloud APIs (faster) or completely Locally (more private).

### Option A: Cloud Version (Powered by Google Gemini 2.5)
*Best for speed and lightweight local execution.*

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/agent_teams/ai_real_estate_agent_team
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
You'll need these keys to run the cloud version:
- [Google AI API Key](https://aistudio.google.com/app/apikey) (For the LLM brain)
- [Firecrawl API Key](https://firecrawl.dev) (For web scraping)

**4. Run the Cloud App**
```bash
streamlit run real_estate_agent_team.py
```
*(Enter your keys in the sidebar, set your property criteria, select target websites, and hit Search!)*

---

### Option B: Local Version (Powered by Ollama)
*Best for privacy. Requires a machine with at least 16GB RAM.*

**1. Install & Pull Local Model**
Ensure you have Ollama installed, then pull the required model:
```bash
ollama pull gpt-oss:20b
```

**2. Install Dependencies (If not already done)**
```bash
pip install -r requirements.txt
```

**3. Setup API Key**
Even the local version needs Firecrawl to scrape live listings:
- [Firecrawl API Key](https://firecrawl.dev)

**4. Run the Local App**
```bash
streamlit run local_ai_real_estate_agent_team.py
```
*(Ensure Ollama is running in the background before starting the app).*

---

### 📂 File Structure
* `real_estate_agent_team.py` - The Cloud (Gemini) version.
* `local_ai_real_estate_agent_team.py` - The Local (Ollama) version.
* `requirements.txt` - Required python packages.