import asyncio
from random import choice
from pyrogram import filters, Client
from pyrogram.types import Message

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

# Check who is the winner
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
    while True:
        round_input = (await message.reply_text("Enter how many rounds you want to play between 3 and 9:")).text.lower()
        try:
            rounds = int(round_input)
            if rounds % 2 == 1 and 3 <= rounds <= 9:
                break
            else:
                await message.reply_text("Please enter an odd number between 3 and 9.")
        except ValueError:
            await message.reply_text("Invalid input. Please enter an odd number between 3 and 9.")

    for _ in range(rounds):
        user_choice = (await message.reply_text("Enter your choice -\n\nOne of these:\n(rock, paper, scissors)")).text.lower()
        bot_choice = choice(["rock", "paper", "scissors"])

        result = determine_winner(user_choice, bot_choice)
        await message.reply_text(f"You chose **{user_choice}**.\nComputer chose **{bot_choice}**.\n\n**{result}** wins this round")
        win_lst.append(result)

    final_result = check_winner(win_lst)
    if final_result == "player":
        user_id = message.from_user.id
        userr = await client.get_users(user_id)
        mention = f"[{userr.first_name}](tg://user?id={user_id})"
        await message.reply_text(f"{mention} wins the game")
    elif final_result == "computer":
        await message.reply_text("**Computer** wins the game")
    else:
        await message.reply_text("It's a draw!")
                 




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
      
