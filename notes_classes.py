from collections import UserDict
import pickle


class NoteBook(UserDict):
    def read_file(self):
        with open('NoteBook.bin', 'rb') as reader:
            self.data = pickle.load(reader)
            return self.data

    def write_file(self):
        with open('NoteBook.bin', 'wb') as writer:
            pickle.dump(self.data, writer)

    def add_note(self, record):
        self.data[record.index.value] = record

    def remove_note(self, record):
        self.data.pop(record.index.value, None)


class Field:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Tags(Field):
    pass


class Notes(Field):
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    @Field.value.setter
    def value(self, value):
        self._value = value


NOTEBOOK = NoteBook()
