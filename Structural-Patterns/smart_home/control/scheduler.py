class Command:
    def execute(self):
        pass

class DeviceCommand(Command):
    def __init__(self, device, action):
        self.device = device
        self.action = action
    def execute(self):
        getattr(self.device, self.action)()

class GroupCommand(Command):
    def __init__(self):
        self.commands = []
    def add(self, command):
        self.commands.append(command)
    def execute(self):
        for cmd in self.commands:
            cmd.execute()