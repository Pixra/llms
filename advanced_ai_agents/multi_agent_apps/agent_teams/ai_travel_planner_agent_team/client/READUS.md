# 💻 Pixra Travel AI: Frontend UI

This is the Next.js frontend interface for the Pixra Travel Agent Team. It provides a sleek, interactive web UI for users to input their travel preferences and view their AI-generated itineraries.

### 🚀 Getting Started

**1. Install Dependencies**
We recommend using `pnpm` for optimal performance:
```bash
pnpm install
```

**2. Configure Environment**
Copy the example environment file and add your database/API credentials:
```bash
cp .env.example .env.local
```

**3. Setup the Database (Prisma)**
Generate the Prisma client and push the schema to your database:
```bash
pnpm prisma generate
pnpm prisma db push
```

**4. Run the Development Server**
```bash
pnpm dev
```
*(Open [http://localhost:3000](http://localhost:3000) in your browser to see the Pixra Travel interface in action!)*