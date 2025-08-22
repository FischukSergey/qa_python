import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем
# наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

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
    def test_add_new_book_book_added_successfully(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.get_books_genre()

    # Тест 2: Параметризованный тест для добавления книг с невалидными
    # названиями (пустая строка и строка длиной более 40 символов)
    @pytest.mark.parametrize(
        "book_name",
        ["", "012345678901234567890123456789012345678901"],
    )
    def test_add_new_book_invalid_length_book_names(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    # Тест 3: Проверка, что одну книгу нельзя добавить дважды
    def test_add_new_book_same_book_cannot_be_added_twice(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.add_new_book("Мастер и Маргарита")
        assert len(collector.get_books_genre()) == 1

    # Тест 4: Проверка, что у добавленной книги нет жанра
    def test_add_new_book_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        assert collector.get_book_genre("Мастер и Маргарита") == ""

    # Тест 5: Проверка, что у книги можно установить жанр
    def test_set_book_genre_set_genre_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")
        assert collector.get_book_genre("Дюна") == "Фантастика"

    # Тест 6: Получение списка книг определенного жанра
    def test_get_books_with_specific_genre_returns_books_of_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Дюна")
        collector.add_new_book("Ночной дозор")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Дюна", "Фантастика")
        collector.set_book_genre("Ночной дозор", "Фантастика")
        collector.set_book_genre("Шерлок Холмс", "Детективы")

        fantasy_books = collector.get_books_with_specific_genre("Фантастика")
        assert len(fantasy_books) == 2
        assert "Дюна" in fantasy_books
        assert "Ночной дозор" in fantasy_books

    # Тест 7: Получение книг для детей (проверка возрастного рейтинга)
    def test_get_books_for_children_excludes_age_rated_genres(self):
        collector = BooksCollector()
        collector.add_new_book("Фиксики")
        collector.add_new_book("Туман")
        collector.add_new_book("Маша и Медведь")

        collector.set_book_genre("Фиксики", "Мультфильмы")
        collector.set_book_genre("Туман", "Ужасы")  # возрастной рейтинг
        collector.set_book_genre("Маша и Медведь", "Мультфильмы")

        children_books = collector.get_books_for_children()
        assert len(children_books) == 2
        assert "Фиксики" in children_books
        assert "Маша и Медведь" in children_books
        assert "Туман" not in children_books

    # Тест 8: Добавление книги в избранное
    def test_add_book_in_favorites_adds_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Этерна")
        collector.add_book_in_favorites("Этерна")
        assert "Этерна" in collector.get_list_of_favorites_books()

    # Тест 9: Попытка добавить в избранное несуществующую книгу
    def test_add_book_in_favorites_cannot_add_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Несуществующая книга")
        assert (
            len(collector.get_list_of_favorites_books()) == 0
        )

    # Тест 10: Удаление книги из избранного
    def test_delete_book_from_favorites_deletes_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Этерна")
        collector.add_book_in_favorites("Этерна")
        collector.delete_book_from_favorites("Этерна")
