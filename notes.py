from notes_classes import Note, Tag, NOTEBOOK, Record

HELP_TEXT = """This contact bot save your contacts 
    Global commands:
      'add contact' - add new contact. Input user name and phone
    Example: add User_name 095-xxx-xx-xx
    """


def hello(*args):
    return "How can I help you?"


# Exit assistant
def bye(*args):
    return "Bye"


# README instructions
def help_user(*args):
    return HELP_TEXT


def add_note(*args):
    note = input('Print your note ')
    tag = input('Print tag or tags to your note ')
    record = Record(note, tag)
    NOTEBOOK.add_note(record)
    return f"Note successfully added"


def change_note(index, new_note):
    try:
        return NOTEBOOK.edit_note(int(index), new_note)
    except KeyError:
        return f"Note {index} not exist. Try again"


def delete_note(*args):
    NOTEBOOK.remove_note(int(*args))
    return f"Note has been deleted"


def search_notes(message):
    return NOTEBOOK.search_note(message)


def show_all(*args):
    if len(NOTEBOOK):
        return NOTEBOOK.show_all()
    else:
        return 'No notes found'


def sort_tags(message):
    return NOTEBOOK.sort_tags(message)


COMMANDS = {
    hello: ["hello", "hi"],
    show_all: ["show all"],
    help_user: ["help"],
    bye: [".", "bye", "good bye", "close", "exit"],
    add_note: ["add"],
    change_note: ["change"],
    delete_note: ["delete"],
    search_notes: ["find"],
    sort_tags: ["sort"]
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


def run_notes():
    try:
        NOTEBOOK.read_file()
    except FileNotFoundError:
        NOTEBOOK.write_file()
        NOTEBOOK.read_file()

    while True:
        user_input = str(input(">>>> "))
        result = run_bot(user_input)
        if result == "Bye":
            save = input('Do you want to save? (y/n) ')
            if save == 'n':
                print("Goodbye!")
                break
            elif save == 'y':
                NOTEBOOK.write_file()
                print("All data save. Goodbye!")
                break
            else:
                print("Try again, please")
        print(result)
