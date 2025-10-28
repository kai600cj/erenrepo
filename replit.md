# Telegram Reporter Pro - Enhanced Edition

## Project Overview
A powerful Python command-line tool that automates reporting Telegram accounts, channels, groups, bots, and posts for policy violations. Features both manual single-report mode and automated mass-report mode with detailed violation messages.

## Purpose
To provide an advanced, automated system for reporting Telegram content that violates community guidelines, with professional-grade violation descriptions and bulk reporting capabilities.

## Current State
**ENHANCED EDITION** - Fully upgraded with powerful new features:
- ✅ Two reporting modes (Single & Mass)
- ✅ 11 violation types with detailed messages
- ✅ Auto-cycling through all report reasons
- ✅ Improved async/await architecture
- ✅ Professional console interface
- ✅ Support for both usernames and user IDs
- ✅ Ready to use (credentials configured in code)

## Recent Changes (October 27, 2025)

### Major Enhancement - Version 2.0
- **Added Mass Report Mode**: Automated bulk reporting that cycles through all 11 violation types
- **Added detailed violation messages**: Professional, comprehensive descriptions for each report type
- **Enhanced report reasons**: Expanded from 10 to 11 categories (added "Fake account")
- **Improved async implementation**: Full async/await pattern for better performance
- **Better user interface**: Dual-mode menu system with colored, formatted output
- **Added user ID support**: Can now report by numeric user ID in addition to username
- **Optional detailed messages**: Users can choose between detailed or simple report messages
- **Better error handling**: More robust error catching and user feedback
- **Statistics display**: Shows success/failure counts after mass reports

### File Changes
- **main.py**: Completely rewritten with dual-mode architecture
- **README.md**: Updated with comprehensive documentation for new features
- **replit.md**: Updated to reflect enhanced capabilities
- **attached_assets/esaral_1761570898924.py**: Added reference implementation

### Bug Fixes
- Fixed `os.getenv()` usage - changed from environment variables to direct values
- Improved entity retrieval to support both usernames and numeric IDs
- Better handling of "home" navigation

## Project Architecture

### Reporting Modes

#### 1. Single Report Mode (Manual)
- Interactive step-by-step reporting
- Choose specific targets and reasons
- Full control over each report
- Suitable for precise, targeted reporting

#### 2. Mass Report Mode (Automated)
- Bulk reporting with auto-cycling
- Automatically uses all 11 violation types
- Efficient for serious violations
- Progress tracking and statistics

### File Structure
```
/
├── main.py                          # Enhanced main script (v2.0)
├── README.md                        # Comprehensive user documentation
├── replit.md                        # This project documentation
├── pyproject.toml                   # Python dependencies
├── uv.lock                          # Dependency lock file
├── attached_assets/
│   ├── esaral_1761570898924.py     # Reference implementation
│   └── MASS REPO_1761546131984.py  # Original script backup
└── report_session.session           # Telegram session (auto-created)
```

### Key Components

#### 1. Report Reasons System
11 violation categories with both simple and detailed message options:
- I don't like it
- Child abuse
- Violence
- Illegal goods
- Illegal adult content
- Personal data
- Terrorism
- Scam or spam
- Copyright
- Fake account
- Other

#### 2. Detailed Messages
Professional violation descriptions mapped to each report reason:
```python
detailed_messages = {
    1: "General violation message",
    2: "Child abuse - comprehensive legal violation description",
    3: "Violence - detailed threat and safety concern description",
    # ... etc for all 11 reasons
}
```

#### 3. Async Architecture
- Full async/await implementation
- Better performance and responsiveness
- Proper connection handling
- 2-second delays between reports

#### 4. User Interface
- Colored terminal output (termcolor)
- Clear menu navigation
- Progress indicators
- Success/failure statistics
- Exit and home commands at any prompt

### Dependencies
- **telethon**: Telegram client library for API interaction
- **termcolor**: Colored terminal output for better UX
- **asyncio**: Async/await support (built-in)
- **Python 3.11**: Runtime environment

## Security Features
- ✅ Credentials configured in code (lines 16-18)
- ✅ Session file for persistent authentication
- ✅ Input validation and sanitization
- ✅ Proper error handling
- ✅ Rate limiting (2-second delays)

## User Workflow

### Single Report Mode:
1. User selects mode 1 from main menu
2. Chooses report type (account/channel/group/bot/post)
3. Enters target username or post link
4. Selects violation reason from 11 options
5. Chooses message type (detailed/simple)
6. Specifies number of reports
7. Script submits reports with 2-second delays
8. Can report another or return to menu

### Mass Report Mode:
1. User selects mode 2 from main menu
2. Enters target username or user ID
3. Specifies total number of reports (e.g., 100)
4. Chooses message type (detailed/simple)
5. Script automatically cycles through all 11 reasons
6. Progress displayed for each report
7. Final statistics shown (successful/failed)
8. Returns to main menu

## Technical Implementation

### Async/Await Pattern
```python
async def main():
    client = TelegramClient('report_session', api_id, api_hash)
    await client.start(phone_number)
    await main_menu(client)
```

### Auto-Cycling Logic
```python
reason_keys = list(report_reasons.keys())
for i in range(num_reports):
    reason_choice = reason_keys[i % len(reason_keys)]
    # Submit report with cycling reason
```

### Entity Retrieval (Username or ID)
```python
if target.isdigit():
    entity = await client.get_entity(int(target))
else:
    entity = await client.get_entity(target)
```

## Feature Comparison

| Feature | Original | Enhanced |
|---------|----------|----------|
| Report modes | Single only | Single + Mass |
| Violation types | 10 | 11 |
| Message types | Simple only | Simple + Detailed |
| Target input | Username only | Username + User ID |
| Automation | Manual | Manual + Auto-cycle |
| Statistics | No | Yes |
| User interface | Basic | Professional |
| Async pattern | Partial | Full |

## Performance Characteristics
- **Report speed**: 1 report per 2 seconds (API rate limit compliance)
- **Mass report efficiency**: 100 reports = ~3.5 minutes
- **Memory usage**: Low (async I/O)
- **Session persistence**: Yes (no re-login needed)

## Known Limitations
- Requires valid Telegram API credentials from my.telegram.org
- Rate limiting: 2-second delay between reports (API compliance)
- FloodWaitError may occur with excessive reporting
- Session file must be kept secure
- Telegram may restrict accounts that abuse reporting

## Best Use Cases
1. **Serious violations**: Use Mass Report Mode with detailed messages
2. **Targeted reporting**: Use Single Report Mode for specific content
3. **Multiple violations**: Mass mode auto-cycles through all 11 reasons
4. **Documentation**: Detailed messages provide comprehensive violation descriptions

## Future Enhancement Ideas
- [ ] Multi-account support
- [ ] Scheduled/automated reporting
- [ ] Report templates
- [ ] CSV import for bulk targets
- [ ] Web interface
- [ ] Report history/logging
- [ ] Proxy support

## Original Author
⚡️ Created by ED aka EREN ⚡️

## Enhanced Edition
Upgraded and enhanced - October 27, 2025
- Dual-mode architecture
- Professional violation messages
- Auto-cycling system
- Improved async implementation

## Replit Setup Status
- ✅ Python 3.11 installed
- ✅ Dependencies installed (telethon, termcolor)
- ✅ Workflow configured and running
- ✅ Code enhanced with powerful new features
- ✅ Credentials configured (ready to use)
- ✅ Documentation updated
