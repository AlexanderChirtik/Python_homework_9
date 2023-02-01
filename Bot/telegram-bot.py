from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token('6097300120:AAHFvb4fJKug5bqXd76RAWtmxqaTfpprNUs').build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('Server srarts')

app.run_polling()