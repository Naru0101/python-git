from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest, ViberSubscribedRequest
import random

# Viber Bot Token
viber_token = '522f1d0665a7dd18-4666d49b9a38aa61-f6b1052001c9e54d'
bot_configuration = BotConfiguration(
    name='Baby Ichigo',
    auth_token=viber_token
)

# Initialize Viber API
viber = Api(bot_configuration)

# Rock, Paper, Scissors game logic
def play_rps(user_choice):
    choices = ['камень', 'ножницы', 'бумага']
    bot_choice = random.choice(choices)

    if user_choice == bot_choice:
        return f"Ничья! {user_choice}."
    elif (
        (user_choice == 'камень' and bot_choice == 'ножницы') or
        (user_choice == 'ножницы' and bot_choice == 'бумага') or
        (user_choice == 'бумага' and bot_choice == 'камень')
    ):
        return f"Вы выиграли! Вы выбрали {user_choice}, бот выбрал {bot_choice}."
    else:
        return f"Вы проиграли! Вы выбрали {user_choice}, бот выбрал {bot_choice}."

# Message handling
def handle_message(viber, message):
    text = message.text.lower()
    sender = message.sender.id

    if "бот" in text:
        response_text = "Привет! Я ваш лучший друг, бот. Чем могу помочь?"
    elif text in ['камень', 'ножницы', 'бумага']:
        response_text = play_rps(text)
    else:
        response_text = f"Привет, {text}! Это ваш бот."

    viber.send_messages(sender, [TextMessage(text=response_text)])

# Subscription handling
def handle_subscription(viber, request):
    user_id = request.user.id
    welcome_text = "Добро пожаловать! Я бот. Напишите что-нибудь."

    viber.send_messages(user_id, [TextMessage(text=welcome_text)])

# Set up handlers
viber.set_webhook('https://invite.viber.com/?g2=AQBalMRQsRLwhlIY7EY7o%2Fg5x1ZRmvBGdHMCDKJMJ%2FFDhvqN2eyqoaJYqDT6sMYG')
viber.set_message_handler(handle_message)
viber.set_subscribe_handler(handle_subscription)

if __name__ == "__main__":
    viber.start_polling()
