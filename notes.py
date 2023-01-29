from notes_classes import NOTEBOOK, Record

HELP_TEXT = """This bot save your notes 
    Global commands:
      'add' - add new note. Input note text and then input tag or tags (key words)
    Example: add
      'change' - command for change existing note. Input note number and then input new text
    Example: change
      'delete' - command for delete note. Input note number
    Example: delete 1
      'find note' - command to find notes. Input note text that you want to find
    Example: find note KeyWord
      'find tag' - command to find notes by tag. Input tag that you want to find
    Example: find tag Tag
      'hello'/'hi' - greeting command to start working with the bot
      'help' - command for output helptext
      'show all' - show all notes
    Example: show all
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


def add_note(*args):
    note = input('Enter your note: ')
    tag = input('Enter tag or tags to your note: ')
    record = Record(note, tag)
    NOTEBOOK.add_note(record)
    return f"Note successfully added"


def change_note(*args):
    index = input('Enter note number: ')
    new_note = input('Enter new note: ')
    try:
        return NOTEBOOK.edit_note(int(index), new_note)
    except KeyError:
        return f"Note {index} not exist. Try again"


def delete_note(index):
    try:
        int(index)
    except ValueError:
        return 'Try again. Input index'

    if int(index) in NOTEBOOK.data.keys():
        NOTEBOOK.remove_note(int(index))
        return f"Note has been deleted"
    else:
        return f'Not found index {index}'


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
    search_notes: ["find note"],
    sort_tags: ["find tag"]
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
