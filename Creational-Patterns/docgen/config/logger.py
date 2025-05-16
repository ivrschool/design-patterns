# config/logger.py
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"[LOG]: {message}")
