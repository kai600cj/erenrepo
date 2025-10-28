import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)
from telethon import TelegramClient
from telethon.tl.functions.account import ReportPeerRequest
from telethon.tl.types import (
    InputReportReasonSpam, InputReportReasonFake, InputReportReasonViolence,
    InputReportReasonPornography, InputReportReasonChildAbuse,
    InputReportReasonCopyright, InputReportReasonIllegalDrugs,
    InputReportReasonPersonalDetails, InputReportReasonOther
)
from telethon.errors import SessionPasswordNeededError

API_ID, API_HASH, PHONE, VERIFICATION_CODE, MODE_SELECT, TARGET_INPUT, REASON_SELECT, COUNT_INPUT, MESSAGE_TYPE = range(9)

user_sessions = {}

report_reasons = {
    1: ("I don't like it", InputReportReasonOther()),
    2: ("Child abuse", InputReportReasonChildAbuse()),
    3: ("Violence", InputReportReasonViolence()),
    4: ("Illegal goods", InputReportReasonIllegalDrugs()),
    5: ("Illegal adult content", InputReportReasonPornography()),
    6: ("Personal data", InputReportReasonPersonalDetails()),
    7: ("Terrorism", InputReportReasonViolence()),
    8: ("Scam or spam", InputReportReasonSpam()),
    9: ("Copyright", InputReportReasonCopyright()),
    10: ("Fake account", InputReportReasonFake()),
    11: ("Other", InputReportReasonOther())
}

