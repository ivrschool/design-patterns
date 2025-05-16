# main.py

from config.logger import Logger
from factories.document_factory import DocumentFactory
from factories.document_factory_method import HRDocumentCreator, FinanceDocumentCreator, MarketingDocumentCreator
from factories.theme_factory import ThemeFactory
from builder.builder import DocumentBuilder
from models.document import Document

# -------------------------------
# 1. Singleton: Logger
# -------------------------------
logger = Logger()
logger.log("=== Singleton Pattern ===")
logger.log("Logger initialized. This will be shared across the app.\n")

# -------------------------------
# 2. Factory Pattern: Static Factory
# -------------------------------
logger.log("=== Factory Pattern ===")
doc = DocumentFactory.create_document("HR")
logger.log("Generated HR document using static factory.")
doc.show()

# -------------------------------
# 3. Factory Method Pattern
# -------------------------------
logger.log("=== Factory Method Pattern ===")
creator = FinanceDocumentCreator()
finance_doc = creator.create_document()
logger.log("Generated Finance document using Factory Method.")
finance_doc.show()

# -------------------------------
# 4. Abstract Factory Pattern
# -------------------------------
logger.log("=== Abstract Factory Pattern ===")
theme = ThemeFactory.get_theme("dark")
logger.log(f"Applying theme - background: {theme.background()}, font: {theme.font()}.\n")

# -------------------------------
# 5. Builder Pattern
# -------------------------------
logger.log("=== Builder Pattern ===")
builder = DocumentBuilder()
custom_doc = (builder.set_title("Custom Marketing Plan")
                      .set_body("Marketing strategy for Q1")
                      .set_footer("Internal Use Only")
                      .apply_theme(theme)
                      .build())
logger.log("Built a custom marketing document using Builder.")
custom_doc.show()

# -------------------------------
# 6. Prototype Pattern
# -------------------------------
logger.log("=== Prototype Pattern ===")
cloned_doc = custom_doc.clone()
cloned_doc.title = "Cloned: Marketing Plan Copy"
logger.log("Cloned the custom marketing document using Prototype.")
cloned_doc.show()
