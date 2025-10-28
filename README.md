# Telegram Reporter Pro - Enhanced Edition

A powerful Python command-line tool for reporting Telegram accounts, channels, groups, bots, and posts for policy violations.

## 🚀 New Features (Enhanced Edition)

### **Two Reporting Modes:**
1. **Single Report Mode** - Manual, precise reporting with full control
2. **Mass Report Mode** - Automated bulk reporting that cycles through all violation types

### **Enhanced Capabilities:**
- ✅ Detailed, professional violation messages for maximum impact
- ✅ Auto-cycling through all 11 report reasons
- ✅ Support for numeric user IDs in addition to usernames
- ✅ Improved async/await implementation for better performance
- ✅ Professional formatted console output with colors
- ✅ Better error handling and user experience

## Setup Instructions

### 1. Get Your Telegram API Credentials

You need to obtain your own `api_id` and `api_hash` from Telegram:

1. Visit **https://my.telegram.org**
2. Log in with your phone number
3. Go to "API development tools"
4. Fill out the form:
   - App title: Any name (e.g., "Reporter Tool")
   - Short name: 5-32 characters, no spaces
   - Platform: Desktop
5. Submit and copy your `api_id` and `api_hash`

### 2. Update Credentials in Code

**For this version**, update lines 16-18 in `main.py`:
```python
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'
```

### 3. Run the Script

Click the **Run** button or use the console to start the script.

On first run, Telegram will send you a verification code - enter it when prompted.

## How to Use

### Main Menu
When you start the script, you'll see:
```
1: Single Report Mode (Manual target & reason selection)
2: Mass Report Mode (Auto-cycle all reasons)
3: Exit
```

### Mode 1: Single Report Mode (Manual)

**Step-by-step control for precise reporting:**

1. **Choose what to report**:
   - 1: Account
   - 2: Channel
   - 3: Group
   - 4: Bot
   - 5: Post Link

2. **Enter the target**:
   - For accounts/channels/groups/bots: Enter username (e.g., @username) or user ID
   - For post links: Enter full URL (e.g., https://t.me/channel/12345)

3. **Select a reason** from 11 options:
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

4. **Choose message type**:
   - Detailed: Professional, comprehensive violation descriptions
   - Simple: Basic report message

5. **Specify number of reports** to submit

6. Reports are submitted automatically with 2-second delays

### Mode 2: Mass Report Mode (Automated)

**Powerful bulk reporting that auto-cycles through all reasons:**

1. **Enter target**: Username or user ID (e.g., @username or 123456789)

2. **Set total reports**: Recommended 50-500 for maximum effectiveness

3. **Choose message type**: Detailed or simple

4. **Automated execution**: Script cycles through all 11 violation types automatically

**Example**: If you choose 110 reports, each of the 11 reasons will be used 10 times

## Available Report Reasons

| # | Reason | Use Case |
|---|--------|----------|
| 1 | I don't like it | General violations |
| 2 | Child abuse | Serious illegal content |
| 3 | Violence | Threats, violent content |
| 4 | Illegal goods | Drug sales, weapons |
| 5 | Illegal adult content | Pornography |
| 6 | Personal data | Doxxing, privacy violations |
| 7 | Terrorism | Extremist content |
| 8 | Scam or spam | Spam, scams, fraud |
| 9 | Copyright | IP violations |
| 10 | Fake account | Impersonation |
| 11 | Other | Harassment, hate speech |

## Detailed Messages Feature

When enabled, each report includes a professional, comprehensive description of the violation:

**Example (Spam):**
> "This user is sending repeated spam messages across multiple groups and private chats, disturbing many users and flooding conversations unnecessarily. Please take action immediately to protect users from constant spam abuse."

**Example (Violence):**
> "The user is promoting violent threats and aggressive content. They have threatened members in chats and continue to spread harmful ideology that could lead to real-world consequences. Immediate moderation is needed."

## Commands

- Type `exit` at any prompt to quit
- Type `home` to return to the main menu
- Type `y` to continue, `n` to stop when prompted

## Pro Tips

### For Maximum Effectiveness:
1. **Use Mass Report Mode** for serious violations
2. **Enable detailed messages** for stronger reports
3. **Submit 100-500 reports** cycling through all reasons
4. **Combine with user reports** from multiple accounts if available
5. **Document evidence** before reporting

### Best Practices:
- Use appropriate report reasons for the actual violation
- Don't abuse the system - only report genuine violations
- Allow 2-second delays between reports (automatic)
- Keep session files secure

## Important Notes

- ⚠️ **Use responsibly**: Only report actual policy violations
- 🔒 **Security**: Keep your API credentials secure
- 📱 **Session**: The session file (`report_session.session`) persists login
- ⏱️ **Rate limits**: 2-second delays prevent API throttling
- 🚫 **Abuse warning**: Misusing Telegram's reporting system may result in account restrictions

## Technical Details

- **Language**: Python 3.11+
- **Library**: Telethon (async Telegram client)
- **Architecture**: Fully async/await for better performance
- **Dependencies**: telethon, termcolor

## Troubleshooting

**Script won't start / credentials error:**
- Verify your API credentials are correct
- Make sure API_ID is numeric only
- Check that phone number includes country code

**"FloodWaitError":**
- You're sending reports too fast
- Wait for the specified time
- Reduce the number of reports

**Session errors:**
- Delete `report_session.session` file
- Restart the script
- Re-enter verification code

## File Structure
```
/
├── main.py                          # Enhanced main script
├── README.md                        # This file
├── attached_assets/
│   ├── esaral_1761570898924.py     # Reference implementation
│   └── MASS REPO_1761546131984.py  # Original script
└── report_session.session           # Login session (auto-created)
```

---

⚡️ **Created by ED aka EREN** ⚡️  
**Enhanced Edition - October 2025**
