import pytest

# класс BooksCollector, в котором реализован конструктор и методы
from main import BooksCollector

@pytest.fixture
# фикстура, которая создаёт коллекцию
def collector():
    collector = BooksCollector()

    return collector

@pytest.fixture
# фикстура, которая набор коллекции книг
def collector_full():
    collector = BooksCollector()
    collector.books_genre = {'The Fifth Element': 'Фантастика', 'Infinite': 'Фантастика',
                             'Jurassic Park': 'Фантастика', 'A Quiet Place': 'Ужасы', 'The Skeleton Key': 'Ужасы'}
    return collector