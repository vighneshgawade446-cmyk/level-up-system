from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from database import init_db, create_user, get_user
TOKEN = "8888125390:AAFAYQyWgmAkMnhGLrn-PpgVQuqfknS4BM0"
NAME, AGE, HEIGHT, WEIGHT = range(4)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚔️ HUNTER REGISTRATION\n\nEnter your name:"
    )
    return NAME
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text
    await update.message.reply_text("Enter your age:")
    return AGE
async def get_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["age"] = update.message.text
    await update.message.reply_text("Enter your height (cm):")
    return HEIGHT
async def get_height(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["height"] = update.message.text
    await update.message.reply_text("Enter your weight (kg):")
    return WEIGHT
async def get_weight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["weight"] = update.message.text
    user_id = update.effective_user.id
    create_user(
        user_id,
        context.user_data["name"],
        context.user_data["age"],
        context.user_data["height"],
        context.user_data["weight"]
    )
    user = get_user(user_id)
    await update.message.reply_text(
        f"✅ REGISTRATION COMPLETE\n\n"
        f"Hunter: {user[1]}\n"
        f"Age: {user[2]}\n"
        f"Height: {user[3]} cm\n"
        f"Weight: {user[4]} kg\n\n"
        f"Rank: {user[5]}\n"
        f"Level: {user[6]}\n"
        f"Gold: {user[7]}"
    )
    return ConversationHandler.END
async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)
    if not user:
        await update.message.reply_text(
            "No profile found. Use /start to register."
        )
        return
    await update.message.reply_text(
        f"👤 HUNTER PROFILE\n\n"
        f"Hunter: {user[1]}\n"
        f"Age: {user[2]}\n"
        f"Height: {user[3]} cm\n"
        f"Weight: {user[4]} kg\n\n"
        f"Rank: {user[5]}\n"
        f"Level: {user[6]}\n"
        f"Gold: {user[7]}"
    )
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Registration cancelled.")
    return ConversationHandler.END
def main():
    init_db()
    app = Application.builder().token(TOKEN).build()
    registration_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_age)],
            HEIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_height)],
            WEIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_weight)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(registration_handler)
    app.add_handler(CommandHandler("profile", profile))
    print("Bot is running...")
    app.run_polling()
if __name__ == "__main__":
    main()
