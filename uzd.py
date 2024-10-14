from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def get_summary(self):
        pass

class Fiction(Book):
    def get_summary(self):
        print(f'{self.title}{self.author}')

class NonFiction(Book):
    def get_summary(self):
        print(f'{self.title}{self.author}')

class Poetry(Book):
    pass

fiction_book = Fiction("Террор", "Дэн Симмонс")
nonfiction_book = NonFiction("Как писать книги", "Стивен Кинг")
fiction_book.get_summary()
nonfiction_book.get_summary()