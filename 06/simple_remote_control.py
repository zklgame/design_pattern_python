class SimpleRemoteControl(object):

    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def button_was_pressed(self):
        self.command.execute()
