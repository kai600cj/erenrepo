# 🚀 Deploy to Render - Quick Guide

## Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit - Telegram Reporter Bot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

## Step 2: Deploy on Render

### Method 1: Using render.yaml (Automatic)

1. Go to https://dashboard.render.com/
2. Click **"New +"** → **"Blueprint"**
3. Connect your GitHub repository
4. Render will detect `render.yaml` and auto-configure
5. Add environment variables:
   - `BOT_TOKEN` = Your bot token from @BotFather
   - `API_ID` = Your Telegram API ID from my.telegram.org
   - `API_HASH` = Your Telegram API hash from my.telegram.org
6. Click **"Apply"**

### Method 2: Manual Setup

1. Go to https://dashboard.render.com/
2. Click **"New +"** → **"Background Worker"**
3. Connect your GitHub repository
4. Configure:
   - **Name:** `telegram-reporter-bot`
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
5. Add environment variables (same as Method 1)
6. Click **"Create Background Worker"**

## Step 3: Get Your Bot Credentials

### Bot Token:
1. Message @BotFather on Telegram
2. Send `/newbot`
3. Follow instructions to create bot
4. Copy the token (looks like: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)

### API ID & API Hash:
1. Go to https://my.telegram.org/apps
2. Login with your phone number
3. Create an application
4. Copy your `api_id` (number) and `api_hash` (string)

## Step 4: Monitor Your Bot

- View logs: Render Dashboard → Your service → Logs
- Restart: Dashboard → Manual Deploy
- Update: Push to GitHub (auto-deploys)

## ⚡ Pricing

**Free Tier:**
- ✅ Free forever
- ⚠️ Spins down after 15 min inactivity
- ⚠️ Takes ~30 sec to wake up

**Paid Plan ($7/month):**
- ✅ 24/7 always online
- ✅ Instant responses
- ✅ No sleep/wake delays

## 🔧 Troubleshooting

### Bot not responding?
1. Check Render logs for errors
2. Verify environment variables are set correctly
3. Make sure bot token is valid

### Session errors?
Sessions don't persist on free tier. Bot will ask for login after each restart.
Upgrade to paid plan for persistent disk storage.

### Need help?
Check logs in Render dashboard for detailed error messages.

---

**Created by ED aka EREN** ⚡️
