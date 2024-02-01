import json
import xml.etree.ElementTree as ElTree


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookDisplay:
    def display(self, book: Book) -> None:
        raise NotImplementedError


class ConsoleBookDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseBookDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class BookPrinter:
    def print_book(self, book: Book) -> None:
        raise NotImplementedError


class ConsoleBookPrinter(BookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseBookPrinter(BookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class BookSerializer:
    def serialize(self, book: Book) -> str:
        raise NotImplementedError


class JsonBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = ElTree.Element("book")
        title = ElTree.SubElement(root, "title")
        title.text = book.title
        content = ElTree.SubElement(root, "content")
        content.text = book.content
        return ElTree.tostring(root, encoding="unicode")


class DisplayFactory:
    @staticmethod
    def create(method_type: str) -> BookDisplay:
        if method_type == "console":
            return ConsoleBookDisplay()
        elif method_type == "reverse":
            return ReverseBookDisplay()
        else:
            raise ValueError(f"Unknown display type: {method_type}")


class PrintFactory:
    @staticmethod
    def create(method_type: str) -> BookPrinter:
        if method_type == "console":
            return ConsoleBookPrinter()
        elif method_type == "reverse":
            return ReverseBookPrinter()
        else:
            raise ValueError(f"Unknown print type: {method_type}")


class SerializeFactory:
    @staticmethod
    def create(method_type: str) -> BookSerializer:
        if method_type == "json":
            return JsonBookSerializer()
        elif method_type == "xml":
            return XmlBookSerializer()
        else:
            raise ValueError(f"Unknown serialize type: {method_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display = DisplayFactory.create(method_type)
            display.display(book)
        elif cmd == "print":
            printer = PrintFactory.create(method_type)
            printer.print_book(book)
        elif cmd == "serialize":
            serializer = SerializeFactory.create(method_type)
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
