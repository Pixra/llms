# ⚡ Pixra AI Hub

Elevate your AI applications with **Pixra AI Hub**, a high-performance engine designed for ultra-responsive streaming and seamless state management. Built for developers who demand premium architecture, this hub provides the foundation for real-time, event-driven intelligent conversations.

---

## 🚀 Features

- **Real-time Token Streaming**: Deliver instantaneous, token-by-token feedback using OpenAI’s low-latency streaming protocols.
- **Dynamic State Management**: Maintain complex conversation histories with real-time updates and persistent context.
- **Event-Driven Core**: Utilize a modular API → Event → Response flow, optimized for scalability and high-concurrency environments.
- **Ultra-Lean Architecture**: Achieve enterprise-grade performance with a minimal footprint, ensuring maximum efficiency and maintainability.

---

## 📁 Architecture

```bash
pixra-ai-hub/
├── steps/
│   ├── conversation.stream.ts    # Real-time state persistence
│   ├── chat-api.step.ts         # High-performance API gateway  
│   └── ai-response.step.ts      # Streaming logic & AI orchestration
├── package.json                 # Core dependencies
└── .env.example                 # Production configuration template
```

---

## 🛠️ Setup

Follow these steps to deploy your high-performance AI streaming node:

### 1. Clone the Repository
```bash
git clone https://github.com/Pixra/llms.git
cd pixra-ai-hub
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Configure API Keys
Copy the environment template and insert your credentials:
```bash
cp .env.example .env
# Open .env and add your OPENAI_API_KEY
```

### 4. Run the Hub
```bash
npm run dev
# Access the interface at http://localhost:3000
```

---

## 🔧 API Reference

### Execute Chat Stream
**POST** `/chat`

```json
{
  "message": "Analyze the latest market trends.",
  "conversationId": "optional-uuid"
}
```

**Stream States:**
- `created`: Handshake established.
- `streaming`: AI processing and emitting tokens.
- `completed`: Full response finalized and state persisted.

---

## 💎 Why Pixra AI Hub?

Pixra AI Hub removes the friction between complex AI backends and fluid user experiences. By leveraging **Type-safe events** and **Built-in state synchronization**, developers can focus on building unique features rather than debugging infrastructure. It is the definitive choice for modern, high-tech AI implementations.