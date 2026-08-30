import os
import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n\n"
        "🤖 من ربات هوشمند تشخیص الگوی بازار هستم.\n\n"
        "📊 فعلاً در مرحله آزمایشی هستیم.\n"
        "یک عکس از نمودار طلا برای من بفرست."
    )


async def receive_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ عکس نمودار دریافت شد.\n\n"
        "📸 تصویر با موفقیت به ربات رسید.\n\n"
        "🧠 در مرحله بعد، سیستم تشخیص الگو را به ربات اضافه می‌کنیم."
    )


async def run_bot():
    if not TOKEN:
        raise RuntimeError(
            "BOT_TOKEN environment variable is not set."
        )

    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        MessageHandler(
            filters.PHOTO,
            receive_photo
        )
    )

    await application.initialize()
    await application.start()

    if application.updater is None:
        raise RuntimeError("Telegram updater is not available.")

    await application.updater.start_polling()

    print("=================================")
    print("🤖 AI Pattern Bot is running!")
    print("=================================")

    try:
        while True:
            await asyncio.sleep(3600)

    except asyncio.CancelledError:
        pass

    finally:
        await application.updater.stop()
        await application.stop()
        await application.shutdown()


if __name__ == "__main__":
    asyncio.run(run_bot())
