import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    @pytest.mark.parametrize('name, expected_len', [
                                                    ('A', 1),
                                                    ('A' * 40, 1),
                                                    ('A' * 41, 0),
                                                    ('', 0),
        ])
    def test_add_new_book_length_validation(self, collector, name, expected_len):
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == expected_len


    def test_set_book_genre_sets_valid_genre(self, collector):
        collector.add_new_book('Snatch')
        collector.set_book_genre('Snatch', 'Комедии')

        assert collector.get_book_genre('Snatch') == 'Комедии'


    def test_set_book_genre_unknown_genre_not_set(self, collector):
        collector.add_new_book('The hateful eight')
        collector.set_book_genre('The hateful eight', 'Вестерн')

        assert collector.get_book_genre('The hateful eight') == ''


    def test_get_book_genre_get_valid_genre(self, collector):
        collector.add_new_book('Zodiac')
        collector.set_book_genre('Zodiac', 'Детективы')

        assert collector.get_book_genre('Zodiac') == 'Детективы'


    def test_get_books_with_specific_genre_returns_matching(self, collector):
        collector.add_new_book('The Fellowship of the Ring')
        collector.add_new_book('The Two Towers')
        collector.add_new_book('The Return of the King')
        collector.add_new_book('A Man Called Ove')
        collector.add_new_book('Dirk Gently Holistic Detective Agency')
        collector.add_new_book('It')
        collector.set_book_genre('The Fellowship of the Ring', 'Фантастика')
        collector.set_book_genre('The Two Towers', 'Фантастика')
        collector.set_book_genre('The Return of the King', 'Фантастика')
        collector.set_book_genre('A Man Called Ove', 'Комедии')
        collector.set_book_genre('Dirk Gently Holistic Detective Agency', 'Детективы')
        collector.set_book_genre('It', 'Ужасы')
        
        assert collector.get_books_with_specific_genre('Фантастика') == [
                                                                        'The Fellowship of the Ring',
                                                                        'The Two Towers',
                                                                        'The Return of the King',
            ]


    def test_get_books_genre_returns_full_dict(self, collector):
        collector.add_new_book('The Shining')
        collector.add_new_book('Misery')
        collector.set_book_genre('The Shining', 'Ужасы')
        collector.set_book_genre('Misery', 'Ужасы')

        assert collector.get_books_genre() == {'The Shining': 'Ужасы', 'Misery': 'Ужасы'}


    def test_get_books_for_children_returns_allowed(self, collector):
        collector.add_new_book('Harry Potter and the Philosophers Stone')
        collector.add_new_book('Harry Potter and the Deathly Hallows')
        collector.set_book_genre('Harry Potter and the Philosophers Stone', 'Фантастика')
        collector.set_book_genre('Harry Potter and the Deathly Hallows', 'Фантастика')

        assert collector.get_books_for_children() == ['Harry Potter and the Philosophers Stone',
                                                'Harry Potter and the Deathly Hallows'
            ]


    def test_get_books_for_children_excludes_age_rated(self, collector):
        collector.add_new_book('Pet Sematary')
        collector.add_new_book('Carrie')
        collector.add_new_book('11/22/63')
        collector.set_book_genre('Pet Sematary', 'Ужасы')
        collector.set_book_genre('Carrie', 'Ужасы')
        collector.set_book_genre('11/22/63', 'Фантастика')

        assert collector.get_books_for_children() == ['11/22/63']


    def test_add_book_in_favorites_adds_book(self, collector):
        collector.add_new_book('The Catcher in the Rye')
        collector.add_book_in_favorites('The Catcher in the Rye')

        assert collector.get_list_of_favorites_books() == ['The Catcher in the Rye']


    def test_add_book_in_favorites_duplicate_not_added(self, collector):
        collector.add_new_book('Good Omens')
        collector.add_book_in_favorites('Good Omens')
        collector.add_book_in_favorites('Good Omens')
        assert len(collector.get_list_of_favorites_books()) == 1


    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book('American Gods')
        collector.add_new_book('Good Omens')
        collector.add_book_in_favorites('American Gods')
        collector.add_book_in_favorites('Good Omens')
        collector.delete_book_from_favorites('American Gods')

        assert collector.get_list_of_favorites_books() == ['Good Omens']


    def test_get_list_of_favorites_books_returns_list(self, collector):
        collector.add_new_book('The Catcher in the Rye')
        collector.add_new_book('American Gods')
        collector.add_new_book('Good Omens')
        collector.add_book_in_favorites('The Catcher in the Rye')
        collector.add_book_in_favorites('American Gods')
        collector.add_book_in_favorites('Good Omens')

        assert collector.get_list_of_favorites_books() == ['The Catcher in the Rye',
                                                            'American Gods',
                                                            'Good Omens'
            ]
