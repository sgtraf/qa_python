import pytest

# класс BooksCollector, в котором реализован конструктор и методы
from main import BooksCollector

@pytest.fixture # фикстура, которая создаёт коллекцию
def collector():
    collector = BooksCollector()

    return collector