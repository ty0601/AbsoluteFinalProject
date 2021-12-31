from transitions.extensions import GraphMachine

from utils import send_text_message


# class TocMachine(GraphMachine):
#     def __init__(self, **machine_configs):
#         self.machine = GraphMachine(model=self, **machine_configs)
#
#     def is_going_to_read(self, event):
#         text = event.message.text
#         return text.lower() == "study"
#
#     def is_going_to_play(self, event):
#         text = event.message.text
#         return text.lower() == "play"
#
#     def is_going_to_reset(self, event):
#         text = event.message.text
#         return text.lower() == "reset"
#
#     def on_enter_to_read1(self, event):
#         print("I'm reading")
#
#         reply_token = event.reply_token
#         send_text_message(reply_token, "Study for two hours.")
#
#     def on_enter_to_read2(self, event):
#         print("I'm reading")
#
#         reply_token = event.reply_token
#         send_text_message(reply_token, "Study for two hours.")
#
#     def on_enter_to_read3(self, event):
#         print("I'm reading")
#
#         reply_token = event.reply_token
#         send_text_message(reply_token, "Study for two hours.")
#
#     def on_enter_to_read4(self, event):
#         print("I'm reading")
#
#         reply_token = event.reply_token
#         send_text_message(reply_token, "You need to take a break!")
#
#     def on_enter_to_play1(self, event):
#         print("I'm playing")
#
#         reply_token = event.reply_token
#         send_text_message(reply_token, "Play for two hours.")
#
#     def on_enter_to_play2(self, event):
#         print("I'm playing")
#
#         reply_token = event.reply_token
#         send_text_message(reply_token, "Play for two hours.")
#
#     def on_enter_to_play3(self, event):
#         print("I'm playing")
#
#         reply_token = event.reply_token
#         send_text_message(reply_token, "Play for two hours.")
#
#     def on_enter_to_play4(self, event):
#         print("I'm playing")
#
#         reply_token = event.reply_token
#         send_text_message(reply_token, "Don't play anymore!")
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_play(self, event):
        text = event.message.text
        return text.lower() == "play"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_to_play1(self, event):
        print("I'm playing")

        reply_token = event.reply_token
        send_text_message(reply_token, "Play for two hours.")

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")