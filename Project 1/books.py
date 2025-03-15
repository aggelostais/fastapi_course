from fastapi import Body, FastAPI

app = FastAPI() # Create a FastAPI instance


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

# async is not needed here as FastAPI will add it automatically if needed,
# but it is a good practice to use it

@app.get("/books")
async def read_all_books():
    return BOOKS

# If two functions accept the same path, the one defined first will be used
# So what we need to do is always have the static or smaller or more specific APIs in front, 
# because fast API looks in a chronological order from top to bottom to see what matches the URL.
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():  # case insensitive comparison
            return book

# Query parameter is used to filter the books by category
# Usage example http://127.0.0.1:8000/books/?category=math
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    # Wwe loop through all the books and check if the category matches the one provided in the query
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# Get all books from a specific author using path or query parameters
# We use query parameter here
@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return

# Get all books from a specific author using path or query parameters
# Path parameters have priority over query parameters,so if you use both, the path parameter will be used.
# Both arameters are required in this case.
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()): # Body is used to get the request body
    BOOKS.append(new_book)

# Update a book by title (we assume that the title is unique)
# The updated book is passed in the request body
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i) # Remove the book from the list
            break
