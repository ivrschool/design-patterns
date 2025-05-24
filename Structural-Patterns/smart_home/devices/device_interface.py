class DeviceInterface:
    def on(self):
        pass
    def off(self):
        pass

class SmartLight(DeviceInterface):
    def on(self):
        print("Smart Light ON")
    def off(self):
        print("Smart Light OFF")