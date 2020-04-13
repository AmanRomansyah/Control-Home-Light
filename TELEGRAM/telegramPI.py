import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
from time import sleep

#GPIO PIN
LAMPU1 = 5
LAMPU2 = 7
LAMPU3 = 8
LAMPU4 = 12
LAMPU5 = 13
LAMPU6 = 16
LAMPU7 = 17
LAMPU8 = 18
LAMPU9 = 19
LAMPU10 = 20
#SENSOR_PINTU = 18
#PIR_SENSOR = 19
#LED_MODULE = 20
#Arduino = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LAMPU1, GPIO.OUT)
GPIO.setup(LAMPU2, GPIO.OUT)
GPIO.setup(LAMPU3, GPIO.OUT)
GPIO.setup(LAMPU4, GPIO.OUT)
GPIO.setup(LAMPU5, GPIO.OUT)
GPIO.setup(LAMPU6, GPIO.OUT)
GPIO.setup(LAMPU7, GPIO.OUT)
GPIO.setup(LAMPU8, GPIO.OUT)
GPIO.setup(LAMPU9, GPIO.OUT)
GPIO.setup(LAMPU10, GPIO.OUT)

#GPIO.setup(SENSOR_PINTU, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(PIR_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(LED_MODULE, GPIO.OUT)
#GPIO.setup(Arduino, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def action(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	if 'start' in command:
		message = "Hi, I am your house!\n all commands you can see in /help \n If you want to know who I am see in /you"
		telegram_bot.sendMessage (chat_id, message)

	if 'help' in command:
		message = " I \' m Smarthouse v1. \n"\
			"You can send me such commands:\n"\
			"/on_lampu1 /off_lampu1 - Control lampu 1\n"\
			"/on_lampu2 /off_lampu2 - Control lampu 2\n"\
			"/on_lampu3 /off_lampu3 - Control lampu 3\n"\
			"/on_lampu4 /off_lampu4 - Control lampu 4\n"\
			"/on_lampu5 /off_lampu5 - Control lampu 5\n"\
			"/on_lampu6 /off_lampu6 - Control lampu 6\n"\
			"/on_lampu7 /off_lampu7 - Control lampu 7\n"\
			"/on_lampu8 /off_lampu8 - Control lampu 8\n"\
			"/on_lampu9 /off_lampu9 - Control lampu 9\n"\
			"/on_lampu10 /off_lampu10 - Control lampu 10\n"\
			"/on_all    /off_all	- Control semua lampu\n\n"
		telegram_bot.sendMessage (chat_id, message)
	if 'you' in command:
		message = " I'M Smarthouse v1 with Raspberry pi B+ \n"\
			"Developed by Smarthouse Nusantara \n"\
			"instagram = @smarthousenusantara \n"
		telegram_bot.sendMessage (chat_id, message)

	if 'on' in command:
		message = "Turned on "
		if 'lampu1' in command:
			message = message + "lampu 1 "
			GPIO.output(LAMPU1, 1)
		if 'lampu2' in command:
			message = message + "lampu 2 "
			GPIO.output(LAMPU2, 1)
		if 'lampu3' in command:
			message = message + "lampu 3 "
			GPIO.output(LAMPU3, 1)
		if 'lampu4' in command:
			message = message + "lampu 4 "
			GPIO.output(LAMPU4, 1)
		if 'lampu5' in command:
			message = message + "lampu 5 "
			GPIO.output(LAMPU5, 1)
		if 'lampu6' in command:
			message = message + "lampu 6 "
			GPIO.output(LAMPU6, 1)
		if 'lampu7' in command:
			message = message + "lampu 7 "
			GPIO.output(LAMPU7, 1)
		if 'lampu8' in command:
			message = message + "lampu 8 "
			GPIO.output(LAMPU8, 1)
		if 'lampu9' in command:
			message = message + "lampu 9 "
			GPIO.output(LAMPU9, 1)
		if 'lampu10' in command:
			message = message + "lampu 10 "
			GPIO.output(LAMPU10, 1)
		if 'all' in command:
			message = message + "all "
			GPIO.output(LAMPU1, 1)
			GPIO.output(LAMPU2, 1)
			GPIO.output(LAMPU3, 1)
			GPIO.output(LAMPU4, 1)
			GPIO.output(LAMPU5, 1)
			GPIO.output(LAMPU6, 1)
			GPIO.output(LAMPU7, 1)
			GPIO.output(LAMPU8, 1)
			GPIO.output(LAMPU9, 1)
			GPIO.output(LAMPU10, 1)
		message = message + ""
		telegram_bot.sendMessage (chat_id, message)

	if 'off' in command:
		message = "Turned off "
		if 'lampu1' in command:
			message = message + "lampu 1 "
			GPIO.output(LAMPU1, 0)
		if 'lampu2' in command:
			message = message + "lampu 2 "
			GPIO.output(LAMPU2, 0)
		if 'lampu3' in command:
			message = message + "lampu 3 "
			GPIO.output(LAMPU3, 0)
		if 'lampu4' in command:
			message = message + "lampu 4 "
			GPIO.output(LAMPU4, 0)
		if 'lampu5' in command:
			message = message + "lampu 5 "
			GPIO.output(LAMPU5, 0)
		if 'lampu6' in command:
			message = message + "lampu 6 "
			GPIO.output(LAMPU6, 0)
		if 'lampu7' in command:
			message = message + "lampu 7 "
			GPIO.output(LAMPU7, 0)
		if 'lampu8' in command:
			message = message + "lampu 8 "
			GPIO.output(LAMPU8, 0)
		if 'lampu9' in command:
			message = message + "lampu 9 "
			GPIO.output(LAMPU9, 0)
		if 'lampu10' in command:
			message = message + "lampu 10 "
			GPIO.output(LAMPU10, 0)
		if 'all' in command:
			message = message + "all "
			GPIO.output(LAMPU1, 0)
			GPIO.output(LAMPU2, 0)
			GPIO.output(LAMPU3, 0)
			GPIO.output(LAMPU4, 0)
			GPIO.output(LAMPU5, 0)
			GPIO.output(LAMPU6, 0)
			GPIO.output(LAMPU7, 0)
			GPIO.output(LAMPU8, 0)
			GPIO.output(LAMPU9, 0)
			GPIO.output(LAMPU10, 0)
		message = message + ""
		telegram_bot.sendMessage (chat_id, message)

#	if GPIO.input(SENSOR_PINTU) == False:
#		message="pintu tertutup"
#		telegram_bot.sendMessage(id, message)
#	else:
#		message="pintu terbuka"
#		telegram_bot.sendMessage(id, message)
#	if GPIO.input(Arduino) == False:
#		message="Asap/gas terdeteksi"
#		telegram_bot.sendMessage(id, message)
#	else:
#		message="Asap/gas tak terdeteksi"
#		telegram_bot.sendMessage(id, message)

telegram_bot = telepot.Bot('659612696:AAEuM5DfO91p13ADLE37CSOpoGfVdqSDP7I')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')


while 1:
    time.sleep(10)



