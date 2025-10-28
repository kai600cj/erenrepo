from telethon import TelegramClient
from telethon.tl.functions.account import ReportPeerRequest
from telethon.tl.types import (
    InputReportReasonSpam, InputReportReasonFake, InputReportReasonViolence,
    InputReportReasonPornography, InputReportReasonChildAbuse,
    InputReportReasonCopyright, InputReportReasonIllegalDrugs,
    InputReportReasonPersonalDetails, InputReportReasonOther, InputPeerUser)
import asyncio
import sys
import os
from termcolor import colored

api_id = os.getenv('API_ID', '')
api_hash = os.getenv('API_HASH', '')

if not api_id or not api_hash:
    print(colored("ERROR: API credentials not set!", "red"))
    print(colored("Please set API_ID and API_HASH in Replit Secrets.", "yellow"))
    sys.exit(1)

try:
    api_id = int(api_id)
except ValueError:
    print(colored("ERROR: API_ID must be a number!", "red"))
    print(colored("Please set API_ID in Replit Secrets.", "yellow"))
    sys.exit(1)

print(colored("\n⚡️ REPORTER PRO ⚡️", "cyan", attrs=["bold"]))
print(colored("🔥 by ED aka EREN\n", "yellow"))
print(colored("📱 Phone number (e.g., +1234567890):", "cyan"))
phone_number = input(colored("> ", "red")).strip()

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
    1:
    "This account is causing disruption and violating community guidelines through inappropriate behavior that negatively impacts other users.",
    2:
    "This account appears to be involved in highly disturbing content related to child abuse. Such content is unacceptable and violates global laws. Immediate investigation and action are needed.",
    3:
    "The user is promoting violent threats and aggressive content. They have threatened members in chats and continue to spread harmful ideology that could lead to real-world consequences. Immediate moderation is needed.",
    4:
    "This account is promoting the sale of illegal goods including drugs and other prohibited substances. This violates Telegram's terms of service and poses serious legal risks.",
    5:
    "User is actively sharing pornographic, NSFW, and sexually explicit content in both public and private Telegram spaces. This behavior is dangerous for the community and against the platform's policy.",
    6:
    "This account is sharing personal and private information of individuals without consent, which constitutes doxxing and harassment. This puts people at risk.",
    7:
    "This account is promoting terrorist ideology, violent extremism, and threatening content that poses a serious security risk to communities and individuals.",
    8:
    "This user is sending repeated spam messages across multiple groups and private chats, disturbing many users and flooding conversations unnecessarily. Please take action immediately to protect users from constant spam abuse.",
    9:
    "This account is violating copyright laws by sharing copyrighted content without permission from the original creators. This infringes on intellectual property rights.",
    10:
    "The user is impersonating others and sharing false information to scam and mislead people. Many users have been affected by this fake identity. Telegram must take immediate steps.",
    11:
    "The account is continuously misusing the platform by harassing others, spreading hate speech, and causing disturbance. It needs to be reported under other serious violations."
}


def check_exit(input_value):
    if input_value.lower() == "exit":
        print(colored("⚡️ Exiting... [Created by ED aka EREN] ⚡️", "red"))
        sys.exit()


def check_home(input_value):
    return input_value.lower() == "home"


def get_valid_input(prompt, valid_options=None):
    while True:
        user_input = input(colored(prompt, "red"))
        check_exit(user_input)
        if check_home(user_input):
            return "home"
        if valid_options:
            try:
                user_input = int(user_input)
                if user_input in valid_options:
                    return user_input
                else:
                    print(
                        colored(
                            f"Please select a valid option from {valid_options}.",
                            "red"))
            except ValueError:
                print(colored("Invalid input. Please enter a number.", "red"))
        else:
            return user_input


def get_valid_integer_input(prompt, max_val=None):
    while True:
        user_input = input(colored(prompt, "red"))
        check_exit(user_input)
        if check_home(user_input):
            return "home"
        try:
            num = int(user_input)
            if max_val and num > max_val:
                print(
                    colored(
                        f"Maximum value is {max_val}. Please enter a smaller number.",
                        "yellow"))
                continue
            return num
        except ValueError:
            print(
                colored("Invalid input. Please enter a valid integer.", "red"))


