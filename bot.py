import os
import time
import requests
from telegram.ext import Updater, CommandHandler

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
FACEBOOK_ACCOUNTS = [
    "https://www.facebook.com/tamer.mohmed.5245/",
    "https://www.facebook.com/hmam.shkry.2025/",
    "https://www.facebook.com/makram.mahros.2025/",
    "https://www.facebook.com/haitham.ezz.422249/",
]

def start(update, context):
    update.message.reply_text("✅ البوت شغال وبيتابع الحسابات")

def check_facebook():
    posts = []
    for acc in FACEBOOK_ACCOUNTS:
        try:
            res = requests.get(acc)
            posts.append(f"📌 متابعة {acc} - آخر تحديث {time.ctime()}")
        except Exception as e:
            posts.append(f"❌ مشكلة مع {acc}: {e}")
    return posts

def loop_check(context):
    posts = check_facebook()
    for post in posts:
        context.bot.send_message(chat_id=CHAT_ID, text=post)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    job = updater.job_queue
    job.run_repeating(loop_check, interval=30, first=5)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
