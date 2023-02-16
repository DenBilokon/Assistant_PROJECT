from addressbook_classes import *


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough parameters to execute the command"
        except KeyError:
            return "Enter correct username"
        except ValueError:
            return "Try again. Enter your contacts name"
        except TypeError:
            return "Not enough parameters to execute the command"
        except PhoneLengthError:
            return "Wrong length of phone number. Must be 10 or 12 symbols"
        except PhoneError:
            return "Entered phone number has some mistakes. Check it and try again"
        except MailTypeError:
            return "Wrong type of email. Check it and try again"
        except MailExistError:
            return "User already has email. You can only change or delete"
        except AddressTypeError:
            return "Wrong address type. Check it and try again"
        except AddressExistError:
            return "User already has address. You can only change or remove"
        except PhoneMissing:
            return "Phone number is not found. Please try again"
        except UserMissing:
            return "User is not found. Please try again"
        except BirthdayDateError:
            return "Wrong date of birthday. Check and try again"
        except BirthdayTypeError:
            return "Wrong format of birthday. Enter birthday in format yyyy-mm-dd"
        except UnknownCommand:
            return "Unknown command. Press 'help' to see HELP DESK"
        except ElseError:
            return "Something went wrong. Please try again"

    return wrapper
