import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "من ربات تشخیص الگوی بازار هستم 🤖📊\n\n"
        "یک عکس از نمودار برای من بفرست."
    )


async def receive_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ عکس دریافت شد!\n\n"
        "در مرحله بعد، موتور تشخیص الگو را به من اضافه می‌کنیم."
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, receive_photo))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
