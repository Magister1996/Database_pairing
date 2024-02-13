## 1. Design and create the Table

Created a table called Bookstore in psql and seeded it with the SQL file

## 2. Create Test SQL seeds

See book_store.sql in databases

## 3. Define the class names

class Book()
    self.title
    self.author_name

class BookRepository()
    self.connection


## 4. Implement the Model class

class Book()
    def __init__(self, title, author_name)
        self.title
        self.author_name
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.author_name})"

## 5. Define the Repository Class interface

class BookRepository()
    def __init__(self, connection)
        self.conneciton = connection

    def all
        retrives all items in the table

## 6. Write Test Examples

def test_book()
    assert the inputed parameters are object features

def test_book_repository_all()
    assert the the all() function returns the entire database

## 7. Test-drive and implement the Repository class behaviour

