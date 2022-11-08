import pyautogui as pt
import pyperclip as pc
from time import sleep
from bot_responses import response

class Whatsapp:
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

# navigate through the whatsapp web to the green dots for new message and click on it
    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen("greendot.png", confidence=.7)
            pt.moveTo(position[0:2], duration = self.speed)
            pt.moveRel(-100,0, duration = self.speed)
            pt.doubleClick(interval = self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot):', e)

# navigate to our message input box and click on it
    def nav_message_box(self):
        try:
            position = pt.locateOnScreen("paperclip.png", confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 15, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_message_box):', e)

# navigate to the last message
    def nav_message(self):
        try:
            position = pt.locateOnScreen("paperclip.png", confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(60, -50, duration=self.speed)
        except Exception as e:
            print('Exception (nav_message):', e)

# copy the last message that we want to process
    def get_message(self):
        pt.tripleClick(interval = self.click_speed)
        sleep(self.speed)
        pt.rightClick(interval = self.click_speed)
        sleep(self.speed)
        pt.moveRel(12, 15, duration = self.speed)
        pt.click(interval = self.click_speed)
        sleep(1)

        self.message = pc.paste()
        print('User said:', self.message)

# process the message and send the response
    def send_message(self, response):
        try:
            if self.message != self.last_message:
                bot_response = response(self.message)
                print('Bot said:', bot_response)
                pt.typewrite(bot_response, interval = .1)
                pt.typewrite('\n', interval = .1)

                self.last_message = self.message
            else:
                print('Bot said:', 'I have already responded to that message.')

        except Exception as e:
            print('Exception (send_message):', e)

# close response box
    def close_response_box(self):
        try:
            position = pt.locateOnScreen("x.png", confidence=.7)
            pt.moveTo(position[0:2], duration = self.speed)
            pt.moveRel(18, 10, duration = self.speed)
            pt.click(interval = self.click_speed)

        except Exception as e:
            print('Exception (close_response_box):', e)

wa_bot = Whatsapp(speed=.5, click_speed=.4)
sleep(2)

while True:
    wa_bot.close_response_box()
    wa_bot.nav_green_dot()
    wa_bot.nav_message_box()
    wa_bot.close_response_box()
    wa_bot.nav_message()
    wa_bot.close_response_box()
    wa_bot.get_message()
    wa_bot.send_message(response)

    sleep(5)
