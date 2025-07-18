# 📖 Quran Bot

A simple and efficient Telegram bot built with Python to help users explore chapters of the Qur'an using the [Quran.com API](https://quran.com). Created with ❤️ by [@huzeyef](https://github.com/huzeyef)

To install the bot locally, clone the repository and install the dependencies:

```bash
git clone https://github.com/huzeyef/quran-bot.git
cd quran-bot
pip install -r requirements.txt
```
Before running the bot, create a config.json file in the root directory of the project with the following content:

```json
{
  "token": "YOUR_BOT_TOKEN",
  "bot-owner-id": "YOUR_TELEGRAM_ID"
}
```
Replace YOUR_BOT_TOKEN with your bot’s token from BotFather, and YOUR_TELEGRAM_ID with your personal Telegram numeric user ID.

Then run the bot using:

```python
python main.py
```
Once the bot is running, you can interact with it on Telegram. Here are the available commands:

/start — Shows a welcome message and instructions for using the bot.

/getallchapters — Displays a list of all Qur'anic chapter names (Surahs).

/getchapterinfo <chapter_id> — Shows detailed information for a given chapter ID, such as:

Surah name

Revelation place

Verse count

Revelation order

Page range

English translation name
Example: /getchapterinfo 1 will return information about Surah Al-Fatihah.

/id — Returns your Telegram user ID.

/users — (Owner only) Shows how many users have interacted with the bot.

This bot is made for educational purposes and to ease Quran study and navigation. You’re encouraged to improve it or deploy your own copy.

Made with sincerity. If you find it useful, please remember to make Du'a for the developer 🙏
Contact: @hhuuzzz1 | GitHub: @huzeyef
