def start(update, context):
  return update.message.reply_text("How do u do fellow kids?")

def help(update, context):
  message = """
  The following commands are available:

  /start -> Welcome Message
  /help -> Display Available commands
  """
  return update.message.reply_text(message)

def handle_message(update, context):
  return update.message.reply_text(f"Echo {update.message.text}")