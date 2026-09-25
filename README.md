# qa_python

# BooksCollector — тесты

Проект с юнит-тестами для класса `BooksCollector`, который управляет коллекцией книг: хранит книги и их жанры, ведёт список избранного, определяет книги для детей.

## Структура

- `main.py` — класс `BooksCollector`.
- `tests.py` — тесты.
- `conftest.py` — фикстура `collector`.

## Запуск тестов

```bash
pytest -v tests.py
```

## Реализованные тесты

### add_new_book
- `test_add_new_book_length_validation` — параметризованный тест: проверяет добавление книги с именем длиной 1, 40, 41 и 0 символов.

### set_book_genre
- `test_set_book_genre_sets_valid_genre` — валидный жанр устанавливается.
- `test_set_book_genre_unknown_genre_not_set` — жанр не из списка доступных не устанавливается.

### get_book_genre
- `test_get_book_genre_get_valid_genre` — возвращает установленный жанр книги.

### get_books_with_specific_genre
- `test_get_books_with_specific_genre_returns_matching` — возвращает только книги с указанным жанром.

### get_books_genre
- `test_get_books_genre_returns_full_dict` — возвращает полный словарь книг.

### get_books_for_children
- `test_get_books_for_children_returns_allowed` — возвращает книги без возрастного рейтинга.
- `test_get_books_for_children_excludes_age_rated` — не включает книги с возрастным рейтингом.

### add_book_in_favorites
- `test_add_book_in_favorites_adds_book` — книга добавляется в избранное.
- `test_add_book_in_favorites_duplicate_not_added` — повторное добавление не создаёт дубликат.

### delete_book_from_favorites
- `test_delete_book_from_favorites_removes_book` — книга удаляется из избранного.

### get_list_of_favorites_books
- `test_get_list_of_favorites_books_returns_list` — возвращает список избранных книг.

## Используемые приёмы

- **Фикстура** `collector` в `conftest.py` — создаёт свежий `BooksCollector` перед каждым тестом.
- **Параметризация** через `@pytest.mark.parametrize` — для проверки граничных значений имени книги.