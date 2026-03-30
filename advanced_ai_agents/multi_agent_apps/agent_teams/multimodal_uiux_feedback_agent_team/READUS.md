# 🎨 🍌 Multimodal UI/UX Feedback Agent Team (Nano Banana)

A sophisticated multi-agent system built with **Google ADK**. It doesn't just critique your landing pages—it automatically generates improved versions! Using Gemini's advanced multimodal capabilities, this team acts as your elite design reviewer and visual implementer.

### ✨ The AI Design Team
1. **👁️ UI Critic Agent:** Uses native vision to analyze layout, hierarchy, and CTA effectiveness, providing a comprehensive WCAG-compliant audit.
2. **📐 Design Strategist Agent:** Creates a prioritized improvement plan, specifying exact hex codes, typography, and spacing adjustments.
3. **🚀 Visual Implementer Agent:** Generates an improved, high-quality landing page design based on the feedback and maintains version history.

---

### 🚀 How to Get Started

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_uiux_feedback_agent_team
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Key**
Export your Gemini API key in the terminal:
```bash
export GOOGLE_API_KEY="your_gemini_api_key"
```

**4. Launch the ADK Web Interface**
```bash
cd advanced_ai_agents/multi_agent_apps/agent_teams
adk web
```
*(Open your browser, select the `multimodal_uiux_feedback_agent_team`, upload your landing page screenshot, and watch the AI team audit and redesign it!)*

---

### 🧠 Multi-Agent Architecture
This app uses a **Coordinator/Dispatcher pattern**:
* **Coordinator (Root Agent)** routes your requests.
* **Info Agent** handles general Q&A.
* **Design Editor** handles iterative refinements based on your feedback.
* **Analysis Pipeline** sequentially runs the UI Critic ➡️ Design Strategist ➡️ Visual Implementer.

### 💡 Best Practices
- Use full-page, high-resolution screenshots (1920x1080 minimum).
- Be specific with refinements (e.g., "Make the CTA button 20% larger with a vibrant orange color").
- Use it for A/B testing ideas, pre-launch reviews, and conversion optimization.