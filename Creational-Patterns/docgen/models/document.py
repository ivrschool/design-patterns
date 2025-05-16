# models/document.py
from prototype.cloneable import Cloneable

class Document(Cloneable):
    def __init__(self, title="", body="", footer="", style=None):
        self.title = title
        self.body = body
        self.footer = footer
        self.style = style or {}

    def show(self):
        print("=== DOCUMENT ===")
        print(f"Title: {self.title}")
        print(f"Body: {self.body}")
        print(f"Footer: {self.footer}")
        print(f"Style: {self.style}")
        print("================\n")
