# 🛡️ AI Agent Governance

Implement a robust policy-based sandboxing layer to enforce deterministic safety on AI agents. Prevent unauthorized actions, restrict file system access, and ensure compliance with a specialized governance engine.

---

### ✨ Key Features
- **Policy-Based Sandboxing** to define declarative boundaries for agent actions.
- **Real-Time Action Interception** that validates requests before they reach the tool layer.
- **Comprehensive File & Network Guards** to restrict access to sensitive paths and domains.
- **Full Audit Logging** for tracking every agent decision, allow-list match, or denial.

---

### 🚀 Quick Start

**1. Clone & Navigate**
```bash
git clone https://github.com/Pixra/llms.git
cd llms/advanced_ai_agents/single_agent_apps/ai_agent_governance
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API Keys**
Set your API key in your environment or a `.env` file:
```env
OPENAI_API_KEY=your_actual_key_here
```

**4. Run the Governance Layer**
```bash
python ai_agent_governance.py
```
*(Try different actions to see how the policy engine enforces deterministic safety boundaries!)*
