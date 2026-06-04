from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8888125390:AAGbM5SGGm6Lmx4Omgy6Hr_7bAb2pPnroGY"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚔️ Welcome to Level Up System!\n\nHunter registration will be added soon."
    )

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👤 Hunter Profile\n\nRank: E\nLevel: 1\nGold: 0"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("profile", profile))

    print("Bot is running...")

    app.run_polling()

if __name__ == "__main__":
    main()
