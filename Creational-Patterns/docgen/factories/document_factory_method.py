# factories/document_factory_method.py
from abc import ABC, abstractmethod
from models.document import Document

# Abstract Creator
class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self):
        pass

# Concrete Creators
class HRDocumentCreator(DocumentCreator):
    def create_document(self):
        return Document(title="HR Policy", body="Welcome to the company!", footer="HR Department")

class FinanceDocumentCreator(DocumentCreator):
    def create_document(self):
        return Document(title="Q1 Finance Report", body="Balance & Revenue", footer="Finance Department")

class MarketingDocumentCreator(DocumentCreator):
    def create_document(self):
        return Document(title="Marketing Strategy", body="Social media plan", footer="Marketing Team")
