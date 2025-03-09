from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_one_book_book_added(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        #добавляем книгу
        collector.add_new_book('The Shawshank Redemption')
        # проверяем, что добавилось именно одна книга
        assert len(collector.books_genre) == 1

    def test_set_book_genre_set_genre_genre_added(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        #добавляем книгу
        collector.add_new_book('The Shawshank Redemption')
        collector.set_book_genre('The Shawshank Redemption', 'Фантастика')
        # проверяем, что добавился жанр
        assert collector.books_genre['The Shawshank Redemption'] == 'Фантастика'
