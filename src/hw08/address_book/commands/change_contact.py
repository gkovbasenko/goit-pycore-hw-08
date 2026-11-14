from hw08.address_book.decorators import input_error
from hw08.address_book.book import AddressBook


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book[name]
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."
