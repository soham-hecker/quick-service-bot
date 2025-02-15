import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        video_id = context.args[0]  # The first argument after /start
        try:
            # Use copy_message to send the video without the forward tag
            await context.bot.copy_message(
                chat_id=update.effective_chat.id,  # Send to the user
                from_chat_id=CHANNEL_ID,           # From your private channel
                message_id=int(video_id)           # The video message ID in the channel
            )
            
            await update.message.reply_text("Here is the video you requested.")
        except Exception as e:
            await update.message.reply_text(f"Error: {str(e)}")
    else:
        await update.message.reply_text("Welcome! Please provide a valid video link.")

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == '__main__':
    main()
