import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load environment variables from .env file
load_dotenv()

# Fetch sensitive data from environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')



# Your bot code here...

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if a parameter was passed (like /start 12345)
    if context.args:
        video_id = context.args[0]  # The first argument after /start
        try:
            # Use copy_message to send the video without the forward tag
            await context.bot.copy_message(
                chat_id=update.effective_chat.id,  # Send to the user
                from_chat_id=CHANNEL_ID,           # From your private channel
                message_id=int(video_id)           # The video message ID in the channel
            )

            # Optionally send a confirmation message
            await update.message.reply_text("Here is the video you requested.")
        except Exception as e:
            await update.message.reply_text(f"Error: {str(e)}")
    else:
        await update.message.reply_text("Welcome! Please provide a valid video link.")

def main():
    # Set up the bot with the Application class
    application = Application.builder().token(BOT_TOKEN).build()

    # Handle the /start command
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()