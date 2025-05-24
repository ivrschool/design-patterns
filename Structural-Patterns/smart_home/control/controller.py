class SmartHomeController:
    def __init__(self):
        self.devices = {}

    def register(self, name, device):
        self.devices[name] = device

    def execute(self, name, action):
        if name in self.devices:
            getattr(self.devices[name], action)()