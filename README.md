<p align="center">
  <h1 align="center">🚀 CK AdBot</h1>
  <p align="center">
    <b>Telegram Automation Tool</b><br>
    by <b>cyberkallan</b>
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-blue">
  <img src="https://img.shields.io/badge/Language-Python-yellow">
  <img src="https://img.shields.io/badge/Telegram-Pyrogram-blue">
  <img src="https://img.shields.io/badge/Status-Stable-success">
</p>

---

## 🔥 Overview

**CK AdBot** is a premium, terminal-based Telegram automation tool built using **Pyrogram** and **asyncio**, featuring a **Telegram Bot Control Panel** and a **secure licence-based startup system**.

The tool is designed to work smoothly on **Linux, VPS, and Termux**, while allowing full Telegram group automation controlled directly from Telegram itself.

> ⚠️ This project is intended for educational and personal automation purposes only. Use responsibly and follow Telegram’s Terms of Service.

---

## ✨ Key Features

- 🔐 Licence-protected startup
- 🤖 Telegram bot control panel
- 📤 Broadcast custom messages to all joined groups
- 🔁 Forward last saved message automatically
- ➕ Join groups via invite link or username
- ➖ Leave all joined groups instantly
- 🛑 Emergency stop command
- 👑 Owner-only command execution
- ⚡ Async, fast, and FloodWait-safe
- 🖥️ Fully terminal & Termux friendly
- 🛡️ Stable and lightweight design

---

## 🧠 How CK AdBot Works

1. Run CK AdBot from terminal or Termux  
2. Enter a **valid licence key**  
3. The tool starts:
   - Telegram **user account session**
   - Telegram **bot control panel**
4. All automation is controlled via Telegram bot commands  
5. Messages are sent using your **Telegram user account**, not the bot

---

## 🔐 Licence Information

- CK AdBot requires a **valid licence key** to start
- Licence verification happens at tool startup
- If the key is invalid, the tool will exit automatically

📩 **To obtain a licence key, contact:**  
👉 **@imarjunarz on Instagram**

---

## 🛠️ Tech Stack

- Python 3.8+
- Pyrogram
- asyncio
- tgcrypto
- colorama

---

## 📦 Installation

### 🐧 Linux / VPS

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install pyrogram tgcrypto colorama

## Termux (Android)
Copy code
Bash
pkg update && pkg upgrade
pkg install python -y
pip install pyrogram tgcrypto colorama
Recommended Python version: 3.9 or higher

##🔑 Telegram Setup
1️⃣ Get Telegram API Credentials
Visit: https://my.telegram.org
Login → API development tools
Copy:
API ID
API Hash
2️⃣ Create Telegram Bot
Open @BotFather
Create a new bot
Copy the Bot Token
3️⃣ Get Your Telegram User ID
Use @userinfobot
Copy your numeric user ID
⚙️ Configuration
Edit the following values inside the script before running:
API_ID = YOUR_API_ID
API_HASH = "YOUR_API_HASH"

BOT_TOKEN = "YOUR_BOT_TOKEN"
OWNER_ID = YOUR_TELEGRAM_USER_ID

##🚀 Running CK AdBot
Copy code
Bash
python ck_adbot.py
Startup Flow
Copy code

CK AdBot by cyberkallan
Secure Automation Tool

##Enter Licence Key:
🤖 Telegram Bot Control Panel Commands
⚠️ Only the OWNER_ID can use these commands
📤 Broadcast Message
Copy code
Text
/broadcast Hello everyone!
🔁 Forward Saved Message
Copy code
Text
/forward
🛑 Stop Current Task
Copy code
Text
/stop
📊 Total Joined Groups
Copy code
Text
/groups
📡 Bot Status
Copy code
Text
/status
➕ Join Group
Copy code
Text
/join https://t.me/examplegroup
➖ Leave All Groups
Copy code
Text
/leaveall
##🛡️ Safety Guidelines
Start with small group counts
Maintain reasonable delays
Avoid spammy or repetitive content
Use /stop for emergency halt
Never share your API credentials or session files

