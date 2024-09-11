class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

# Create an instance and run the method
book1 = Book("1984", "George Orwell", 328)
print(book1.summary())