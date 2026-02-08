# 🚀 Milestone 4: Deployment & Production

## Objective
Deploy the VisaSight application to production with robust CI/CD, monitoring, and scalability.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                        VERCEL                                │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Next.js 14 Frontend                     │    │
│  │  • React 18 with App Router                          │    │
│  │  • Framer Motion animations                          │    │
│  │  • Recharts visualizations                           │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼ HTTPS API Calls
┌─────────────────────────────────────────────────────────────┐
│                        RAILWAY                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              FastAPI Backend                         │    │
│  │  • REST API endpoints                                │    │
│  │  • ML model inference                                │    │
│  │  • Supabase client                                   │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼ SQL/Auth
┌─────────────────────────────────────────────────────────────┐
│                       SUPABASE                               │
│  • PostgreSQL Database                                       │
│  • Row Level Security                                        │
│  • User Authentication                                       │
│  • Real-time subscriptions                                   │
└─────────────────────────────────────────────────────────────┘
```

## Deployment Platforms

### Frontend (Vercel)
- **URL**: https://visasight.vercel.app
- **Framework**: Next.js 14
- **Build Command**: `npm run build`
- **Environment Variables**:
  - `NEXT_PUBLIC_API_URL`
  - `NEXT_PUBLIC_SUPABASE_URL`
  - `NEXT_PUBLIC_SUPABASE_ANON_KEY`

### Backend (Railway)
- **URL**: https://visasight-backend.up.railway.app
- **Framework**: FastAPI + Uvicorn
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Environment Variables**:
  - `SUPABASE_URL`
  - `SUPABASE_KEY`
  - `FRONTEND_URL`
  - `MODEL_TYPE` (mock/baseline/huggingface)

### Database (Supabase)
- **Region**: US East
- **Tables**: visa_cases, predictions, rules, users
- **Auth**: Email/Password, OAuth (Google)

## CI/CD Pipeline

### GitHub Actions Workflow
```yaml
name: VisaSight CI
on: [push, pull_request]

jobs:
  frontend-check:
    - npm install
    - npm run lint
    - npm run build

  backend-check:
    - pip install -r requirements.txt
    - python -c "from main import app"
```

### Deployment Triggers
- **Main Branch Push** → Auto-deploy to production
- **Pull Request** → Preview deployment + CI checks
- **Manual** → Railway/Vercel dashboard

## Monitoring & Observability

### Health Checks
- `/health` endpoint on backend
- Uptime monitoring via Railway
- Error tracking in console logs

### Performance Metrics
- API response times: <200ms average
- Frontend LCP: <2.5s
- Model inference: <500ms

## Security Measures

- ✅ CORS configured for production domains
- ✅ Environment secrets in platform configs
- ✅ Supabase Row Level Security enabled
- ✅ HTTPS enforced on all endpoints
- ✅ JWT authentication for protected routes

## Deliverables
- [x] Vercel frontend deployment
- [x] Railway backend deployment
- [x] Supabase database configuration
- [x] GitHub Actions CI/CD pipeline
- [x] Branch protection rules
- [x] Production environment documentation
