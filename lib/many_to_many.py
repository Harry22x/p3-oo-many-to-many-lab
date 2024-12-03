from datetime import datetime
class Author:
    
    all = []
    def __init__(self,name):
        pass
        self.name = name
        Author.all.append(self)

    def contracts(self):
        pass
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        pass
        return[contract.book for contract in Contract.all if contract.author == self]
   
    def sign_contract(self,book,date,royalties):
        pass
        return Contract(self,book,date,royalties)
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])

        
class Book:
    pass
    all = []
    def __init__(self,title):
        pass
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        pass
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return Author.all


class Contract:
    pass
    all = []
    def __init__(self,author,book,date,royalties):
        pass
        self.author = author
        self.book = book
        self.date= date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,author):
        if isinstance(author,Author):
            self._author = author
        else:
            raise Exception("Author must be a string")
   
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self,book):
        if isinstance(book,Book):
            self._book = book
        else:
            raise Exception("book must be a string")



    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,date):
        if isinstance(date,str):
            self._date = date
        else:
            raise Exception("date must be a string")
    
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self,royalties):
        if isinstance(royalties, int) and royalties > 0:
            self._royalties = royalties
        else:
            raise Exception("Royalties must be a positive integer")
        
    @classmethod
    def contracts_by_date(cls, date): 
        pass
        return [contract for contract in cls.all if contract.date == date]