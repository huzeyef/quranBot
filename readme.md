# 📖 Quran Bot

A simple and efficient Telegram bot built with Python to help users explore chapters of the Qur'an using the [Quran.com API](https://quran.com).

Created with ❤️ by [@huzeyef](https://github.com/huzeyef)

---

## ✨ Features

- `/start` — Get a welcome message with usage instructions.
- `/getallchapters` — Get a full list of all 114 Surahs (Qur'anic chapters).
- `/getchapterinfo <chapter_id>` — Get detailed info about any Surah by ID (1–114).
- `/users` — (Owner only) View the number of users who used the bot.
- `/id` — Get your Telegram user ID.

---

## 📦 Setup Instructions

### 🔧 Prerequisites

- Python 3.10 or later
- A Telegram bot token from [BotFather](https://t.me/BotFather)

### 📁 Installation

1. **Clone the repository**

```bash
git clone https://github.com/huzeyef/quran-bot.git
cd quran-bot
Install the required packages

bash
Copy
Edit
pip install -r requirements.txt
Create a config.json file

In the root directory, create a file called config.json and add the following:

json
Copy
Edit
{
  "token": "YOUR_TELEGRAM_BOT_TOKEN",
  "bot-owner-id": YOUR_TELEGRAM_USER_ID
}
Replace "YOUR_TELEGRAM_BOT_TOKEN" with your actual Telegram bot token and "YOUR_TELEGRAM_USER_ID" with your own Telegram user ID.

Run the bot

bash
Copy
Edit
python main.py
📋 Example Commands
/getchapterinfo 1 — Get info about Surah Al-Fatihah

/getchapterinfo 114 — Get info about Surah An-Nas

/getallchapters — Lists all Surah names

/id — Get your Telegram ID

/users — Bot owner command to count users

👤 Author
GitHub: @huzeyef

Telegram: @hhuuzzz1

Please don't forget to make Du'a for the developer 🙏
