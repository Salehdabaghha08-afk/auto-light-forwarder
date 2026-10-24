import os from telegram import Update from telegram.ext import Application, MessageHandler, ContextTypes, filters
TOKEN = os.environ["BOT_TOKEN"]
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE): message = update.channel_post if not message: return
# مقصدهای مجاز را بعداً اینجا تنظیم می‌کنیم.
print(f"New post received: {message.message_id}")
app = Application.builder().token(TOKEN).build() app.add_handler(MessageHandler(filters.ALL, forward_message)) app.run_polling()