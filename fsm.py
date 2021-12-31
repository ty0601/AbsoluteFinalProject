from linebot.models import ImageSendMessage
from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_read(self, event):
        text = event.message.text
        return text.lower() == "study"

    def is_going_to_play(self, event):
        text = event.message.text
        return text.lower() == "play"

    def is_going_to_reset(self, event):
        text = event.message.text
        return text.lower() == "reset"

    def is_going_to_fsm(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def on_enter_read1(self, event):
        print("I'm reading")

        reply_token = event.reply_token
        send_text_message(reply_token, "Study for two hours.")

    def on_enter_read2(self, event):
        print("I'm reading")

        reply_token = event.reply_token
        send_text_message(reply_token, "Study for two hours.")

    def on_enter_read3(self, event):
        print("I'm reading")

        reply_token = event.reply_token
        send_text_message(reply_token, "Study for two hours.")

    def on_enter_read4(self, event):
        print("I'm reading")

        reply_token = event.reply_token
        send_text_message(reply_token, "You need to take a break!")

    def on_enter_play1(self, event):
        print("I'm playing")

        reply_token = event.reply_token
        send_text_message(reply_token, "Play for two hours.")

    def on_enter_play2(self, event):
        print("I'm playing")

        reply_token = event.reply_token
        send_text_message(reply_token, "Play for two hours.")

    def on_enter_play3(self, event):
        print("I'm playing")

        reply_token = event.reply_token
        send_text_message(reply_token, "Play for two hours.")

    def on_enter_play4(self, event):
        print("I'm playing")

        reply_token = event.reply_token
        send_text_message(reply_token, "Don't play anymore!")


    def on_enter_fsm(self, event):
        print("I'm in fsm")

        reply_token = event.reply_token
        send_image_url(reply_token, )