detailed_messages = {
    1: "This account is causing disruption and violating community guidelines through inappropriate behavior that negatively impacts other users.",
    2: "This account appears to be involved in highly disturbing content related to child abuse. Such content is unacceptable and violates global laws. Immediate investigation and action are needed.",
    3: "The user is promoting violent threats and aggressive content. They have threatened members in chats and continue to spread harmful ideology that could lead to real-world consequences. Immediate moderation is needed.",
    4: "This account is promoting the sale of illegal goods including drugs and other prohibited substances. This violates Telegram's terms of service and poses serious legal risks.",
    5: "User is actively sharing pornographic, NSFW, and sexually explicit content in both public and private Telegram spaces. This behavior is dangerous for the community and against the platform's policy.",
    6: "This account is sharing personal and private information of individuals without consent, which constitutes doxxing and harassment. This puts people at risk.",
    7: "This account is promoting terrorist ideology, violent extremism, and threatening content that poses a serious security risk to communities and individuals.",
    8: "This user is sending repeated spam messages across multiple groups and private chats, disturbing many users and flooding conversations unnecessarily. Please take action immediately to protect users from constant spam abuse.",
    9: "This account is violating copyright laws by sharing copyrighted content without permission from the original creators. This infringes on intellectual property rights.",
    10: "The user is impersonating others and sharing false information to scam and mislead people. Many users have been affected by this fake identity. Telegram must take immediate steps.",
    11: "The account is continuously misusing the platform by harassing others, spreading hate speech, and causing disturbance. It needs to be reported under other serious violations."
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    await update.message.reply_text(
        "⚡️ *REPORTER PRO* ⚡️\n"
        "🔥 Mass & Single Report Modes | 11 Categories\n"
        "━━━━━━━━━━━━━━━━━━━\n\n"
        "🚀 Get API credentials: my.telegram.org\n\n"
        "📝 Send your *API ID*:",
        parse_mode='Markdown'
    )
    return API_ID


async def get_api_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    api_id = update.message.text.strip()
    
    if not api_id.isdigit():
        await update.message.reply_text("❌ API ID must be numbers only. Please try again:")
        return API_ID
    
    if user_id not in user_sessions:
        user_sessions[user_id] = {}
    
    user_sessions[user_id]['api_id'] = int(api_id)
    
    await update.message.reply_text(
        "✅ API ID saved!\n\n"
        "Now, please send your *API Hash*:",
        parse_mode='Markdown'
    )
    return API_HASH


async def get_api_hash(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    api_hash = update.message.text.strip()
    
    if len(api_hash) < 20:
        await update.message.reply_text("❌ API Hash seems too short. Please check and try again:")
        return API_HASH
    
    user_sessions[user_id]['api_hash'] = api_hash
    
    await update.message.reply_text(
        "✅ API Hash saved!\n\n"
        "Finally, send your *Phone Number* with country code:\n"
        "Example: +1234567890",
        parse_mode='Markdown'
    )
    return PHONE


async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    phone = update.message.text.strip()
    
    if not phone.startswith('+'):
        await update.message.reply_text("❌ Phone number must start with + and country code.\nExample: +1234567890\n\nPlease try again:")
        return PHONE
    
    user_sessions[user_id]['phone'] = phone
    
    msg = await update.message.reply_text("🔐 *Checking authorization...*", parse_mode='Markdown')
    
    try:
        api_id = user_sessions[user_id]['api_id']
        api_hash = user_sessions[user_id]['api_hash']
        session_name = f'bot_session_{user_id}'
        
        client = TelegramClient(session_name, api_id, api_hash)
        await client.connect()
        
        if not await client.is_user_authorized():
            await client.send_code_request(phone)
            user_sessions[user_id]['client'] = client
            user_sessions[user_id]['awaiting_code'] = True
            
            await msg.edit_text(
                "📱 *Verification code sent!*\n\n"
                "Telegram has sent a code to your phone.\n\n"
                "⚠️ *IMPORTANT:* Enter code with spaces between digits\n"
                "Example: If code is 88888, enter: `8 8 8 8 8`\n\n"
                "Please enter the code with spaces:",
                parse_mode='Markdown'
            )
            return VERIFICATION_CODE
        else:
            await client.disconnect()
            user_sessions[user_id]['authorized'] = True
            
            keyboard = [
                [InlineKeyboardButton("🎯 Single Report Mode", callback_data="mode_single")],
                [InlineKeyboardButton("🚀 Mass Report Mode", callback_data="mode_mass")],
                [InlineKeyboardButton("⚙️ Change Credentials", callback_data="change_creds")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await msg.edit_text(
                "✅ *Already authorized!*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "🎯 *Select Reporting Mode:*\n\n"
                "• *Single Report Mode*\n"
                "  Manual control, choose specific reasons\n\n"
                "• *Mass Report Mode*\n"
                "  Auto-cycle through all 11 violation types",
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
            return MODE_SELECT
            
    except Exception as e:
        await msg.edit_text(f"❌ Error: {str(e)}\n\nUse /start to try again.")
        return ConversationHandler.END


async def get_verification_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    code_or_password = update.message.text.strip()
    
    code_or_password = code_or_password.replace(' ', '')
    
    client = user_sessions[user_id].get('client')
    
    if not client:
        await update.message.reply_text("❌ Session expired. Please use /start to begin again.")
        return ConversationHandler.END
    
    needs_password = user_sessions[user_id].get('needs_password', False)
    
    if not needs_password and not code_or_password.isdigit():
        await update.message.reply_text("❌ Verification code should be numbers only (with spaces).\n\nExample: `8 8 8 8 8`\n\nPlease try again:", parse_mode='Markdown')
        return VERIFICATION_CODE
    
    msg = await update.message.reply_text("🔐 *Verifying...*", parse_mode='Markdown')
    
    try:
        phone = user_sessions[user_id]['phone']
        
        try:
            if needs_password:
                await client.sign_in(password=code_or_password)
            else:
                await client.sign_in(phone, code_or_password)
            
            user_sessions[user_id]['authorized'] = True
            user_sessions[user_id].pop('awaiting_code', None)
            user_sessions[user_id].pop('needs_password', None)
            user_sessions[user_id].pop('client', None)
            await client.disconnect()
            
        except SessionPasswordNeededError:
            user_sessions[user_id]['needs_password'] = True
            await msg.edit_text(
                "🔒 *2FA Enabled*\n\n"
                "Your account has two-factor authentication.\n"
                "Please enter your 2FA password:",
                parse_mode='Markdown'
            )
            return VERIFICATION_CODE
        
        keyboard = [
            [InlineKeyboardButton("🎯 Single Report Mode", callback_data="mode_single")],
            [InlineKeyboardButton("🚀 Mass Report Mode", callback_data="mode_mass")],
            [InlineKeyboardButton("⚙️ Change Credentials", callback_data="change_creds")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await msg.edit_text(
            "✅ *AUTHORIZATION SUCCESSFUL!* ✅\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "⚡️ *REPORTER PRO ACTIVATED* ⚡️\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎯 *SELECT YOUR MODE:*\n\n"
            "🔹 *Single Report Mode*\n"
            "   └ Manual control, precision targeting\n\n"
            "🔹 *Mass Report Mode*\n"
            "   └ Auto-cycle, maximum impact\n\n"
            "⚡️ *Powered by ED aka EREN* ⚡️",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        return MODE_SELECT
        
    except Exception as e:
        await msg.edit_text(f"❌ Invalid code/password or error: {str(e)}\n\nPlease try again or use /start to restart:")
        return VERIFICATION_CODE


async def mode_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    user_id = update.effective_user.id
    
    if query.data == "change_creds":
        await query.edit_message_text(
            "🔄 *Resetting credentials...*\n\n"
            "Please send your *API ID* (numbers only):",
            parse_mode='Markdown'
        )
        return API_ID
    
    user_sessions[user_id]['mode'] = query.data.replace("mode_", "")
    
    await query.edit_message_text(
        f"✅ *{query.data.replace('mode_', '').title()} Report Mode* selected!\n\n"
        "📝 Please enter the target username or user ID:\n"
        "Examples:\n"
        "• @username\n"
        "• username\n"
        "• 123456789 (user ID)",
        parse_mode='Markdown'
    )
    return TARGET_INPUT


async def get_target(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    target = update.message.text.strip()
    
    user_sessions[user_id]['target'] = target
    
    if user_sessions[user_id]['mode'] == 'mass':
        await update.message.reply_text(
            "🎯 *Target saved!*\n\n"
            "📊 How many total reports to submit?\n"
            "Recommended: 50-500\n\n"
            "Enter number:",
            parse_mode='Markdown'
        )
        return COUNT_INPUT
    else:
        keyboard = []
        for num, (reason_name, _) in report_reasons.items():
            keyboard.append([InlineKeyboardButton(f"{num}. {reason_name}", callback_data=f"reason_{num}")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "📋 *Select Report Reason:*",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        return REASON_SELECT


async def reason_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    user_id = update.effective_user.id
    reason_num = int(query.data.replace("reason_", ""))
    
    user_sessions[user_id]['reason'] = reason_num
    
    await query.edit_message_text(
        f"✅ Reason: *{report_reasons[reason_num][0]}*\n\n"
        "📊 How many reports to submit?\n"
        "Enter number:",
        parse_mode='Markdown'
    )
    return COUNT_INPUT


async def get_count(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    count = update.message.text.strip()
    
    if not count.isdigit():
        await update.message.reply_text("❌ Please enter a valid number:")
        return COUNT_INPUT
    
    user_sessions[user_id]['count'] = int(count)
    
    keyboard = [
        [InlineKeyboardButton("📝 Detailed Messages", callback_data="msg_detailed")],
        [InlineKeyboardButton("📄 Simple Messages", callback_data="msg_simple")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "💬 *Choose Message Type:*\n\n"
        "• *Detailed*: Professional violation descriptions\n"
        "• *Simple*: Basic report messages\n\n"
        "Select:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
    return MESSAGE_TYPE


async def message_type_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    user_id = update.effective_user.id
    user_sessions[user_id]['detailed'] = query.data == "msg_detailed"
    
    await query.edit_message_text(
        "⏳ *Starting report process...*\n\n"
        "Please wait while I authenticate and submit reports.\n"
        "This may take a moment...",
        parse_mode='Markdown'
    )
    
    await execute_reports(query, context)
    
    return ConversationHandler.END


async def execute_reports(query, context: ContextTypes.DEFAULT_TYPE):
    user_id = query.from_user.id
    session = user_sessions[user_id]
    
    api_id = session['api_id']
    api_hash = session['api_hash']
    phone = session['phone']
    target = session['target']
    count = session['count']
    detailed = session['detailed']
    mode = session['mode']
    
    try:
        session_name = f'bot_session_{user_id}'
        client = TelegramClient(session_name, api_id, api_hash)
        await client.connect()
        
        if not await client.is_user_authorized():
            await client.disconnect()
            await query.edit_message_text(
                "❌ *Authorization required!*\n\n"
                "Please use /start to authenticate first.",
                parse_mode='Markdown'
            )
            return
        
        if not target.startswith("@") and not target.isdigit():
            target = "@" + target
        
        if target.isdigit():
            entity = await client.get_entity(int(target))
        else:
            entity = await client.get_entity(target)
        
        await query.edit_message_text(
            f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"🎯 *TARGET LOCKED* 🎯\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"👤 *Name:* {getattr(entity, 'first_name', getattr(entity, 'title', 'Target'))}\n"
            f"📊 *Total Reports:* {count}\n"
            f"⚡️ *Status:* EXECUTING...\n\n"
            f"🔥 *Launching Report Sequence...*",
            parse_mode='Markdown'
        )
        
        successful = 0
        failed = 0
        
        if mode == 'mass':
            reason_keys = list(report_reasons.keys())
            
            for i in range(count):
                reason_choice = reason_keys[i % len(reason_keys)]
                reason_name, reason_obj = report_reasons[reason_choice]
                
                if detailed:
                    message = detailed_messages[reason_choice]
                else:
                    message = f"Reported for {reason_name}"
                
                try:
                    await client(
                        ReportPeerRequest(
                            peer=entity,
                            reason=reason_obj,
                            message=message
                        ))
                    successful += 1
                    
                    if (i + 1) % 10 == 0 or i == count - 1:
                        await query.edit_message_text(
                            f"⚡️ *MASS REPORT IN PROGRESS* ⚡️\n"
                            f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                            f"📊 Progress: [{i + 1}/{count}]\n"
                            f"✅ Success: {successful}\n"
                            f"❌ Failed: {failed}\n"
                            f"🎯 Current: {reason_name}\n"
                            f"━━━━━━━━━━━━━━━━━━━━━━━━━",
                            parse_mode='Markdown'
                        )
                    
                except Exception:
                    failed += 1
                
                await asyncio.sleep(2)
        else:
            reason_choice = session['reason']
            reason_name, reason_obj = report_reasons[reason_choice]
            
            for i in range(count):
                if detailed:
                    message = detailed_messages[reason_choice]
                else:
                    message = f"Reported for {reason_name}"
                
                try:
                    await client(
                        ReportPeerRequest(
                            peer=entity,
                            reason=reason_obj,
                            message=message
                        ))
                    successful += 1
                    
                    if (i + 1) % 10 == 0 or i == count - 1:
                        await query.edit_message_text(
                            f"📊 *Progress:* {i + 1}/{count}\n"
                            f"✅ Successful: {successful}\n"
                            f"❌ Failed: {failed}",
                            parse_mode='Markdown'
                        )
                    
                except Exception:
                    failed += 1
                
                await asyncio.sleep(2)
        
        await client.disconnect()
        
        keyboard = [
            [InlineKeyboardButton("🔄 Report Another", callback_data="mode_" + mode)],
            [InlineKeyboardButton("🏠 Back to Menu", callback_data="back_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            f"🎉 *MISSION COMPLETE!* 🎉\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"⚡️ *FINAL STATISTICS* ⚡️\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"📊 *Total Reports:* {count}\n"
            f"✅ *Successful:* {successful} 🔥\n"
            f"❌ *Failed:* {failed}\n"
            f"🎯 *Target:* {getattr(entity, 'first_name', getattr(entity, 'title', target))}\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"⚡️ *Powered by ED aka EREN* ⚡️\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
    except Exception as e:
        keyboard = [[InlineKeyboardButton("🔄 Try Again", callback_data="mode_" + mode)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            f"❌ *Error:* {str(e)}\n\n"
            "Please check your credentials and try again.",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )


async def back_to_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("🎯 Single Report Mode", callback_data="mode_single")],
        [InlineKeyboardButton("🚀 Mass Report Mode", callback_data="mode_mass")],
        [InlineKeyboardButton("⚙️ Change Credentials", callback_data="change_creds")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "🏠 *Main Menu*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🎯 *Select Reporting Mode:*",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
    return MODE_SELECT


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❌ Operation cancelled.\n"
        "Use /start to begin again."
    )
    return ConversationHandler.END


def main():
    bot_token = os.getenv('BOT_TOKEN')
    
    if not bot_token:
        print("❌ ERROR: BOT_TOKEN environment variable not set!")
        print("Please create a bot with @BotFather and set the BOT_TOKEN.")
        return
    
    application = Application.builder().token(bot_token).build()
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            API_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_api_id)],
            API_HASH: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_api_hash)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            VERIFICATION_CODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_verification_code)],
            MODE_SELECT: [
                CallbackQueryHandler(mode_selection, pattern="^mode_"),
                CallbackQueryHandler(mode_selection, pattern="^change_creds$"),
                CallbackQueryHandler(back_to_menu, pattern="^back_menu$")
            ],
            TARGET_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_target)],
            REASON_SELECT: [CallbackQueryHandler(reason_selection)],
            COUNT_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_count)],
            MESSAGE_TYPE: [CallbackQueryHandler(message_type_selection)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    
    application.add_handler(conv_handler)
    
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("⚡️  TELEGRAM REPORTER PRO BOT  ⚡️")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🎯 Status: ONLINE & READY")
    print("🔥 Mode: Advanced Reporting System")
    print("⚡️ Created by: ED aka EREN")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
