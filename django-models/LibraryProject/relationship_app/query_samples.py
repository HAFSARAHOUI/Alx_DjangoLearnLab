# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def get_librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

author = Author.objects.get(name="Author Name")  # Replace with real name in your DB
books_by_author = Book.objects.filter(author=author)

for book in books_by_author:
    print(book.title)
library = Library.objects.get(name="Library Name")  # Replace with a real name
librarian = Librarian.objects.get(library=library)

print(librarian.name)