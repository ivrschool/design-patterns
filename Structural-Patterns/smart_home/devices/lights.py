class Light:
    def on(self):
        print("Light turned ON")
    def off(self):
        print("Light turned OFF")

class LightDecorator:
    def __init__(self, light):
        self.light = light
    def on(self):
        self.light.on()
    def off(self):
        self.light.off()

class BlinkingLight(LightDecorator):
    def on(self):
        print("Light is blinking now.")
        self.light.on()