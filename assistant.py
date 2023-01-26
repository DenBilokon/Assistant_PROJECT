import re
from datetime import datetime, timedelta
from decorators import input_error
from bot_classes import Name, Phone, Record, ADDRESSBOOK, Mail
from sort_directory import sort_folder

HELP_TEXT = """This contact bot save your contacts 
    Global commands:
      'add contact' - add new contact. Input user name and phone
    Example: add User_name 095-xxx-xx-xx
      'add birthday' - add birthday of some User. Input user name and birthday in format yyyy-mm-dd
    Example: add User_name 1971-01-01
      'change' - change users old phone to new phone. Input user name, old phone and new phone
    Example: change User_name 095-xxx-xx-xx 050-xxx-xx-xx
      'delete contact' - delete contact (name and phones). Input user name
    Example: delete contact User_name
      'delete phone' - delete phone of some User. Input user name and phone
    Example: delete phone User_name 099-xxx-xx-xx
      'phone' - show contacts of input user. Input user name
    Example: phone User_name
      'search' - keyword search. Input keywords that ypu want
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
        return f"Contact {name.value} does not exists"

@input_error
def add_mail(*args):
    name = Name(str(args[0]).title())
    mail = Mail(str(args[1]))
    if name.value in ADDRESSBOOK:
        ADDRESSBOOK[name.value].add_mail(mail)
        return f'{mail.value} successfully added to contact {name.value}'
    else:
        return f'Contact {name.value} does not exist'


@input_error
def delete_mail(*args):
    name = Name(str(args[0]).title())
    if name.value in ADDRESSBOOK:
        ADDRESSBOOK[name.value].del_mail()
        return f'Successfully deleted {name.value} mail'
    else:
        return f'Cannot delete mail'


@input_error
def change_mail(*args):
    name = Name(str(args[0]).title())
    mail = Mail(str(args[1]))
    if name.value in ADDRESSBOOK:
        ADDRESSBOOK[name.value].chang_mail(mail)
        return f'{mail.value} successfully changed to contact {name.value}'
    else:
        return f'Contact {name.value} does not exist'


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
    ADDRESSBOOK.change_record(name.value, old_phone.value, new_phone.value)
    return f'User {name} changed {old_phone} to {new_phone}'


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
        return f'Contact {name.value} does not exists'


# Delete contact
@input_error
def delete_contact(*args):
    name = ADDRESSBOOK[args[0].title()]
    ADDRESSBOOK.remove_record(name)
    return f'Contact {args[0]} deleted'


@input_error
def delete_phone(*args):
    name = Name(str(args[0]).title())
    phone = Phone(args[1])
    if name.value in ADDRESSBOOK:
        ADDRESSBOOK[name.value].remove_phone(phone.value)
        return f"Phone for {name.value} was delete"
    else:
        return f"Contact {name.value} does not exist"


@input_error
def get_birthdays_per_period(*args):
    period = args[0]
    item = ''
    current_date = datetime.now().date()
    for contact in ADDRESSBOOK.values():
        contact_birthday = datetime.date(datetime.strptime(
            str(contact.birthday), '%Y-%m-%d')).replace(year=current_date.year)
        if current_date < contact_birthday < current_date + timedelta(days=int(period)):
            item += f'{contact.name}: {str(contact.birthday)}\n'
    # f'{rec.name} (B-day: {rec.birthday}; email: {rec.mail}): {", ".join([p.value for p in rec.phones])}\n'
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
    return ADDRESSBOOK.search(str(args[0]))


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
    change_mail: ["change mail"]
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


def main():
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


if __name__ == "__main__":
    main()
