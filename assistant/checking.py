import re
from datetime import datetime


class Checking:
    def check(self, *args):
        raise NotImplementedError


class NameCheck(Checking):
    def check(self, name):
        """Normalize names from cyrillic to latin"""
        cyrillic_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
        translations = ("a", "b", "v", "g", "d", "e", "e", "j", "z",
                        "i", "j", "k", "l", "m", "n", "o", "p", "r",
                        "s", "t", "u", "f", "h", "ts", "ch", "sh",
                        "sch", "", "y", "", "e", "yu", "ya", "je",
                        "i", "ji", "g")
        trans = {}
        for i, j in zip(cyrillic_symbols, translations):
            trans[ord(i)] = j
            trans[ord(i.upper())] = j.upper()
            name_list = name.split(".")
            name_list[0] = name_list[0].translate(trans)
            name_list[0] = re.sub("\W+", "_", name_list[0])
            name = f"{name_list[0]}.{name_list[1]}"
        return name


class PhoneCheck(Checking):
    def check(self, phone):
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
            raise "Entered phone number has some mistakes. Check it and try again"
        else:
            new_phone = "".join(new_phone)
            if len(new_phone) == 12:
                return f"+{new_phone}"
            elif len(new_phone) == 10:
                return f"+38{new_phone}"
            else:
                return "Wrong length of phone number. Must be 10 or 12 symbols"


class BirthdayCheck(Checking):
    def check(self, year, month, day):
        try:
            birthday = datetime(year=year, month=month, day=day)
        except ValueError:
            return "Wrong format of birthday. Enter birthday in format yyyy-mm-dd"
        else:
            return str(birthday.date())


class MailCheck(Checking):
    def check(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, str(email)):
            return email
        else:
            raise ''
