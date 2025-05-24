from control.controller import SmartHomeController
from devices.lights import Light
from control.logging_proxy import LoggingProxy
from control.scheduler import DeviceCommand, GroupCommand

controller = SmartHomeController()
light = LoggingProxy(Light())
controller.register("hall_light", light)

controller.execute("hall_light", "on")

group = GroupCommand()
group.add(DeviceCommand(light, "off"))
group.execute()