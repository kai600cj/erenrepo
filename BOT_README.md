# Telegram Reporter Bot - Interactive Bot Version

An interactive Telegram bot that makes reporting violations easy through a conversational interface.

## 🤖 Features

### **Interactive Setup:**
- Bot asks for your API ID, API Hash, and Phone Number
- No need to edit code files
- Secure session management per user
- Each user has their own credentials

### **Two Reporting Modes:**
- **🎯 Single Report Mode** - Choose specific violation type
- **🚀 Mass Report Mode** - Auto-cycle through all 11 violations

### **User-Friendly Interface:**
- Step-by-step guided process
- Interactive buttons for easy selection
- Real-time progress updates
- Statistics after completion

## 📋 Setup Instructions

### Step 1: Create Your Bot

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` command
3. Choose a name for your bot (e.g., "My Reporter Bot")
4. Choose a username (must end with 'bot', e.g., "myreporter_bot")
5. **Copy the BOT_TOKEN** you receive

### Step 2: Get Telegram API Credentials

1. Visit **https://my.telegram.org**
2. Log in with your phone number
3. Go to "API development tools"
4. Fill out the form:
   - App title: Any name (e.g., "Reporter Tool")
   - Short name: 5-32 characters
   - Platform: Desktop
5. Copy your `api_id` and `api_hash` (you'll enter these in the bot)

### Step 3: Set Bot Token

Add your BOT_TOKEN as a secret in Replit:

1. Click the **🔒 Secrets** tab
2. Add secret:
   - **Key:** `BOT_TOKEN`
   - **Value:** Your token from BotFather
3. Click "Add new secret"

### Step 4: Run the Bot

1. Click **Run** button
2. Wait for "🤖 Telegram Reporter Bot is running..."
3. Open your bot in Telegram
4. Send `/start` command

## 🎮 How to Use

### First Time Setup (in the bot):

1. **Send** `/start` to your bot
2. **Enter API ID** when prompted (numbers from my.telegram.org)
3. **Enter API Hash** when prompted
4. **Enter Phone Number** with country code (e.g., +1234567890)
5. Bot is now ready!

### Reporting Process:

#### Option 1: Single Report Mode
1. Click "🎯 Single Report Mode"
2. Enter target username or ID
3. Select violation reason from 11 options
4. Enter number of reports
5. Choose message type (Detailed/Simple)
6. Bot submits reports automatically

#### Option 2: Mass Report Mode
1. Click "🚀 Mass Report Mode"
2. Enter target username or ID
3. Enter total number of reports (e.g., 110)
4. Choose message type (Detailed/Simple)
5. Bot auto-cycles through all 11 violation types

### Example Session:

```
You: /start
Bot: Welcome! Please send your API ID:

You: 12345678
Bot: ✅ API ID saved! Now send your API Hash:

You: abc123def456...
Bot: ✅ API Hash saved! Send your Phone Number:

You: +1234567890
Bot: ✅ All credentials saved! Select mode:
     [🎯 Single Report] [🚀 Mass Report]

You: [Click Mass Report]
Bot: Enter target username or ID:

You: @baduser
Bot: How many total reports? (50-500 recommended)

You: 110
Bot: Choose message type:
     [📝 Detailed] [📄 Simple]

You: [Click Detailed]
Bot: ⏳ Starting reports...
     🚀 Progress: 10/110
     ✅ Successful: 10
     ❌ Failed: 0
     ...
     
Bot: ✅ Reports Complete!
     Total: 110
     Successful: 110
     Failed: 0
```

## 📊 Available Violations

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

## 💡 Pro Tips

### For Maximum Effectiveness:
- Use **Mass Report Mode** for serious violations
- Choose **Detailed Messages** for stronger impact
- Submit **100-500 reports** for best results
- Reports auto-cycle through all violation types

### Security Best Practices:
- Each user's credentials are stored separately
- Session files are isolated per user
- Never share your BOT_TOKEN
- Keep API credentials secure

## 🔧 Bot Commands

- `/start` - Begin interaction or restart
- `/cancel` - Cancel current operation

## ⚙️ Features

### Smart Session Management:
- Credentials stored per user
- Each user gets their own Telethon session
- No interference between users
- Sessions persist between bot restarts

### Progress Tracking:
- Real-time updates every 10 reports
- Success/failure statistics
- Current violation type shown
- Time estimation

### Error Handling:
- Clear error messages
- Retry options
- Input validation
- Credential verification

## 🚨 Important Notes

- ⚠️ **Use responsibly**: Only report real violations
- 🔒 **Privacy**: Your credentials are stored securely
- ⏱️ **Rate limits**: 2-second delay between reports
- 🚫 **Abuse warning**: Don't misuse the reporting system

## 🔄 Workflow Comparison

### CLI Version (main.py):
- Run from console
- Credentials hardcoded
- Single user
- Direct control

### Bot Version (bot.py):
- Run via Telegram chat
- Credentials entered per user
- Multi-user support
- Interactive buttons

## 📁 File Structure

```
/
├── bot.py              # Telegram bot version (this)
├── main.py             # CLI version
├── BOT_README.md       # This file
└── README.md           # CLI version docs
```

## 🐛 Troubleshooting

**Bot doesn't respond:**
- Check BOT_TOKEN is set correctly in Secrets
- Make sure bot is running (check console)
- Restart the workflow

**"Not authorized" error:**
- Your phone will receive a verification code
- Bot will prompt you to enter it
- This only happens on first use

**Reports failing:**
- Check your API credentials
- Verify target username exists
- Try reducing number of reports

**FloodWaitError:**
- You're sending too many reports
- Wait for the specified time
- Reduce report count

## 🎯 Use Cases

### Perfect for:
- ✅ Non-technical users (no coding needed)
- ✅ Multiple people using same bot
- ✅ Quick, on-the-go reporting
- ✅ Mobile-first experience

### When to use CLI version instead:
- Advanced automation
- Server deployment
- Single dedicated user
- Custom modifications

---

⚡️ **Created by ED aka EREN** ⚡️  
**Bot Version - October 2025**
