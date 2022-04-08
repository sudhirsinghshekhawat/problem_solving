import datetime
from abc import ABC

from .models import AccountStatus


class Account(ABC):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__status = status
        self.__person = person

    def reset_password(self):
        ...


class Librarian(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        super().__init__(id, password, person, status)

    def add_book_item(self, book_item):
        ...

    def block_member(self, member):
        ...

    def unblock_member(self, member):
        ...


class Member(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        super().__init__(id, password, person, status)
        self.date_of_membership = datetime.date.today()
        self.total_book_checkout = 0
