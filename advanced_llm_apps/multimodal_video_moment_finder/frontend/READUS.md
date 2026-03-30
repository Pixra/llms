# 🌌 Pixra AI Hub

Elevate your workflow with a unified, high-performance interface for state-of-the-art Large Language Models. **Pixra AI Hub** is an enterprise-grade ecosystem designed to bridge the gap between complex AI intelligence and seamless user experience.

---

## ✨ Features

*   **Multi-Model Orchestration**: Seamlessly integrate and switch between world-class LLMs within a single, cohesive dashboard.
*   **Real-time Streaming**: Experience lightning-fast, low-latency text generation powered by optimized Vercel edge functions.
*   **Premium UI/UX**: A sophisticated, minimalist interface built with Tailwind CSS and Geist Sans for maximum readability and focus.
*   **Secure Architecture**: Robust environment management ensuring your API keys and data remain private and protected.

---

## 🚀 Getting Started

Follow these steps to deploy your local instance of Pixra AI Hub.

### 1. Clone the Repository
Start by pulling the latest version of the hub to your local machine:
```bash
git clone https://github.com/Pixra/llms.git
cd llms
```

### 2. Install Dependencies
Ensure you have [Node.js](https://nodejs.org/) installed, then run the installation:
```bash
npm install
# or
yarn install
```

### 3. Configure Environment Keys
Create a `.env.local` file in the root directory and add your provider credentials:
```env
# Example Keys
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

### 4. Run the Platform
Launch the development server to start building:
```bash
npm run dev
```
Navigate to [http://localhost:3000](http://localhost:3000) to view your premium AI interface.

---

**Built with precision using [Next.js](https://nextjs.org/).**