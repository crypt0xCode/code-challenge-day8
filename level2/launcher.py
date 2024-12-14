from level2.bankaccount import BankAccount
from level2.library import Library


def start_level2() -> None:
    #region BankAccount example.
    my_account = BankAccount(1000, 'Bob')
    print(f'Balance of account before deposit: {my_account.balance}')
    my_account.deposit(500)
    print(f'Balance of account after deposit: {my_account.balance}')
    my_account.withdraw(800)
    print(f'Balance of account after withdraw: {my_account.balance}')
    my_account.withdraw(800)
    print(f'Balance of account after secondary withdraw: {my_account.balance}\n\n')
    #endregion

    #region Library example.
    my_library = Library(['Ulysses', 'The Great Gatsby', 'Lolita'], ['Bob', 'John', 'James'])
    print(f'Initial books list: {my_library.books}')
    print(f'Initial members list: {my_library.members}\n')

    my_library.add_book('Catch-22')
    print(f'Books list after append: {my_library.books}')
    my_library.remove_book('Lolita')
    print(f'Books list after removing: {my_library.books}')
    my_library.remove_book('1984')
    print(f'Books list after secondary removing: {my_library.books}\n')

    my_library.add_member('Kate')
    print(f'Members list after append: {my_library.members}')
    my_library.remove_member('John')
    print(f'Members list after removing: {my_library.members}')
    my_library.remove_member('Sarah')
    print(f'Members list after secondary removing: {my_library.members}\n')

    my_library.checkout_book('Ulysses', 'Bob')
    print(f'Books list after checkout book for member: {my_library.books}')
    my_library.checkout_book('The Great Gatsby', 'Sarah')
    print(f'Books list after secondary checkout book for member: {my_library.books}')
    my_library.return_book('Ulysses', 'Bob')
    print(f'Books list after returning book from member: {my_library.books}')
    #endregion