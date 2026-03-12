# 📰 News Aggregator

An AI-powered news aggregator that fetches, summarizes, and analyzes sentiment of news articles across multiple categories.

🌐 **Live Demo:** [newsaggregatorproj.netlify.app](https://newsaggregatorproj.netlify.app)
🔗 **Backend API:** [news-aggregator-4d5n.onrender.com](https://news-aggregator-4d5n.onrender.com)

## 🚀 Features

- 🌍 Fetches real-time news from NewsAPI across 6 categories
- 🤖 AI-powered article summarization using Groq (LLaMA 3.3)
- 💬 Sentiment analysis (Positive, Negative, Neutral)
- 📧 Daily email digest via Gmail SMTP
- ⏰ Automated article fetching every 30 minutes
- 🎨 Dynamic category-based UI themes
- 🐳 Dockerized for easy deployment
- ✅ CI/CD pipeline via GitHub Actions

## 🛠️ Tech Stack

| Layer       | Technology                          |
|-------------|-------------------------------------|
| Backend     | Python, FastAPI                     |
| AI          | Groq API (LLaMA 3.3)                |
| News Source | NewsAPI                             |
| Frontend    | React, Tailwind CSS, Vite           |
| Scheduler   | APScheduler                         |
| Email       | Gmail SMTP                          |
| Testing     | Pytest                              |
| DevOps      | Docker, GitHub Actions              |
| Deployment  | Render (Backend), Netlify (Frontend)|

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/FaisalMubeen2001/News-Aggregator.git
cd News-Aggregator
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```env
NEWS_API_KEY=your_newsapi_key
GROQ_API_KEY=your_groq_key
EMAIL_SENDER=your_gmail
EMAIL_PASSWORD=your_gmail_app_password
EMAIL_RECEIVER=your_email
```

### 5. Run the backend
```bash
uvicorn backend.main:app --reload
```

### 6. Run the frontend
```bash
cd frontend
npm install
npm run dev
```

### 7. Run with Docker
```bash
docker-compose up --build
```

## 🧪 Running Tests
```bash
pytest tests/ -v
```

## 📁 Project Structure
```
News-Aggregator/
├── backend/
│   ├── api/
│   ├── models/
│   │   └── article.py
│   ├── services/
│   │   ├── news_service.py
│   │   ├── ai_service.py
│   │   └── email_service.py
│   ├── scheduler/
│   │   ├── jobs.py
│   │   └── scheduler.py
│   ├── main.py
│   └── config.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ArticleCard.jsx
│   │   │   └── CategoryFilter.jsx
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── vite.config.js
├── tests/
│   ├── test_api.py
│   └── test_services.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🌐 Deployment

- **Frontend** deployed on [Netlify](https://netlify.com)
- **Backend** deployed on [Render](https://render.com)
- **CI/CD** powered by GitHub Actions — tests run automatically on every push