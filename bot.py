from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

API_TOKEN = "8689338536:AAGHD_BfRvzlqW6yC0k_8d_9Yi3_V7PVUAU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام محمد! رباتت فعاله ✅")

app = ApplicationBuilder().token(API_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
