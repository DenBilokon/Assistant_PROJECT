from pathlib import Path
import os
import re
import shutil


def normalize_names(name):
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


def sort_create_files(start_path):
    """create dirs"""
    dir_images = os.path.join(start_path, "images")
    dir_videos = os.path.join(start_path, "videos")
    dir_music = os.path.join(start_path, "music")
    dir_documents = os.path.join(start_path, "documents")
    dir_archives = os.path.join(start_path, "archives")
    dir_programming = os.path.join(start_path, "programming")
    dir_others = os.path.join(start_path, "others")
    list_of_dirs = [dir_images, dir_videos, dir_documents, dir_music, dir_archives, dir_others]
    name_of_dirs = ["images", "videos", "music", "documents", "archives", "others"]
    for direct in list_of_dirs:
        try:
            os.mkdir(direct)
        except FileExistsError:
            pass
    """Removing and renaming files"""
    list_image = ('JPEG', 'PNG', 'JPG', 'SVG', 'BMP')
    list_video = ('AVI', 'MP4', 'MOV', 'MKV')
    list_documents = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'RTF', 'XLS')
    list_music = ('MP3', 'OGG', 'WAV', 'AMR')
    list_archives = ('ZIP', 'GZ', 'TAR', 'RAR', '7Z')
    list_programming = ('PY', 'PHP', 'HTML', 'JS', 'CSS')
    known_extensions = []
    unknown_extensions = []
    for root, subFolders, files in os.walk(start_path):
        for file in files:
            try:
                txt_path = os.path.join(root, file)
                list_files = file.rsplit(".")
                if list_files[-1].upper() in list_image:
                    new_name = os.path.join(root, normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, dir_images)
                    (known_extensions.append(list_files[-1]))
                elif list_files[-1].upper() in list_video:
                    new_name = os.path.join(root, normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, dir_videos)
                    known_extensions.append(list_files[-1])
                elif list_files[-1].upper() in list_music:
                    new_name = os.path.join(root, normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, dir_music)
                    known_extensions.append(list_files[-1])
                elif list_files[-1].upper() in list_documents:
                    new_name = os.path.join(root, normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, dir_documents)
                    known_extensions.append(list_files[-1])
                elif list_files[-1].upper() in list_programming:
                    new_name = os.path.join(root, normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, dir_programming)
                    known_extensions.append(list_files[-1])
                elif list_files[-1].upper() in list_archives:
                    filename = normalize_names(file)
                    new_name = os.path.join(root, filename)
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    os.mkdir(os.path.join(dir_archives, os.path.splitext(filename)[0]))
                    shutil.move(txt_path, os.path.join(dir_archives, os.path.splitext(filename)[0]))
                    txt_path = os.path.join(dir_archives, os.path.splitext(filename)[0], filename)
                    try:
                        shutil.unpack_archive(txt_path, os.path.join(dir_archives, os.path.splitext(filename)[0]))
                    except (ValueError, shutil.ReadError):
                        pass
                    known_extensions.append(list_files[-1])
                else:
                    os.path.join(dir_others, file)
                    new_name = os.path.join(root, normalize_names(file))
                    os.rename(txt_path, new_name)
                    txt_path = new_name
                    shutil.move(txt_path, dir_others)
                    unknown_extensions.append(list_files[-1])
            finally:
                continue

    print('\n------------------------- File sorting is done successfully! -------------------------\n')
    print("Known_extensions - ", known_extensions)
    print("Unknown_extensions - ", unknown_extensions)

    """Delete folders after removing"""
    for direct in Path(start_path).glob("*"):
        if direct.is_dir() and direct.name not in name_of_dirs:
            try:
                shutil.rmtree(direct, ignore_errors=True)
            except PermissionError:
                print("Permission error for delete", direct)


def run_sort():
    try:
        sort_create_files(input('Input path: '))
        while True:
            b = input("\nDo you want to sort something else? (yes/no)\n>>>> ")
            if b == "yes":
                a = input('Input path: ')
                sort_create_files(a)
                continue
            if b == "no":
                print("Goodbye!")
                break
            else:
                print("The answer must be 'yes' or 'no'!")
    except (IndexError, FileNotFoundError):
        print("Please input correct path to sort folder")
        pass


if __name__ == '__main__':
    run_sort()
