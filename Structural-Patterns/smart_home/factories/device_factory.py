from devices.device_interface import SmartLight
from devices.security_camera import SecurityCamera

class DeviceFactory:
    def create_light(self):
        return SmartLight()
    def create_camera(self):
        return SecurityCamera()