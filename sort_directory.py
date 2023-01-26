import os
import re
import shutil


def sort_folder(path):
    def normalize(name):

        CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
        TRANSLATION = (
        "a", "b", "v", "g", "d", "e", "e", "zh", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
        "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

        TRANS = {}

        for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
            TRANS[ord(c)] = l
            TRANS[ord(c.upper())] = l.upper()

        new_name = name.translate(TRANS)

        new_name = re.sub("[^a-zA-Z0-9 \n\.]", "_", new_name)

        return new_name

    if not path:
        return 'Please enter a folder path!'
    elif os.path.exists(path) != True:
        return 'Please enter a correct folder path!'

    basepath = os.path.abspath(path)

    CATEGORIES = {
        "images": [".jpeg", ".png", ".jpg", ".svg"],
        "documents": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"],
        "audio": [".mp3", ".ogg", ".wav", ".amr"],
        "video": [".avi", ".mp4", ".mov", ".mkv"],
        "archives": [".zip", ".gz", ".tar"]
    }

    for keys in list(CATEGORIES):
        target = f"{basepath}/{keys.capitalize()}"
        if not os.path.exists(target):
            os.mkdir(target)

    for root, dirs, files in os.walk(basepath, topdown=False):
        for dir in dirs:
            os.rename(os.path.join(root, dir),
                      os.path.join(root, normalize(dir)))

    for root, dirs, files in os.walk(basepath):
        for file in files:
            if os.path.splitext(file)[1].lower() in CATEGORIES["images"]:
                os.replace(f"{root}/{file}", f"{basepath}/Images/{normalize(file)}")
            elif os.path.splitext(file)[1].lower() in CATEGORIES["documents"]:
                os.replace(f"{root}/{file}", f"{basepath}/Documents/{normalize(file)}")
            elif os.path.splitext(file)[1].lower() in CATEGORIES["audio"]:
                os.replace(f"{root}/{file}", f"{basepath}/Audio/{normalize(file)}")
            elif os.path.splitext(file)[1].lower() in CATEGORIES["video"]:
                os.replace(f"{root}/{file}", f"{basepath}/Video/{normalize(file)}")
            elif os.path.splitext(file)[1].lower() in CATEGORIES["archives"]:
                os.replace(f"{root}/{file}", f"{basepath}/Archives/{normalize(file)}")
                shutil.unpack_archive(f"{basepath}/Archives/{file}", f"{basepath}/Archives/{os.path.splitext(file)[0]}")

    for root, dirs, files in os.walk(basepath, topdown=False):
        if not files:
            try:
                os.rmdir(root)
            finally:
                continue

    return f"Folder '{path}' has been sorted"