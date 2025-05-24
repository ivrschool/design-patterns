class DeviceBuilder:
    def __init__(self):
        self.device = {}

    def add_light(self, light_type):
        self.device["light"] = light_type
        return self

    def add_camera(self, cam_type):
        self.device["camera"] = cam_type
        return self

    def build(self):
        return self.device