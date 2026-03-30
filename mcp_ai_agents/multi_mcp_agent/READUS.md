# 🌐 Pixra AI Hub

Unleash the power of unified intelligence. **Pixra AI Hub** is an enterprise-grade Multi-MCP orchestrator designed to bridge the gap between your LLM and your digital workspace. By integrating high-performance Model Context Protocol (MCP) servers, Pixra transforms natural language into actionable workflows across GitHub, Gmail, Calendar, and Perplexity.

## ⚡ Features

- **Unified Multi-Agent Orchestration**: Seamlessly switch between specialized agents powered by the Agno AI framework.
- **Deep GitHub Integration**: **Repository management**, automated issue tracking, and intelligent code analysis via natural language.
- **Real-Time Research**: Leverage **Perplexity AI** for live web searches and data-driven insights.
- **Productivity Suite**: Full control over **Gmail and Google Calendar** to automate scheduling and communication workflows.
- **Cross-Platform Tool Chaining**: Execute complex sequences, such as converting a GitHub issue into a Calendar event or summarizing research into an email.
- **High-Tech CLI Interface**: Experience **interactive streaming responses**, markdown formatting, and persistent session memory.
- **Enterprise-Grade Security**: Session-specific IDs and secure environment variable management ensure your data remains protected.

## 🛠️ Setup

Follow these steps to deploy the Pixra AI Hub on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/Pixra/llms.git
cd llms/mcp_ai_agents/multi_mcp_agent
```

### 2. Install Dependencies
Ensure you have Python 3.9+ and Node.js installed (Node is required for MCP server communication).
```bash
# Install Python packages
pip install -r requirements.txt

# Verify Node.js environment
node --version
npm --version
```

### 3. Configure API Keys
Create a `.env` file in the root directory and populate it with your credentials:
```env
OPENAI_API_KEY=your_openai_key
GITHUB_PERSONAL_ACCESS_TOKEN=your_github_token
PERPLEXITY_API_KEY=your_perplexity_key
```
*Note: Ensure your GitHub token has `repo`, `user`, and `admin:org` scopes enabled.*

### 4. Run the Agent
Initialize the interactive hub:
```bash
python multi_mcp_agent.py
```

---

### 🚀 Usage Examples
*   **Engineering:** *"Review the latest pull requests and summarize the changes."*
*   **Research:** *"Find the latest best practices for microservices and save them as a draft in Gmail."*
*   **Management:** *"Check my calendar for tomorrow and schedule a sync for any open GitHub issues."*

**Pixra AI Hub** — *The future of agentic productivity.*