import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
first_led = 7
second_led = 29
third_led = 31
fourth_led = 33
now = datetime.datetime.now()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


#LED first_led
GPIO.setup(first_led, GPIO.OUT)
GPIO.output(first_led, 0) #Off initially
#LED second_led
GPIO.setup(second_led, GPIO.OUT)
GPIO.output(second_led, 0) #Off initially
#LED third_led
GPIO.setup(third_led, GPIO.OUT)
GPIO.output(third_led, 0) #Off initially
##LED fourth_led
GPIO.setup(fourth_led, GPIO.OUT)
GPIO.output(fourth_led, 0) #Off initially

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received: %s' % command)
    if 'on' in command:
         message = "on"
         if 'first_led' in command:
             message = message + "first_led"
             GPIO.output(first_led, 1)
         if 'second_led' in command:
             message = message + "second_led"
             GPIO.output(second_led, 1)
         if 'third_led' in command:
             message = message + "third_led"
             GPIO.output(third_led, 1)
         if 'fourth_led' in command:
             message = message + "fourth_led"
             GPIO.output(fourth_led, 1)
         if 'all' in command:
             GPIO.output(first_led, 1)
             GPIO.output(second_led, 1)
             GPIO.output(third_led, 1)
             GPIO.output(fourth_led, 1)
             message = message + "light(s)"
             telegram_bot.sendMessage (chat_id, message)

    if 'off' in command:
        message = "off "
        if 'first_led' in command:
            message = message + "first_led"
            GPIO.output(first_led, 0)
        if 'second_led' in command:
            message = message + "second_led"
            GPIO.output(second_led, 0)
        if 'third_led' in command:
            message = message + "third_led"
            GPIO.output(third_led, 0)
        if 'fourth_led' in command:
            message = message + "fourth_led"
            GPIO.output(fourth_led, 0)
        if 'all' in command:
            message = message + "all"
            GPIO.output(first_led, 0)
            GPIO.output(second_led, 0)
            GPIO.output(third_led, 0)
            GPIO.output(fourth_led, 0)
            message = message + "light(s)"
            telegram_bot.sendMessage (chat_id, message)
telegram_bot = telepot.Bot('1993353550:AAHT4l_R0YXCsanE0MtOGLtMPy4mQEMMtY0')
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')
while 1:
    time.sleep(10)
