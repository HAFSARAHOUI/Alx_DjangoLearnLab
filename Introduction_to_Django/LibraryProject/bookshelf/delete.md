from bookshelf.models import Book

# Get the book object by ID or another attribute
book = Book.objects.get(title="1984", author="George Orwell")

# Delete the book
book.delete()

# Confirm deletion by retrieving all books
Book.objects.all()

# Expected Output:
# <QuerySet []>
# (This confirms that the book has been successfully deleted)
