import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

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
        #заполнем коллекцию данными
        books_fantasy = collector_full.get_books_with_specific_genre('Фантастика')
        #проверяем, что выводятся книги нужного жанра
        is_true = True
        for item in books_fantasy:
            if collector_full.books_genre[item] != 'Фантастика':
                is_true = False
        assert is_true

    def test_get_books_genre_collecor_books_genre(self, collector_full):
        books_genre = {}
        #заполнем коллекцию данными
        books_genre = collector_full.books_genre
        #проверяем, что выводятся книги нужного жанра
        assert collector_full.get_books_genre() == books_genre

    def test_get_books_for_children_collecor_books_for_children(self, collector_full):
        books_for_children =[]
        #заполнем коллекцию данными
        books_for_children = collector_full.get_books_for_children()
        #проверяем, что выводятся книги нужного жанра
        is_true = True
        for item in books_for_children:
            if collector_full.books_genre.get(item) == 'Ужасы' or collector_full.books_genre[item] == 'Детективы':
                is_true = False
        assert is_true

    def test_add_book_in_favorites_books_book_in_favorites(self, collector):
        #добавляем книгу
        collector.add_new_book('The Shawshank Redemption')
        #добавляем книгу в избранное
        collector.add_book_in_favorites('The Shawshank Redemption')

        assert collector.favorites[0] == 'The Shawshank Redemption'

    def test_delete_book_from_favorites_books_book_not_in_favorites(self, collector):
        #добавляем книгу
        collector.add_new_book('The Shawshank Redemption')
        # добавляем книгу в избранное
        collector.add_book_in_favorites('The Shawshank Redemption')
        # удаляем книгу из избранного
        collector.delete_book_from_favorites('The Shawshank Redemption')

        assert collector.favorites == []

    def test_get_list_of_favorites_books_collector_book_in_favorites(self, collector):
        #добавляем книгу
        collector.add_new_book('The Shawshank Redemption')
        # добавляем книгу в избранное
        collector.add_book_in_favorites('The Shawshank Redemption')

        assert collector.favorites == collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name', ['Ghjhjhjhdhdhdhfhfjfjjk kfkdkdkdkdkskskdkfgk', 'The Shawshank Redemption'] )
    def test_add_new_book_add_negative_input_book_not_added(self, name, collector):
        #добавляем книгу
        collector.add_new_book('The Shawshank Redemption')
        collector.add_new_book(name)
        # проверяем, что добавилось именно одна книга
        assert len(collector.books_genre) == 1