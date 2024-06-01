import time
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop

# GPIO Pins for Lamps
LAMPU_PINS = [5, 7, 8, 12, 13, 16, 17, 18, 19, 20]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up GPIO pins
for pin in LAMPU_PINS:
    GPIO.setup(pin, GPIO.OUT)

# Action function to handle Telegram messages
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].lower()

    if 'start' in command:
        telegram_bot.sendMessage(chat_id, "Hi, I am your house!\nAll commands you can see in /help\nIf you want to know who I am, see /you")

    elif 'help' in command:
        message = "I\'m Smarthouse v1.\nYou can send me these commands:\n"
        for i in range(1, 11):
            message += f"/on_lampu{i} /off_lampu{i} - Control lampu {i}\n"
        message += "/on_all /off_all - Control semua lampu\n"
        telegram_bot.sendMessage(chat_id, message)

    elif 'you' in command:
        message = "I'M Smarthouse v1 with Raspberry Pi B+\nDeveloped by Smarthouse Nusantara\nInstagram: @smarthousenusantara"
        telegram_bot.sendMessage(chat_id, message)

    elif 'on' in command or 'off' in command:
        action = GPIO.HIGH if 'on' in command else GPIO.LOW
        message = "Turned " + ("on" if action == GPIO.HIGH else "off") + " "

        if 'all' in command:
            for pin in LAMPU_PINS:
                GPIO.output(pin, action)
            message += "all lamps"
        else:
            for i in range(1, 11):
                if f'lampu{i}' in command:
                    GPIO.output(LAMPU_PINS[i-1], action)
                    message += f"lampu {i} "
        
        telegram_bot.sendMessage(chat_id, message.strip())

# Initialize Telegram bot
telegram_bot = telepot.Bot('6596*****6:AAEuM5DfO91p13********')
print(telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print('Up and Running...')

while True:
    time.sleep(10)
