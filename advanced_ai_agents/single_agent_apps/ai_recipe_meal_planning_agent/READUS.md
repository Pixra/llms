# 🍽️ AI Recipe & Meal Planning Agent

Generate balanced weekly meal plans, discover recipes based on ingredients you have, and get nutritional/cost analysis instantly. Your personal culinary assistant, powered by Agno and Spoonacular API.

---

### ✨ Key Features
- **Ingredient-Based Recipe Discovery** with support for all major dietary restrictions (Keto, Vegan, etc.).
- **Automated Nutrition Analysis** providing detailed macro and micro breakdowns per serving.
- **Budget-Conscious Planning** with real-time grocery cost estimation for entire meal plans.
- **Shopping List Optimization** to streamline your grocery trips based on planned meals.

---

### 🚀 Quick Start

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/single_agent_apps/ai_recipe_meal_planning_agent
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
Configure your API keys in a `.env` file:
```env
OPENAI_API_KEY=your_openai_key
SPOONACULAR_API_KEY=your_spoonacular_key
```

**4. Run the Meal Planner**
```bash
streamlit run ai_recipe_meal_planning_agent.py
```
