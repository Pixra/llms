# 🌍 AQI Analysis Agent (Health & Environment)

Take control of your health with real-time air quality monitoring. Powered by **Firecrawl** and the **Agno AI framework**, this agent fetches live pollution data and provides personalized health recommendations based on your specific medical conditions and planned outdoor activities.

### ✨ Key Features
- **Dual-Agent System:**
  - *AQI Analyzer:* Scrapes and processes real-time metrics (PM2.5, PM10, CO, Wind Speed).
  - *Health Advisor:* Generates custom health tips based on your location and medical profile.
- **Comprehensive Metrics:** Tracks AQI, Humidity, Temperature, and provides activity safety scores.
- **Smart Recommendations:** Suggests the best time for outdoor activities and correlates weather conditions with air quality.

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/single_agent_apps/ai_aqi_analysis_agent
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
You will need two keys to power the logic and the data scraping. You can enter these in the app's configuration section:
- [OpenAI API Key](https://platform.openai.com/api-keys) (For the LLM brain)
- [Firecrawl API Key](https://www.firecrawl.dev/app/api-keys) (For real-time air quality scraping)

**4. Run the App (Gradio UI)**
```bash
python ai_aqi_analysis_agent.py
```
*(Once it runs, open `http://127.0.0.1:7860` in your browser. Enter your city, any medical conditions, and get your instant AQI report!)*

---
*💡 **Usage Tip:** For the best results, include your specific planned activity (e.g., "Cycling", "Morning Walk") to get tailored safety advice.*