async def mass_report_mode(client):
    print(
        colored("\n⚡️ === MASS REPORT MODE (Auto-Cycling) === ⚡️",
                "cyan",
                attrs=["bold"]))
    print(
        colored(
            "🔥 This mode will automatically cycle through ALL 11 report reasons",
            "yellow"))
    print()

    target = input(
        colored("Enter target username or ID (e.g., @username or user_id): ",
                "red"))
    check_exit(target)

    if not target.startswith("@") and not target.isdigit():
        target = "@" + target

    print()

    try:
        if target.isdigit():
            entity = await client.get_entity(int(target))
        else:
            entity = await client.get_entity(target)

        print(
            colored(
                f"🎯 Target Found: {entity.first_name if hasattr(entity, 'first_name') else entity.title} | ID: {entity.id}",
                "green"))
    except Exception as e:
        print(colored(f"❌ Error retrieving entity: {e}", "red"))
        return

    print()
    num_reports = get_valid_integer_input(
        colored("How many total reports to submit? (Recommended: 50-500): ",
                "red"))
    if num_reports == "home":
        return

    print()
    use_detailed = input(
        colored("Use detailed violation messages? (y/n): ",
                "red")).lower().strip()
    detailed = use_detailed == 'y'

    target_name = entity.first_name if hasattr(entity, 'first_name') else entity.title
    
    print(colored("\n━━━━━━━━━━━━━━━━━━━━━━━━━", "cyan"))
    print(colored("🎯 TARGET LOCKED 🎯", "cyan", attrs=["bold"]))
    print(colored("━━━━━━━━━━━━━━━━━━━━━━━━━\n", "cyan"))
    print(colored(f"👤 Name: {target_name}", "yellow"))
    print(colored(f"📊 Total Reports: {num_reports}", "yellow"))
    print(colored(f"⚡️ Status: EXECUTING...\n", "red", attrs=["bold"]))
    print(colored("🔥 Launching Report Sequence...\n", "green"))

    reason_keys = list(report_reasons.keys())
    successful = 0
    failed = 0

    for i in range(num_reports):
        reason_choice = reason_keys[i % len(reason_keys)]
        reason_name, reason_obj = report_reasons[reason_choice]

        if detailed:
            message = detailed_messages[reason_choice]
        else:
            message = f"Reported for {reason_name}"

        try:
            await client(
                ReportPeerRequest(peer=entity,
                                  reason=reason_obj,
                                  message=message))
            successful += 1
            print(colored(f"⚡️ [{successful}/{num_reports}] ✅ Sent | {reason_name}", "green"))
        except Exception as e:
            failed += 1
            print(colored(f"❌ [{i + 1}/{num_reports}] Failed: {str(e)[:30]}...", "red"))

        await asyncio.sleep(2)

    print()
    print(colored("━━━━━━━━━━━━━━━━━━━━━━━━━", "cyan"))
    print(colored("🎉 MISSION COMPLETE! 🎉", "cyan", attrs=["bold"]))
    print(colored("━━━━━━━━━━━━━━━━━━━━━━━━━", "cyan"))
    print(colored(f"✅ Successful: {successful} 🔥", "green"))
    print(colored(f"❌ Failed: {failed}", "red"))
    print(colored("━━━━━━━━━━━━━━━━━━━━━━━━━", "cyan"))
    print(colored("⚡️ by ED aka EREN ⚡️", "yellow", attrs=["bold"]))


