from checking import NameCheck
from pathlib import Path
from pretty_view import SortDirView
import os
import shutil


class SortDirectory:

    def __init__(self):
        self.x = SortDirView()
        self.name = NameCheck()

    def sort_create_files(self, start_path):
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
                        new_name = os.path.join(root, self.name.check(file))
                        os.rename(txt_path, new_name)
                        txt_path = new_name
                        shutil.move(txt_path, dir_images)
                        (known_extensions.append(list_files[-1]))
                    elif list_files[-1].upper() in list_video:
                        new_name = os.path.join(root, self.name.check(file))
                        os.rename(txt_path, new_name)
                        txt_path = new_name
                        shutil.move(txt_path, dir_videos)
                        known_extensions.append(list_files[-1])
                    elif list_files[-1].upper() in list_music:
                        new_name = os.path.join(root, self.name.check(file))
                        os.rename(txt_path, new_name)
                        txt_path = new_name
                        shutil.move(txt_path, dir_music)
                        known_extensions.append(list_files[-1])
                    elif list_files[-1].upper() in list_documents:
                        new_name = os.path.join(root, self.name.check(file))
                        os.rename(txt_path, new_name)
                        txt_path = new_name
                        shutil.move(txt_path, dir_documents)
                        known_extensions.append(list_files[-1])
                    elif list_files[-1].upper() in list_programming:
                        new_name = os.path.join(root, self.name.check(file))
                        os.rename(txt_path, new_name)
                        txt_path = new_name
                        shutil.move(txt_path, dir_programming)
                        known_extensions.append(list_files[-1])
                    elif list_files[-1].upper() in list_archives:
                        filename = self.name.check(file)
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
                        new_name = os.path.join(root, self.name.check(file))
                        os.rename(txt_path, new_name)
                        txt_path = new_name
                        shutil.move(txt_path, dir_others)
                        unknown_extensions.append(list_files[-1])
                finally:
                    continue

        """Delete folders after removing"""
        for direct in Path(start_path).glob("*"):
            if direct.is_dir() and direct.name not in name_of_dirs:
                try:
                    shutil.rmtree(direct, ignore_errors=True)
                except PermissionError:
                    print("Permission error for delete", direct)

        print('\n------------------------- File sorting is done successfully! -------------------------\n')
        result = ["\n".join(i for i in known_extensions), "\n".join(i for i in unknown_extensions)]
        return print(self.x.create_row(result))


def run_sort():
    try:
        start_path = input('Input path: ')
        x = SortDirectory()
        x.sort_create_files(start_path)
        while True:
            b = input("\nDo you want to sort something else? (y/n)\n>>>> ")
            if b == "y":
                a = str(input('Input path: '))
                x = SortDirectory()
                x.sort_create_files(a)
                continue
            if b == "n":
                print("Goodbye!")
                break
            else:
                print("The answer must be y/n")
    except (IndexError, FileNotFoundError):
        print("Please input correct path to sort folder")
        pass


if __name__ == '__main__':
    run_sort()
