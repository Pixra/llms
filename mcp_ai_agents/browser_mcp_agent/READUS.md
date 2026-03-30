# 🌐 Pixra AI Hub: Autonomous Web Intelligence

Experience the next generation of web interaction. **Pixra AI Hub** transforms natural language into precise browser actions, leveraging the Model Context Protocol (MCP) and Playwright to bridge the gap between LLM reasoning and the live web. Engineered for speed, accuracy, and seamless automation.

---

### ✨ Core Features

*   **Autonomous Navigation**: Effortlessly traverse complex web structures and subdirectories using simple English commands.
*   **Dynamic Interaction**: Real-time execution of clicks, form entries, and scrolling across sophisticated web applications.
*   **Visual Intelligence**: High-fidelity screenshot capture and visual element tracking for enhanced contextual awareness.
*   **Precision Extraction**: Instantly transform unstructured web content into clean, actionable data summaries.
*   **Multi-Step Reasoning**: Execute intricate workflows—from navigating login portals to performing deep-dive research—in a single session.

---

### 🚀 Quick Start Guide

Deploy your autonomous agent in minutes by following these steps:

#### 1. Clone the Repository
Initialize the Pixra AI environment on your local machine:
```bash
git clone https://github.com/Pixra/llms.git
cd mcp_ai_agents/browser_mcp_agent
```

#### 2. Install Dependencies
Ensure you have Python 3.8+ and Node.js installed. Install the core engine and browser drivers:
```bash
# Install Python packages
pip install -r requirements.txt

# Install Playwright browser binaries
playwright install
```

#### 3. Configure API Keys
Authenticate your session by setting your OpenAI credentials:
```bash
# For macOS/Linux
export OPENAI_API_KEY='your-api-key-here'

# For Windows (PowerShell)
$env:OPENAI_API_KEY='your-api-key-here'
```

#### 4. Launch the Hub
Start the high-performance Streamlit interface to begin browsing:
```bash
streamlit run main.py
```

---

### 🛠 Architecture
**Pixra AI Hub** is built on a high-tech stack designed for scalability:
*   **Agentic Framework**: MCP-Agent for advanced tool-calling and logic.
*   **Automation Engine**: Playwright for headless browser control.
*   **Interface**: Streamlit for a clean, premium user experience.
*   **Intelligence**: Optimized for OpenAI and Anthropic LLM integration.