async def single_report_mode(client):
    while True:
        print(
            colored("\n🎯 === SINGLE REPORT MODE (Manual) === 🎯",
                    "cyan",
                    attrs=["bold"]))
        print(
            colored(
                "1: Account\n2: Channel\n3: Group\n4: Bot\n5: Post Link (Channel/Group Only)",
                "green"))
        report_type = get_valid_input("What you want to report: ",
                                      valid_options=[1, 2, 3, 4, 5])

        if report_type == "home":
            return

        print()

        if report_type == 5:
            while True:
                post_link = input(
                    colored(
                        "Enter the full post link (e.g., https://t.me/channel/12345): ",
                        "red"))
                check_exit(post_link)
                if check_home(post_link):
                    break
                print()

                if not post_link.startswith("https://t.me/"):
                    print(
                        colored(
                            "You can only report a post link. Please provide a valid link.\n",
                            "red"))
                    continue

                try:
                    parts = post_link.replace("https://t.me/", "").split("/")
                    if len(parts) != 2 or not parts[1].isdigit():
                        print(
                            colored(
                                "Invalid post link format. Please provide a valid link.\n",
                                "red"))
                        continue

                    channel_username = parts[0]
                    message_id = int(parts[1])

                    channel = await client.get_entity(channel_username)

                    print(colored("\nReasons:", "green"))
                    for number, (reason_name, _) in report_reasons.items():
                        print(f"{number}: {reason_name}")
                    print()
                    reason_choice = get_valid_input(
                        colored("Enter the number for the reason: ", "red"),
                        valid_options=report_reasons.keys())
                    if reason_choice == "home":
                        break

                    print()

                    use_detailed = input(
                        colored("Use detailed violation message? (y/n): ",
                                "red")).lower().strip()
                    detailed = use_detailed == 'y'

                    print()

                    num_reports = get_valid_integer_input(
                        colored("How many reports to submit? ", "red"))
                    if num_reports == "home":
                        break

                    print()

                    for i in range(num_reports):
                        if detailed:
                            message = detailed_messages[reason_choice]
                        else:
                            message = f"Reported post ID {message_id} for {report_reasons[reason_choice][0]}"

                        await client(
                            ReportPeerRequest(
                                peer=channel,
                                reason=report_reasons[reason_choice][1],
                                message=message))
                        print(
                            colored(
                                f"✅ Report {i + 1} submitted successfully! 🔥",
                                "green"))
                        await asyncio.sleep(2)

                    print(
                        colored(
                            "\n🎉 All reports sent successfully! 🔥 [ED aka EREN]",
                            "green"))
                    break
                except Exception as e:
                    print(colored(f"Error retrieving entity: {e}\n", "red"))
                    continue

        else:
            entity_username = input(
                colored("Enter the username or ID (e.g., @username): ", "red"))
            check_exit(entity_username)
            if check_home(entity_username):
                break
            print()

            if not entity_username.startswith(
                    "@") and not entity_username.isdigit():
                entity_username = "@" + entity_username

            try:
                if entity_username.isdigit():
                    entity = await client.get_entity(int(entity_username))
                else:
                    entity = await client.get_entity(entity_username)
            except Exception as e:
                print(colored(f"Error retrieving entity: {e}\n", "red"))
                continue

            print(colored("\nReasons:", "green"))
            for number, (reason_name, _) in report_reasons.items():
                print(f"{number}: {reason_name}")
            print()

            reason_choice = get_valid_input(
                colored("Enter the number for the reason: ", "red"),
                valid_options=report_reasons.keys())
            if reason_choice == "home":
                continue

            print()

            use_detailed = input(
                colored("Use detailed violation message? (y/n): ",
                        "red")).lower().strip()
            detailed = use_detailed == 'y'

            print()

            num_reports = get_valid_integer_input(
                colored("How many reports to submit? ", "red"))
            if num_reports == "home":
                continue

            print()

            try:
                for i in range(num_reports):
                    if detailed:
                        message = detailed_messages[reason_choice]
                    else:
                        message = f"Reported for {report_reasons[reason_choice][0]}"

                    await client(
                        ReportPeerRequest(
                            peer=entity,
                            reason=report_reasons[reason_choice][1],
                            message=message))
                    print(
                        colored(f"⚡️ Report {i + 1} successfully submitted! ✅",
                                "green"))
                    await asyncio.sleep(2)
                print(
                    colored(
                        "\n🎉 All reports sent successfully! 🔥 [ED aka EREN]",
                        "green"))
            except Exception as e:
                print(colored(f"Error during reporting: {e}", "red"))

        choice = input(colored("\nReport another? (y/n): ",
                               "red")).lower().strip()
        if choice != 'y':
            break


async def main_menu(client):
    while True:
        print(colored("\n━━━━━━━━━━━━━━━━━━━━━━━━", "cyan"))
        print(colored("⚡️ REPORTER PRO ⚡️", "cyan", attrs=["bold"]))
        print(colored("━━━━━━━━━━━━━━━━━━━━━━━━\n", "cyan"))
        print(colored("1: 🎯 Single Report", "green"))
        print(colored("2: 🔥 Mass Report", "green"))
        print(colored("3: 🚪 Exit\n", "red"))

        mode = get_valid_input("Choice: ", valid_options=[1, 2, 3])

        if mode == 1:
            await single_report_mode(client)
        elif mode == 2:
            await mass_report_mode(client)
        elif mode == 3:
            print(colored("\n⚡️ Goodbye!", "cyan"))
            await client.disconnect()
            sys.exit(0)


def code_callback():
    print(colored("\n📱 Verification code sent to your Telegram!", "yellow"))
    print(colored("⚠️ IMPORTANT: Enter code WITH SPACES between digits", "red", attrs=["bold"]))
    print(colored("Example: If code is 88888, enter: 8 8 8 8 8\n", "yellow"))
    code = input(colored("Enter verification code with spaces: ", "red"))
    return code.replace(' ', '')

async def main():
    client = TelegramClient('report_session', api_id, api_hash)
    await client.start(phone_number, code_callback=code_callback)
    print(colored("\n✅ Logged in! ⚡️\n", "green", attrs=["bold"]))
    await main_menu(client)


if __name__ == "__main__":
    asyncio.run(main())
