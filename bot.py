import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import sqlite3
import os

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 数据库路径
db_path = os.path.join(os.path.dirname(__file__), 'templates', 'database', 'accounting.db')

# 你的 Telegram Bot Token
YOUR_BOT_TOKEN = "7803509610:AAHU6Vf4ufRZEkby7w0g2P_SVqXxerJ7OH8"

# 开始命令
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("欢迎使用记账机器人！输入 '+' 来记录收入，输入 '-' 来记录支出。")

# 处理用户消息
async def record(update: Update, context: CallbackContext) -> None:
    message = update.message.text
    if message.startswith('+') or message.startswith('-'):
        try:
            amount = float(message[1:])
            record_type = '收入' if message.startswith('+') else '支出'
            user_name = update.message.from_user.username

            # 插入到数据库
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("INSERT INTO records (amount, time, user_name) VALUES (?, ?, ?)",
                      (amount, update.message.date, user_name))
            conn.commit()
            conn.close()

            await update.message.reply_text(f"记录成功: {record_type} {amount}元")
        except ValueError:
            await update.message.reply_text("无效的金额，请输入正确的金额格式。")
    else:
        await update.message.reply_text("请输入以 '+' 或 '-' 开头的金额。")

# 设置 Telegram Bot
def main():
    application = Application.builder().token(YOUR_BOT_TOKEN).build()

    # 添加命令和消息处理器
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, record))

    # 启动 Bot
    application.run_polling()

if __name__ == '__main__':
    main()
