from abc import ABC, abstractmethod


class Document(ABC):
    """Абстрактний базовий клас для документів."""

    @abstractmethod
    def print(self) -> None:
        """Абстрактний метод, який повинен реалізувати кожен тип документа."""
        pass

    def prepare_for_printing(self) -> None:
        """Реалізований метод, який готує документ і викликає абстрактний друк."""
        print(f"[Підготовка] Форматування та перевірка макету для {self.__class__.__name__}...")
        self.print()



class PDFDocument(Document):
    def print(self) -> None:
        print("🖨️ [Друк] Рендеринг та друк сторінок файлу PDF.")


class WordDocument(Document):
    def print(self) -> None:
        print("🖨️ [Друк] Друк тексту та розмітки документа Word (.docx).")


class ExcelDocument(Document):
    def print(self) -> None:
        print("🖨️ [Друк] Друк таблиць та діаграм документа Excel (.xlsx).")



class DocumentFactory:
    @staticmethod
    def create_document(doc_type: str) -> Document:
        """Фабричний метод для створення об'єктів документів за їхнім типом."""
        target = doc_type.strip().lower()
        
        if target == "pdf":
            return PDFDocument()
        elif target == "word":
            return WordDocument()
        elif target == "excel":
            return ExcelDocument()
        else:
            raise ValueError(f"Невідомий тип документа: '{doc_type}'")


if __name__ == "__main__":
    types_to_create = ["pdf", "word", "excel"]
    
    print("=== Робота через Фабричний метод ===\n")
    
    for t in types_to_create:
        doc = DocumentFactory.create_document(t)
        
        doc.prepare_for_printing()
        print()
