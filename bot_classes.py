from collections import UserDict
from datetime import datetime
import pickle
import re


class WrongLenPhone(Exception):
    """ Exception for wrong length of the phone number """


class WrongTypePhone(Exception):
    """ Exception when a letter is in the phone number """


class WrongMail(Exception):
    """ Exception when a letter is in the phone number """


class AddressBook(UserDict):
    """ Dictionary class """

    def read_file(self):
        with open('AddressBook.bin', 'rb') as reader:
            self.data = pickle.load(reader)
            return self.data

    def write_file(self):
        with open('AddressBook.bin', 'wb') as writer:
            pickle.dump(self.data, writer)

    def add_record(self, record):
        self.data[record.name.value] = record

    def remove_record(self, record):
        self.data.pop(record.name.value, None)

    def search(self, symb):
        result = ''
        for rec in self.data.values():
            if str(symb).lower() in str(rec.name).lower():
                result += f'{rec.name} (B-day: {rec.birthday}; email: {rec.mail}): {", ".join([p.value for p in rec.phones])}\n'
            else:
                for phone in rec.phones:
                    if str(symb).lower() in str(phone):
                        result += f'{rec.name} (B-day: {rec.birthday}; email: {rec.mail}): {", ".join([p.value for p in rec.phones])}\n'
        return result

    def show_rec(self, name):
        return f'{name} (B-day: {self.data[name].birthday}; email: {self.data[name].mail}): {", ".join([str(phone.value) for phone in self.data[name].phones])}'

    def show_all_rec(self):
        return "\n".join(f'{rec.name} (B-day: {rec.birthday}; email: {rec.mail}): {", ".join([p.value for p in rec.phones])}' for rec in self.data.values())

    def change_record(self, name_user, old_record_num, new_record_num):
        record = self.data.get(name_user)
        if record:
            record.change(old_record_num, new_record_num)

    def iterator(self, n=1):
        records = list(self.data.keys())
        records_num = len(records)
        count = 0
        result = ''
        if n > records_num:
            n = records_num
        for rec in self.data.values():
            if count < n:
                result += f'{rec.name} (B-day: {rec.birthday}; email: {rec.mail}): {", ".join([p.value for p in rec.phones])}\n'
                count += 1
        yield result




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


class Name(Field):

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return str(self._value)

    @Field.value.setter
    def value(self, value):
        self._value = value


class Phone(Field):
    """Class for do phone number standard type"""

    @staticmethod
    def sanitize_phone_number(phone):
        new_phone = (
            str(phone).strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        try:
            new_phone = [str(int(i)) for i in new_phone]
        except ValueError:
            raise WrongTypePhone('Input correct phone')

        else:
            new_phone = "".join(new_phone)
            if len(new_phone) == 12:
                return f"+{new_phone}"
            elif len(new_phone) == 10:
                return f"+38{new_phone}"
            else:
                raise WrongLenPhone("Length of phone's number is wrong")

    def __init__(self, value):
        super().__init__(value)
        self._value = Phone.sanitize_phone_number(value)

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return str(self._value)

    @Field.value.setter
    def value(self, value):
        self._value = Phone.sanitize_phone_number(value)


class Birthday(datetime):
    """ Class for creating fields 'birthday' """

    @staticmethod
    def sanitize_date(year, month, day):
        try:
            birthday = datetime(year=year, month=month, day=day)
        except ValueError:
            print("Date is not correct. Please write date in format: yyyy-m-d")
        else:
            return str(birthday.date())

    def __init__(self, year, month, day):
        self.__birthday = self.sanitize_date(year, month, day)

    def __str__(self):
        return str(self.__birthday)

    def __repr__(self):
        return str(self.__birthday)

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, year, month, day):
        self.__birthday = self.sanitize_date(year, month, day)


class Mail(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    def __str__(self):
        return str(self.value)

    def check_mail(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, str(email)):
            return email
        else:
            raise ValueError

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = Mail.check_mail(value)


class Record:
    """ Class for record name or phones"""

    def __init__(self, name, phone=None, birthday=None, mail=None):
        if birthday:
            self.birthday = Birthday(*birthday)
        else:
            self.birthday = None
        self.name = name
        self.phone = Phone(phone)
        self.phones = list()
        self.mail = mail
        if isinstance(phone, Phone):
            self.phones.append(phone)

    def add_phone(self, phone):
        phone = Phone(phone)
        if phone.value:
            lst = [phone.value for phone in self.phones]
            if phone.value not in lst:
                self.phones.append(phone)
                return "Phone was added"
        else:
            raise ValueError("Phone number is not correct")

    def change(self, old_phone, new_phone):
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)

        for phone in self.phones:
            if phone.value == old_phone.value:
                self.phones.remove(phone)
                self.phones.append(new_phone)
                return f'{old_phone} to {new_phone} changed'
            else:
                return print(f"Phone {old_phone} not found in the Record")

    def remove_phone(self, phone_num):
        phone = Phone(phone_num)

        for ph in self.phones:
            if ph.value == phone.value:
                self.phones.remove(ph)
                return f'Phone {phone_num} deleted'
            else:
                return f'Number {phone_num} not found'

    def add_user_birthday(self, year, month, day):
        self.birthday = Birthday.sanitize_date(int(year), int(month), int(day))

    def add_mail(self, mail):
        if not self.mail:
            self.mail = Mail(mail)
        else:
            raise WrongMail

    def del_mail(self):
        self.mail = None

    def chang_mail(self, mail):
        self.mail = Mail(mail)

    # def days_to_birthday(self):
    #     current_date = datetime.now().date()
    #     current_year = current_date.year
    #     if self.birthday:
    #         birth_date = self.birthday.value.date().replace(year=current_year)
    #         if birth_date >= current_date:
    #             delta = birth_date - current_date
    #         else:
    #             delta = birth_date.replace(year=current_year + 1) - current_date
    #         return f"{delta.days} days left until {self.name}'s birthday"
    #     else:
    #         return f'The birthday of the contact {self.name} is not set'

    def days_to_birthday(self):
        cur_date = datetime.now().date()
        cur_year = cur_date.year

        if self.birthday is not None:
            birthday = datetime.strptime(self.birthday, '%Y-%m-%d')
            this_year_birthday = datetime(cur_year, birthday.month, birthday.day).date()
            delta = this_year_birthday - cur_date
            if delta.days >= 0:
                return f"{self.name}'s birthday will be in {delta.days} days"
            else:
                next_year_birthday = datetime(cur_year + 1, birthday.month, birthday.day).date()
                delta = next_year_birthday - cur_date
                return f"{self.name}'s birthday will be in {delta.days} days"
        else:
            return f"{self.name}'s birthday is unknown"


ADDRESSBOOK = AddressBook()