from addressbook_classes import WrongTypePhone, WrongLenPhone, WrongMail


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Give me name, old phone and new phone"
        except KeyError:
            return "Enter correct username"
        except ValueError:
            return "Incorrect input. Try again"
        except TypeError:
            return "Not enough params for command"
        except WrongLenPhone:
            return "Length of phone's number is wrong"
        except WrongTypePhone:
            return 'Incorrect phone number'
        except WrongMail:
            return 'User already have email. You can only change or delete'

    return wrapper