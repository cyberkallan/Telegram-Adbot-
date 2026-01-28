"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 CK AdBot v3.2
 Telegram Bot Control Panel
 Author : cyberkallan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import asyncio
from pyrogram import Client, filters, idle
from pyrogram.errors import FloodWait
from colorama import Fore, Style, init

# ──────────────────────────────
# INIT
# ──────────────────────────────
init(autoreset=True)

# ──────────────────────────────
# LICENCE CONFIG
# ──────────────────────────────
LICENSE_KEY = "ARJUNARZ123"
MAX_ATTEMPTS = 3

# ──────────────────────────────
# TELEGRAM CONFIG (EDIT THESE)
# ──────────────────────────────
API_ID = 123456          # your api id
API_HASH = "API_HASH"    # your api hash

BOT_TOKEN = "BOT_TOKEN" # telegram bot token
OWNER_ID = 123456789    # your telegram user id

SESSION_NAME = "ck_adbot_user"

DELAYS = {
    "message": 3,
    "group": 6,
}

# ──────────────────────────────
running = False

# CLIENTS
user = Client(SESSION_NAME, API_ID, API_HASH)
bot = Client("ck_adbot_bot", bot_token=BOT_TOKEN)

# ──────────────────────────────
# LICENCE LOGIN
# ──────────────────────────────
def license_login():
    print(Fore.CYAN + Style.BRIGHT + "\n🔐 CK AdBot Licence Verification\n")

    for _ in range(MAX_ATTEMPTS):
        key = input("Enter Licence Key: ").strip()

        if key == LICENSE_KEY:
            print(Fore.GREEN + "✅ Licence verified. Access granted.\n")
            return True
        else:
            print(
                Fore.RED
                + "❌ Invalid key.\n"
                + "Please contact: @imarjuarz on Instagram for a valid licence key.\n"
            )

    print(Fore.RED + "Too many failed attempts. Exiting.")
    return False

# ──────────────────────────────
# HELPERS
# ──────────────────────────────
async def get_groups():
    groups = []
    async for dialog in user.get_dialogs():
        if dialog.chat.id < 0:
            groups.append(dialog.chat.id)
    return groups


async def broadcast(text=None):
    global running
    groups = await get_groups()

    for gid in groups:
        if not running:
            break

        try:
            if text:
                await user.send_message(gid, text)
            else:
                async for msg in user.get_chat_history("me", limit=1):
                    await user.forward_messages(gid, "me", msg.id)

            await asyncio.sleep(DELAYS["message"])

        except FloodWait as fw:
            await asyncio.sleep(fw.value)
            continue

        except Exception:
            continue

        await asyncio.sleep(DELAYS["group"])

# ──────────────────────────────
# BOT COMMANDS (OWNER ONLY)
# ──────────────────────────────
@bot.on_message(filters.command("start") & filters.user(OWNER_ID))
async def start_cmd(_, m):
    await m.reply(
        "🤖 **CK AdBot Control Panel**\n\n"
        "/broadcast <text>\n"
        "/forward\n"
        "/stop\n"
        "/groups\n"
        "/status\n"
        "/join <link>\n"
        "/leaveall"
    )


@bot.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_cmd(_, m):
    global running

    if len(m.command) < 2:
        await m.reply("❌ Usage: /broadcast <message>")
        return

    text = m.text.split(maxsplit=1)[1]
    running = True

    await m.reply("🚀 Broadcasting started")
    await broadcast(text)

    running = False
    await m.reply("✅ Broadcasting completed")


@bot.on_message(filters.command("forward") & filters.user(OWNER_ID))
async def forward_cmd(_, m):
    global running
    running = True

    await m.reply("📤 Forwarding saved message")
    await broadcast()

    running = False
    await m.reply("✅ Forward completed")


@bot.on_message(filters.command("stop") & filters.user(OWNER_ID))
async def stop_cmd(_, m):
    global running
    running = False
    await m.reply("🛑 All tasks stopped")


@bot.on_message(filters.command("groups") & filters.user(OWNER_ID))
async def groups_cmd(_, m):
    groups = await get_groups()
    await m.reply(f"📊 Total joined groups: {len(groups)}")


@bot.on_message(filters.command("status") & filters.user(OWNER_ID))
async def status_cmd(_, m):
    await m.reply(f"🟢 Running: {running}")


@bot.on_message(filters.command("join") & filters.user(OWNER_ID))
async def join_cmd(_, m):
    if len(m.command) < 2:
        await m.reply("❌ Usage: /join <link or username>")
        return

    link = m.text.split(maxsplit=1)[1]

    try:
        await user.join_chat(link)
        await m.reply("➕ Joined successfully")
    except Exception as e:
        await m.reply(f"❌ Join failed: {e}")


@bot.on_message(filters.command("leaveall") & filters.user(OWNER_ID))
async def leaveall_cmd(_, m):
    groups = await get_groups()

    for gid in groups:
        try:
            await user.leave_chat(gid)
            await asyncio.sleep(2)
        except Exception:
            continue

    await m.reply("👋 Left all groups")

# ──────────────────────────────
# RUN
# ──────────────────────────────
async def main():
    await user.start()
    await bot.start()

    print(Fore.GREEN + Style.BRIGHT + "CK AdBot Control Panel is LIVE")

    await idle()


if __name__ == "__main__":
    print(Fore.CYAN + Style.BRIGHT + """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   CK AdBot by cyberkallan
   Secure Automation Tool
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    if license_login():
        asyncio.run(main())
