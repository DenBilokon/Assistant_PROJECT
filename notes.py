from notes_classes import Note, Tag, NOTEBOOK, Record

HELP_TEXT = """This contact bot save your contacts 
    Global commands:
      'add contact' - add new contact. Input user name and phone
    Example: add User_name 095-xxx-xx-xx
    """


def add_note(message, tag):
    record = Record(message, tag)
    NOTEBOOK.add_note(record)


def delete_note(note_index):
    NOTEBOOK.remove_note(note_index)


def show_all():
    print(NOTEBOOK.show_all())


note = input('print note ')
tag = input('print tag ')
add_note(note, tag)
show_all()
index = input('print index ')
delete_note(int(index))
show_all()