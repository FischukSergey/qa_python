import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем
# наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # фикстура для создания экземпляра BooksCollector
    @pytest.fixture
    def collector(self):
        return BooksCollector()

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating,
        # имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный
    # экземпляр класса BooksCollector()

    # Тест 1: Проверка успешного добавления новой книги с названием
    # длиной не более 40 символов (валидное значение)
    def test_add_new_book_book_added_successfully(self, collector):
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.get_books_genre()

    # Тест 2: Параметризованный тест для добавления книг с невалидными
    # названиями (пустая строка и строка длиной более 40 символов)
    @pytest.mark.parametrize(
        "book_name",
        ["", "012345678901234567890123456789012345678901"],
    )
    def test_add_new_book_invalid_length_book_names(
        self, book_name, collector
    ):
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    # Тест 3: Проверка, что одну книгу нельзя добавить дважды
    def test_add_new_book_same_book_cannot_be_added_twice(self, collector):
        collector.add_new_book("Мастер и Маргарита")
        collector.add_new_book("Мастер и Маргарита")
        assert len(collector.get_books_genre()) == 1

    # Тест 4: Проверка, что у добавленной книги нет жанра
    def test_add_new_book_no_genre(self, collector):
        collector.add_new_book("Мастер и Маргарита")
        assert collector.get_book_genre("Мастер и Маргарита") == ""

    # Тест 5: Проверка, что у книги можно установить жанр
    def test_set_book_genre_set_genre_for_existing_book(self, collector):
        name = "Дюна"
        genre = "Фантастика"
        collector.books_genre = {name: ""}
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    # Тест 6: Получение списка книг определенного жанра
    def test_get_books_with_specific_genre_returns_books_of_genre(
        self, collector
    ):
        expected_books = {
            "Дюна": "Фантастика",
            "Ночной дозор": "Фантастика",
            "Шерлок Холмс": "Детективы",
        }
        collector.books_genre = expected_books

        fantasy_books = collector.get_books_with_specific_genre("Фантастика")
        assert "Дюна" in fantasy_books
        assert "Ночной дозор" in fantasy_books
        assert "Шерлок Холмс" not in fantasy_books

    # Тест 7: Получение книг для детей (проверка возрастного рейтинга)
    def test_get_books_for_children_excludes_age_rated_genres(self, collector):
        expected_books = {
            "Фиксики": "Мультфильмы",
            "Туман": "Ужасы",
            "Маша и Медведь": "Мультфильмы",
        }
        collector.books_genre = expected_books

        children_books = collector.get_books_for_children()
        assert "Фиксики" in children_books
        assert "Маша и Медведь" in children_books
        assert "Туман" not in children_books

    # Тест 8: Добавление книги в избранное
    def test_add_book_in_favorites_adds_existing_book(self, collector):
        expected_books = {
            "Этерна": "Фантастика",
        }
        collector.books_genre = expected_books

        collector.add_book_in_favorites("Этерна")
        assert "Этерна" in collector.get_list_of_favorites_books()

    # Тест 9: Попытка добавить в избранное несуществующую книгу
    def test_add_book_in_favorites_cannot_add_nonexistent_book(
        self, collector
    ):
        expected_books = {
            "Этерна": "Фантастика",
        }
        collector.books_genre = expected_books

        collector.add_book_in_favorites("Несуществующая книга")
        assert (
            "Несуществующая книга"
            not in collector.get_list_of_favorites_books()
        )

    # Тест 10: Удаление книги из избранного
    def test_delete_book_from_favorites_deletes_existing_book(self, collector):
        expected_favorites = ["Мастер и Маргарита"]
        collector.favorites = expected_favorites

        collector.delete_book_from_favorites("Мастер и Маргарита")
        assert (
            "Мастер и Маргарита" not in collector.get_list_of_favorites_books()
        )

    # Тест 11: Проверка получения жанра существующей книги
    def test_get_book_genre_returns_genre_of_existing_book(self, collector):
        expected_books = {
            "Преступление и наказание": "Детективы",
        }
        collector.books_genre = expected_books

        result = collector.get_book_genre("Преступление и наказание")
        assert result == "Детективы"

    # Тест 12: Проверка получения словаря всех книг и жанров
    def test_get_books_genre_returns_books_genre_dictionary(self, collector):
        expected_books = {
            "Книга 1": "Фантастика",
            "Книга 2": "Комедии",
            "Книга 3": "Детективы",
        }
        collector.books_genre = expected_books

        result = collector.get_books_genre()
        assert result == expected_books

    # Тест 13: Проверка получения списка избранных книг
    def test_get_list_of_favorites_books_returns_favorites_list(
        self, collector
    ):
        expected_favorites = ["Книга 1", "Книга 2", "Книга 3"]
        collector.favorites = expected_favorites

        result = collector.get_list_of_favorites_books()
        assert result == expected_favorites
