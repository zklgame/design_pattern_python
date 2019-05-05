class RemoteControl(object):

    def __init__(self):
        self.undo_command = None
        self.on_commands = []
        self.off_commands = []
        for _ in range(3):
            self.on_commands.append(None)
            self.off_commands.append(None)

    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_was_pushed(self, slot):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_was_pushed(self):
        self.undo_command.undo()

    def __str__(self):
        strs = []
        strs.append('---------- Remote Control ----------')
        for i in range(len(self.on_commands)):
            strs.append('slot %d: %s, %s' % (i + 1, type(self.on_commands[i]), type(self.off_commands[i])))
        strs.append('---------- END ----------')
        return '\n'.join(strs)
