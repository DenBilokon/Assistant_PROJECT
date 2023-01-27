from collections import UserDict
import pickle

class NoteBook(UserDict):
    def __init__(self):
        super().__init__()
        self.index = 1

    def read_file(self):
        with open('NoteBook.bin', 'rb') as reader:
            self.data = pickle.load(reader)
            return self.data

    def write_file(self):
        with open('NoteBook.bin', 'wb') as writer:
            pickle.dump(self.data, writer)

    def add_note(self, record):
        if self.index:
            self.data[self.index] = record
            self.index += 1
        return self.index

    def remove_note(self, index):
        self.data.pop(index, None)

    def show_all(self):
        return "\n".join(f'{index} {", ".join([p.value for p in wr.tags])} {wr.note.value}' for index, wr in self.data.items())


class Field:
    def __init__(self, value):
        self.value = value


class Tag(Field):
    pass


class Note(Field):
    pass


class Record:
    def __init__(self, note, tag=None):
        self.note = Note(note)
        self.tags = []
        if tag:
            self.tags.append(Tag(tag))


NOTEBOOK = NoteBook()
# s = Note('asfafsafs')
# a = Note('235235')
# g = Note('23525dsf')
# rec = Record(s)
# rec1 = Record(a)
# ab = NoteBook()
# ab.add_note(rec)
# ab.add_note(rec1)


# print(ab.show_all())
# er = ab.get(key)
# print(er)