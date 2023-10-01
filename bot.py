import logging
import requests
from telegram import Update
from telegram.ext import  CommandHandler,  ContextTypes, ApplicationBuilder
import json


# API base 
url = "https://api.quran.com/api/v4/"
with open('config.json', 'r') as cfg:
    data = json.load(cfg)





# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

def is_bot_owner(userid):
    return userid == data['bot-owner-id']

user_ids =[]
async def id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in user_ids:
        user_ids.append(user_id)
    await context.bot.sendMessage(chat_id=update.effective_user.id, text=f"Hello, your user ID ({user_id}) has been added!")

async def users(update:Update, context:ContextTypes.DEFAULT_TYPE):
    uID = update.effective_user.id
    if is_bot_owner(uID):
        await update.message.reply_text(f'you are the owner\n you have {len(user_ids)} bot users ')
    else:
        await update.message.reply_text('sorry you dont have permiission to access this command!!')
# Function to get all chapters
async def get_all_chapters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(url + 'chapters')
    if response.status_code == 200:
        data = response.json()
        chapter_names = [chapter['name_simple'] for chapter in data['chapters']]
        chapters_list = '\n'.join(chapter_names)
        await update.message.reply_text("List of Quranic chapters:\n" + chapters_list)
    else:
        await update.message.reply_text(f"Request failed with status code: {response.status_code}")




async def get_detail_of_a_single_chapter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='Please insert id  like this /getChapterInfo <chapter_id>.\n Example\n/getChapterInfo 1 ',reply_to_message_id=True)
        
    else:
        response = requests.get(url + f'chapters/{context.args[0]}/')
        if response.status_code == 200:
            data = response.json()
            x = data['chapter']
            detail = [
                x['revelation_place'],
                x['revelation_order'],
                x['name_simple'],
                x['name_arabic'],
                x['verses_count'],
                x['pages'],
                x['translated_name']['name']
            ]
            info2 = f'''
Surah name: {detail[2]}
Revelation place: {detail[0]}
Verses count: {detail[4]}
Revelation order: {detail[1]}
Pages: {detail[5]}
English name: {detail[6]}    
            '''
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                    text=info2,reply_to_message_id=True)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                    text=f"Request failed with status code: {response.status_code}")

# Handler for /getAllChapters command
allChapters = CommandHandler("getAllChapters", get_all_chapters)

# Handler for /getChapterInfo command
chapterInfo = CommandHandler("getChapterInfo", get_detail_of_a_single_chapter)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
     text=('''
Welcome to the Quran Bot! This bot is designed to help you access information about Quranic chapters quickly and easily.
You can use the following commands to interact with the bot:

/start - Get started with the Quran Bot.

This command will provide you with a brief welcome message and instructions on how to use the bot.
The bot is designed to make it easier for you to explore and learn about the Quranic chapters.

/getAllChapters - Get a list of all Quranic chapters.

This command will provide you with a list of the names of all the chapters in the Quran.

/getChapterInfo <chapter_id> - Get detailed information about a specific Quranic chapter.

Replace <chapter_id> with the ID of the chapter you want to learn more about. 
For example, 
/getChapterInfo 1 
The above command will provide details about Surah Al-Fatihah.You can type any chapter ID from 1 to 114 to get details about a specific chapter.
You can use this command to retrieve information such as the revelation place, revelation order, number of verses, number of pages, and English name of the selected chapter.

Enjoy your experience with the Quran Bot, and if you have any questions or suggestions, do not hesitate to contact me @hhuuzzz1
Also don't forget to make Du'a for me 🙏     
     '''))

st = CommandHandler("start", start)
i_d = CommandHandler("id", id)
userS= CommandHandler("users", users)

if __name__ == '__main__':
    token = data['token']
    application = ApplicationBuilder().token(token).build()

    
    
    application.add_handler(st)
    application.add_handler(allChapters)
    application.add_handler(chapterInfo)
    application.add_handler(i_d)
    application.add_handler(userS)

    application.run_polling()
