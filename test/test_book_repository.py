from lib.book_repository import BookRepository
from lib.book import Book


def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("databases/book_store.sql") # Seed our database with some test data
    repository = BookRepository(db_connection) # Create a new ArtistRepository

    books = repository.all() # Get all artists

    # Assert on the results
    assert books == [
        Book(1,'Nineteen Eighty-Four', 'George Orwell'),
        Book(2,'Mrs Dalloway', 'Virginia Woolf'),
        Book(3,'Emma', 'Jane Austen'),
        Book(4,'Dracula', 'Bram Stoker'),
        Book(5,'The Age of Innocence', 'Edith Wharton')
    ]

