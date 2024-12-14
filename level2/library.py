"""
2) Создайте класс Library, представляющий библиотеку. Класс должен иметь атрибуты books (список книг) и members
(список членов библиотеки). Реализуйте методы add_book(book) для добавления книги в библиотеку, remove_book(book)
для удаления книги из библиотеки, add_member(member) для добавления нового члена библиотеки и remove_member(member)
для удаления члена библиотеки. Также реализуйте метод checkout_book(book, member) для выдачи книги члену
библиотеки и return_book(book, member) для возврата книги в библиотеку.
"""
class Library:
    def __init__(self, books: list, members: list):
        self.books = books
        self.members = members


    #region Books methods.
    def add_book(self, book: str) -> None:
        """
        Add new book to books list.

        :param book: book title.
        """
        self.books.append(book)


    def remove_book(self, book: str) -> bool:
        """
        Remove specify book from books list by title.

        :param book: book title.
        :return: bool flag.
        """
        flag: bool = True
        if book in self.books:
            self.books.remove(book)
        else:
            flag = False
            print(f'{book} not exist in books list.')

        return flag


    def checkout_book(self, book: str, member: str) -> None:
        """
        Gives specify book by title for specify member by name.

        :param book: book title.
        :param member: member name.
        """
        if self.remove_book(book) and self.check_member(member):
            print(f'Gives book {book} for member {member}')


    def return_book(self, book: str, member: str) -> None:
        """
        Returns specify book by title from specify member by name.

        :param book: book title.
        :param member: member name.
        """
        if self.check_member(member):
            self.add_book(book)
            print(f'Returns book {book} from member {member}')
    #endregion

    #region Members methods.
    def add_member(self, member: str) -> None:
        """
        Add new library member to the members list.

        :param member: member name.
        """
        self.members.append(member)


    def remove_member(self, member: str) -> bool:
        """
        Remove specify member from members list by name.

        :param member: member name.
        :return: bool flag.
        """
        flag: bool = True
        if member in self.members:
            self.members.remove(member)
        else:
            flag = False
            print(f'{member} not exist in library members list.')

        return flag


    def check_member(self, member: str) -> bool:
        """
        Check member in members list by name.

        :param member: member name.
        :return: bool flag.
        """
        flag: bool = True
        if not member in self.members:
            flag = False
            print(f'Member is not exist in members list.')

        return flag
    #endregion