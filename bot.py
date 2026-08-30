
import os
import asyncio
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
        "فعلاً عکس را دریافت کردم.\n"
        "در مرحله بعد موتور هوشمند تشخیص الگو را اضافه می‌کنیم."
    )


async def run_bot():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, receive_photo))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    print("Bot is running...")

    try:
        while True:
            await asyncio.sleep(3600)
    finally:
        await app.updater.stop()
        await app.stop()
        await app.shutdown()


if __name__ == "__main__":
    asyncio.run(run_bot())
