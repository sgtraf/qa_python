from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_one_book_book_added(self, collector):
        #добавляем книгу
        collector.add_new_book('The Shawshank Redemption')
        # проверяем, что добавилось именно одна книга
        assert len(collector.books_genre) == 1

    def test_set_book_genre_book_genre_genre_added(self, collector):
        #добавляем книгу
        collector.add_new_book('The Shawshank Redemption')
        #устанавливаем жанр
        collector.set_book_genre('The Shawshank Redemption', 'Фантастика')
        #проверяем, что добавился жанр
        assert collector.books_genre['The Shawshank Redemption'] == 'Фантастика'

    def test_get_book_genre_book_genre_genre_get(self, collector):
        #добавляем книгу
        collector.add_new_book('The Shawshank Redemption')
        #устанавливаем жанр
        collector.set_book_genre('The Shawshank Redemption', 'Фантастика')
        #проверяем, что добавился жанр
        assert collector.books_genre.get('The Shawshank Redemption') == 'Фантастика'

    def test_get_books_with_specific_genre_book_genre_specific_books(self, collector_full):
        books_fantasy =[]
        books_fantasy = collector_full.get_books_with_specific_genre('Фантастика')
        #проверяем, что добавился жанр
        assert collector_full.books_genre.get(books_fantasy[0]) == 'Фантастика'