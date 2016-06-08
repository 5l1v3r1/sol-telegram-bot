#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from sol import get_akk
import credentials
import logging

TOKEN = credentials.secret_dict['bot_token']

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='For the remaining quato information, type: /akk')

def akk(bot, update):
    akk_info = get_akk() + " GB"
    #Yes, Superonline (Turkish ISP) offers 100GB per month as Fair Usage Quota (highest packages) in 2016.
    bot.sendMessage(update.message.chat_id, text=akk_info)

def no_command(bot, update):
    bot.sendMessage(update.message.chat_id, text="Undefined command. You can learn the commands with /help")

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("akk", akk))
    dp.add_handler(MessageHandler([Filters.text], no_command))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

