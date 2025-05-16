# factories/document_factory.py
from models.document import Document

class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == "HR":
            return Document(title="HR Onboarding", body="Welcome!", footer="HR Dept")
        elif doc_type == "Finance":
            return Document(title="Finance Report", body="Balance sheet...", footer="Confidential")
        elif doc_type == "Marketing":
            return Document(title="Campaign Plan", body="Q4 strategy", footer="Marketing Use Only")
        else:
            raise ValueError("Unknown document type")
