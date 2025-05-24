class UIDashboard:
    def send_command(self, cmd):
        print(f"[UI] Executing command: {cmd}")

class DashboardAdapter:
    def __init__(self, ui_dashboard, controller):
        self.ui = ui_dashboard
        self.controller = controller

    def click_button(self, device_name, action):
        self.ui.send_command(f"{device_name} -> {action}")
        self.controller.execute(device_name, action)