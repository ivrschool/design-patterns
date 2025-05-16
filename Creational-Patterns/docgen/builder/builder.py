# builder/builder.py
from models.document import Document

class DocumentBuilder:
    def __init__(self):
        self.doc = Document()

    def set_title(self, title):
        self.doc.title = title
        return self

    def set_body(self, body):
        self.doc.body = body
        return self

    def set_footer(self, footer):
        self.doc.footer = footer
        return self

    def apply_theme(self, theme):
        self.doc.style = {
            "background": theme.background(),
            "font": theme.font()
        }
        return self

    def build(self):
        return self.doc
