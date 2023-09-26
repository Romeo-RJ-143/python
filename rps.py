import asyncio
from random import choice
from pyrogram import filters, Client
from pyrogram.types import Message
from Romeo import *

win_lst = []

# Function to determine the winner
def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "draw"
    elif (
        (user_choice == "rock" and bot_choice == "scissors") or
        (user_choice == "paper" and bot_choice == "rock") or
        (user_choice == "scissors" and bot_choice == "paper")
    ):
        return "player"
    else:
        return "computer"

# check who is the winner 
def check_winner(win_lst):
    player = win_lst.count("player")
    draw = win_lst.count("draw")
    computer = win_lst.count("computer")
    if player > computer:
        return "player"
    elif computer > player:
        return "computer"
    else:
        return "draw"


@Client.on_message(filters.command(["Rps", "rps"], ["/", "!", "."]))
async def rps(client: Client, message: Message):
    await message.reply_text(f"write one of this (rock, paper, scissors)")
    user = message.from_user.id
    userr = await client.get_users(message.from_user.id)
    player = f"[{userr.first_name}](tg://user?id={userr.id})"
    Romeo = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    rounds = int(Romeo[0])
  
    async for i in range(rounds):
        user_choice = await client.message.text.lower()
        bot_choice = random.choice(["rock", "paper", "scissors"])

        result = await client.determine_winner(user_choice, bot_choice)
        await client.message.reply_text(f"You chose {user_choice}.\nI chose {bot_choice}.\n{result}")
        win_lst.append(result)
 
    final_result = await client.check_winner()
    await message.reply_text(f"{final_result} win the game ")
          


                 




from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Define states for conversation
CHOOSING, PLAYING = range(2)

# Initialize a dictionary to store user data
user_data = {}

# Function to start the game
def start(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    context.user_data['username'] = user.username
    update.message.reply_text(f"Hi, {user.username}! Let's play Rock, Paper, Scissors. Choose your move: Rock, Paper, or Scissors.")
    return CHOOSING

# Function to play the game
def play(update: Update, context: CallbackContext) -> int:
    user_choice = update.message.text.lower()
    bot_choice = random.choice(["rock", "paper", "scissors"])

    result = determine_winner(user_choice, bot_choice)

    update.message.reply_text(f"You chose {user_choice}.\nI chose {bot_choice}.\n{result}")

    return CHOOSING

# Function to determine the winner
def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and bot_choice == "scissors") or
        (user_choice == "paper" and bot_choice == "rock") or
        (user_choice == "scissors" and bot_choice == "paper")
    ):
        return "You win!"
    else:
        return "I win!"

# Function to cancel the game
def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Game canceled.")
    return ConversationHandler.END

def main():
    # Initialize the Telegram bot
    updater = Updater(token="YOUR_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    # Create a conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING: [MessageHandler(Filters.text & ~Filters.command, play)],
            PLAYING: [CommandHandler("cancel", cancel)],
        },
        fallbacks=[],
    )

    dp.add_handler(conv_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
      
