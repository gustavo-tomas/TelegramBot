def start(update, context):
  return update.message.reply_text(
    text="How do u do fellow kids?\nType `/help` to see available commands",
    parse_mode='MarkdownV2')

def help(update, context):
  message = """
  The following commands are available:

  /start \-\> Welcome Message
  /help \-\> Display available commands
  /poke `chat_id` \-\> Poke user with specified id
  """
  return update.message.reply_text(message, parse_mode='MarkdownV2')

def poke(update, context):
  if len(context.args) <= 0 or context.args[0] != context.args[0]:
    return update.message.reply_text('Please specify a valid id')
  print("Poking " + context.args[0])
  try:
    context.bot.sendMessage(chat_id=context.args[0], text="Hewwo :)")
  except:
    update.message.reply_text('Failed to poke user ' + context.args[0])
  finally:  
    return 
  
def handle_message(update, context):
  return update.message.reply_text(f"Echo {update.message.text}")