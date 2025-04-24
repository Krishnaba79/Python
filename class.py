class Book():

    name = " "
    author = " "
    year= " "
    chapters = " "

    def hello(self):
        print("hello")

book1 = Book()
book1.name = "pyscology of money"
book1.year = "2017"
book1.author = "abc"
book1.chapters=[1,2,3,4,]
print(book1.name,book1.year,book1.author,book1.chapters)

book2 = Book()
book2.name = "its ends with us"
book2.year = "2018"
book2.author = "xyz"
book2.chapters=[1,2,3,]
print(book2.name,book2.year,book2.author,book2.chapters)

