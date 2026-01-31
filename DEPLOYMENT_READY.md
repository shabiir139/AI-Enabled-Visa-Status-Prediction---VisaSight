# 🚀 Deployment Ready!

Your code is now fully optimized for deployment. Follow these final steps to connect everything.

## Step 1: Get Your Backend URL
1. Go to your **Railway Dashboard**.
2. Click on your `visasight` project.
3. Click on the **Backend** service.
4. Go to **Settings** -> **Networking**.
5. Copy your **Public Domain** (e.g., `visasight-production.up.railway.app`).
   *Make sure it starts with `https://`*

## Step 2: Configure Vercel (Frontend)
1. Go to your **Vercel Dashboard**.
2. Click on your `visasight` project.
3. Go to **Settings** -> **Environment Variables**.
4. Add the following variable:
   - **Key**: `NEXT_PUBLIC_API_URL`
   - **Value**: `https://YOUR-RAILWAY-URL.up.railway.app` (Paste the URL from Step 1)
5. **Redeploy** your frontend (Go to Deployments -> Redeploy) for changes to take effect.

## Step 3: Configure Railway (Backend)
1. Go to your **Railway Dashboard**.
2. Go to **Variables**.
3. Ensure these are set:
   - `SUPABASE_URL`: (Your Supabase URL)
   - `SUPABASE_KEY`: (Your Supabase Key)
   - `FRONTEND_URL`: (Your Vercel URL, e.g., `https://visasight.vercel.app`)
   - `LOW_MEMORY_MODE`: `true`
   - `MODEL_TYPE`: `mock` (Switch to `baseline` later if needed)

## 🎉 Done!
Your frontend will now automatically talk to your backend using the URL you configured!
