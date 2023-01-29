from datetime import timedelta
from .decorators import *
from .addressbook_classes import Name, Phone, Record, ADDRESSBOOK, Mail, Address


HELP_TEXT = """This contact bot save your contacts 
    Global commands:
      'add contact' - add new contact. Input user name and phone
    Example: add contact User_name 095-xxx-xx-xx
      'add address' - add user address to contact. Input user name and address
    Example: add address User_name User_address
      'add birthday' - add birthday to contact. Input user name and birthday in format yyyy-mm-dd
    Example: add User_name 1971-01-01
      'add mail' - add e-mail address to contact. Input user name and e-mail
    Example: add mail User_name user123@gmail.com
      'birthday soon' - command to display birthdays in a given interval (N-days)
    Example: birthday soon 7
      'change address' - change user address. Input user name and address
    Example: change address User_name User_new_address
      'change mail' - change user e-mail address. Input user name and e-mail
    Example: change mail User_name user123@gmail.com
      'change phone' - change users old phone to new phone. Input user name, old phone and new phone
    Example: change User_name 095-xxx-xx-xx 050-xxx-xx-xx
      'delete address' - delete user address from contact. Input user name
    Example: delete address User_name
      'delete mail' - delete user e-mail address from contact. Input user name
    Example: delete mail User_name
      'delete user' - delete contact (name and phones). Input user name
    Example: delete contact User_name
      'delete phone' - delete phone of some User. Input user name and phone
    Example: delete phone User_name 099-xxx-xx-xx
      'hello'/'hi' - greeting command to start working with the bot
      'help' - command for output helptext
      'phone' - show contacts of input user. Input user name
    Example: phone User_name
      'search' - keyword search. Input keywords that you want
    Example: search KeyWord
      'show all' - show all contacts
    Example: show all
      'show list' - show list of contacts which contains N-users
    Example: show list 5 
      'when celebrate' - show days to birthday of User/ Input user name
    Example: when celebrate User_name
      'exit/'.'/'bye'/'good bye'/'close' - exit bot
    Example: good bye"""


def hello(*args):
    return "How can I help you?"


# Exit assistant
def bye(*args):
    return "Bye"


# README instructions
def help_user(*args):
    return HELP_TEXT


# Add user birthday to AddressBook
@input_error
def add_birthday(*args):
    name = Name(str(args[0]).title())
    birthday = tuple(re.split('\D', args[1]))
    if name.value in ADDRESSBOOK:
        ADDRESSBOOK[name.value].add_user_birthday(*birthday)
        return f"The Birthday for {name.value} was recorded"
    else:
        raise UserMissing("User is not found. Please try again")


@input_error
def add_mail(*args):
    name = Name(str(args[0]).title())
    mail = Mail(str(args[1]))
    if name.value in ADDRESSBOOK:
        ADDRESSBOOK[name.value].add_mail(mail)
        return f'{mail.value} successfully added to contact {name.value}'
    else:
        raise UserMissing("User is not found. Please try again")


@input_error
def delete_mail(*args):
    name = Name(str(args[0]).title())
    if name.value in ADDRESSBOOK:
        ADDRESSBOOK[name.value].del_mail()
        return f'Successfully deleted {name.value} mail'
    else:
        raise ElseError("Something went wrong. Please try again")


@input_error
def change_mail(*args):
    name = Name(str(args[0]).title())
    mail = Mail(str(args[1]))
    if name.value in ADDRESSBOOK:
        ADDRESSBOOK[name.value].chang_mail(mail)
        return f'{mail.value} successfully changed to contact {name.value}'
    else:
        raise UserMissing("User is not found. Please try again")


# Add user or user with phone to AddressBook
@input_error
def add_phone(*args):
    name = Name(str(args[0]).title())
    phone_num = (Phone(args[1]))
    rec = ADDRESSBOOK.get(name.value)
    if rec:
        rec.add_phone(phone_num)
    else:
        rec = Record(name, phone_num)
        ADDRESSBOOK.add_record(rec)
    return f'Contact {name} {phone_num} added'


# Change users contact to another contact
@input_error
def change(*args):
    name = Name(str(args[0]).title())
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])
    if name in ADDRESSBOOK:
        ADDRESSBOOK.change_record(name.value, old_phone.value, new_phone.value)
        return f'User {name} changed {old_phone} to {new_phone}'
    elif name not in ADDRESSBOOK:
        raise UserMissing("User is not found. Please try again")
    else:
        raise PhoneMissing("Phone number is not found. Please try again")


@input_error
def add_address(*args):
    name = Name(str(args[0]).title())
    address = Address(str(args[1]))
    if name.value in ADDRESSBOOK:
        ADDRESSBOOK[name.value].add_address(address)
        return f'Address: {address.value}, successfully added to contact {name.value}'
    else:
        raise UserMissing("User is not found. Please try again")


