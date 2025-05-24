class LoggingProxy:
    def __init__(self, device):
        self.device = device
    def on(self):
        print(f"[LOG] {self.device.__class__.__name__} -> on")
        self.device.on()
    def off(self):
        print(f"[LOG] {self.device.__class__.__name__} -> off")
        self.device.off()