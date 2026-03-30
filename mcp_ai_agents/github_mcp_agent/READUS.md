# 🐙 Pixra AI Hub: GitHub Intelligence

Transform your repository data into actionable intelligence. **Pixra AI Hub** leverages the Model Context Protocol (MCP) to provide a high-performance conversational layer for your GitHub ecosystem, bridging the gap between complex codebases and natural language reasoning.

---

### ✨ Features

*   **Natural Language Logic**: Query complex repository data using plain English—eliminate the need for manual API filtering or complex SQL.
*   **Predictive Analytics**: Execute high-precision reasoning on pull requests, issues, and repository velocity to identify bottlenecks before they occur.
*   **MCP Architecture**: Built on the industry-standard Model Context Protocol for secure, low-latency communication with the GitHub API.
*   **Architect Dashboard**: A premium, high-tech Streamlit interface designed for technical leads to monitor code quality and team health in real-time.
*   **Deep Synchronization**: Real-time tracking of repository activity, labels, and conflict status for total environment transparency.

---

### 🚀 Setup Guide

Deploy your private intelligence instance in four streamlined steps.

#### 1. Clone the Repository
Initialize your local environment by cloning the core repository:
```bash
git clone https://github.com/Pixra/llms.git
cd llms/mcp-github-agent
```

#### 2. Environment Installation
Ensure **Python 3.8+** and **Docker** are active on your system. Docker is utilized to containerize the official GitHub MCP server.
```bash
# Install required dependencies
pip install -r requirements.txt

# Verify Docker status
docker --version
```

#### 3. Configure Security Keys
To power the reasoning engine, obtain and configure the following credentials:
*   **OpenAI API Key**: Secure your key via the [OpenAI Platform](https://platform.openai.com/).
*   **GitHub PAT**: Generate a Personal Access Token with `repo` scope in [GitHub Settings](https://github.com/settings/tokens).

#### 4. Launch the Instance
Run the high-performance dashboard to begin your analysis:
```bash
streamlit run github_agent.py
```

---

### 💡 Example Queries

| Category | Premium Query Template |
| :--- | :--- |
| **Issues** | "Identify all high-priority bugs currently labeled as 'critical'." |
| **Pull Requests** | "Which PRs are currently blocked or awaiting technical review?" |
| **Health** | "Generate a comprehensive summary of activity over the last 14 days." |
| **Quality** | "Analyze code quality trends across the most recent merged PRs." |

---
*Powered by Pixra AI Hub — Streamlining the future of LLM-integrated workflows.*