@input_error
def change_address(*args):
    name = Name(str(args[0]).title())
    address = Address(str(args[1]))
    if name.value in ADDRESSBOOK:
        ADDRESSBOOK[name.value].change_address(address)
        return f'Address: {address.value}, successfully changed to contact {name.value}'
    else:
        raise UserMissing("User is not found. Please try again")


@input_error
def remove_address(*args):
    name = Name(str(args[0]).title())
    if name.value in ADDRESSBOOK:
        ADDRESSBOOK[name.value].remove_address()
        return f'Successfully deleted {name.value} address'
    else:
        raise ElseError("Something went wrong. Please try again")


@input_error
def days_to_bday(*args):
    name = Name(str(args[0]).title())
    if name.value in ADDRESSBOOK:
        if ADDRESSBOOK[name.value].birthday:
            days = ADDRESSBOOK[name.value].days_to_birthday()
            return days
        else:
            return f'{name.value} birthday is unknown'
    else:
        raise UserMissing("User is not found. Please try again")


# Delete contact
@input_error
def delete_contact(*args):
    name = ADDRESSBOOK[args[0].title()]
    ADDRESSBOOK.remove_record(name)
    raise UserMissing("User is not found. Please try again")


@input_error
def delete_phone(*args):
    name = Name(str(args[0]).title())
    phone = Phone(args[1])
    if name.value in ADDRESSBOOK:
        ADDRESSBOOK[name.value].remove_phone(phone.value)
        return f"Phone for {name.value} was delete"
    else:
        raise PhoneMissing("Phone number is not found. Please try again")


@input_error
def get_birthdays_per_period(*args):
    period = args[0]
    item = ''
    current_date = datetime.now().date()
    for contact in ADDRESSBOOK.values():
        contact_birthday = datetime.date(datetime.strptime(str(contact.birthday), '%Y-%m-%d')).replace(year=current_date.year)
        if current_date < contact_birthday < current_date + timedelta(days=int(period)):
            item += f'{contact.name} (B-day: {contact.birthday}; email: {contact.mail}): {", ".join([p.value for p in contact.phones])}\n'
    if item:
        return item.rstrip('\n')
    else:
        return f'No birthdays for the next {period} days'


# Show some contact
@input_error
def phone(*args):
    return ADDRESSBOOK.show_rec(str(args[0]).title())


# Search contacts with some symbols
def search(*args):
    if ADDRESSBOOK.search(str(args[0])):
        return ADDRESSBOOK.search(str(args[0]))
    else:
        return "Searching failed! KeyWord doesn't exist"


# Show all contacts
def show_all(*args):
    if len(ADDRESSBOOK):
        return ADDRESSBOOK.show_all_rec()
    else:
        return 'AddressBook is empty'


@input_error
def show_list(*args):
    if len(ADDRESSBOOK):
        return ''.join(ADDRESSBOOK.iterator(int(args[0])))
    else:
        return 'AddressBook is empty'


COMMANDS = {
    hello: ["hello", "hi"],
    show_all: ["show all"],
    show_list: ["show list"],
    search: ["search"],
    phone: ["phone"],
    add_phone: ["add contact"],
    change: ["change phone"],
    delete_contact: ["delete user"],
    delete_phone: ["delete phone"],
    add_birthday: ["add birthday"],
    days_to_bday: ["when celebrate"],
    help_user: ["help"],
    bye: [".", "bye", "good bye", "close", "exit"],
    get_birthdays_per_period: ["birthday soon"],
    add_mail: ["add mail"],
    delete_mail: ["delete mail"],
    change_mail: ["change mail"],
    add_address: ["add address"],
    change_address: ["change address"],
    remove_address: ["delete address"]
}


def parse_command(text: str):
    for comm, key_words in COMMANDS.items():
        for key_word in key_words:
            if text.startswith(key_word):
                return comm, text.replace(key_word, "").strip().split(" ")
    return None, None


# Функція спілкування з юзером і виконання функцій відповідно до команди
def run_bot(user_input):
    command, data = parse_command(user_input.lower())
    if not command:
        return "Incorrect input. Try again"

    return command(*data)


def run_addressbook():
    try:
        ADDRESSBOOK.read_file()
    except FileNotFoundError:
        ADDRESSBOOK.write_file()
        ADDRESSBOOK.read_file()

    while True:
        user_input = str(input(">>>> "))
        result = run_bot(user_input)
        if result == "Bye":
            save = input('Do you want to save? (y/n) ')
            if save == 'n':
                print("Goodbye!")
                break
            elif save == 'y':
                ADDRESSBOOK.write_file()
                print("All data save. Goodbye!")
                break
            else:
                print("Try again, please")
        print(result)

