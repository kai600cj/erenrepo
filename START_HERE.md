# 🚀 Quick Start: Deploy to Render

Your Telegram Reporter Bot is ready to deploy! Follow these simple steps:

## 📋 Files Created for Render:
✅ `requirements.txt` - Python dependencies
✅ `render.yaml` - Auto-deploy configuration
✅ `.gitignore` - Keeps sensitive files safe
✅ `RENDER_DEPLOYMENT.md` - Detailed guide

---

## 🎯 Deploy in 3 Steps:

### **Step 1: Push to GitHub**
```bash
git init
git add .
git commit -m "Telegram Reporter Bot ready for deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### **Step 2: Connect to Render**
1. Go to: https://dashboard.render.com/
2. Sign in with GitHub
3. Click **"New +"** → **"Background Worker"**
4. Select your repository
5. Render auto-detects settings ✨

### **Step 3: Add Secrets**
In Render Dashboard → Environment Variables, add:

| Key | Value | Where to Get |
|-----|-------|--------------|
| `BOT_TOKEN` | Your bot token | [@BotFather](https://t.me/BotFather) on Telegram |
| `API_ID` | Your API ID | [my.telegram.org/apps](https://my.telegram.org/apps) |
| `API_HASH` | Your API hash | [my.telegram.org/apps](https://my.telegram.org/apps) |

Then click **"Create Background Worker"** → Done! 🎉

---

## 💰 Pricing Options:

**🆓 Free Tier:**
- Completely free forever
- Bot sleeps after 15 min of inactivity
- Wakes up in ~30 seconds on first use

**💎 Paid Plan ($7/month):**
- Always online 24/7
- Instant responses
- No sleep delays

---

## 📱 How to Use Your Bot:

1. Find your bot on Telegram (search for the name you gave @BotFather)
2. Send `/start`
3. Enter your API credentials when asked
4. Choose report mode:
   - 🎯 Single Report - Manual, precise reporting
   - 🔥 Mass Report - Auto-cycle through all 11 violation types

---

## 🔧 Features:

✨ **Report Anything:**
- Accounts, Channels, Groups, Bots
- Specific posts in channels/groups

✨ **11 Violation Categories:**
1. I don't like it
2. Child abuse
3. Violence
4. Illegal goods
5. Illegal adult content
6. Personal data
7. Terrorism
8. Scam or spam
9. Copyright
10. Fake account
11. Other

✨ **Smart Features:**
- OTP with spaces (bypass Telegram restrictions)
- Live report counter
- Detailed violation messages
- Auto-cycling through all reasons

---

## 📊 Monitor Your Bot:

**View Logs:**
Render Dashboard → Your Service → Logs

**Restart Bot:**
Dashboard → Manual Deploy

**Update Code:**
Just push to GitHub - Render auto-deploys!

---

## ⚡ Created by ED aka EREN

Need help? Check `RENDER_DEPLOYMENT.md` for detailed troubleshooting!
