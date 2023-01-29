# CLI ASSISTANT
<b>CLI Assistant</b> is a python program that acts as a personal assistant with a command line interface.  The project is installed as a python package and can be called anywhere on the system using a special command.

The following python libraries were also used for implementation: <b>pathlib, os, re, shutil, sys, datetime, collections, pickle</b>.
## Installation

Download package, unpack it and use next command to install it from unpacked folder: `pip install -e`.

## Description

After starting the program, the user has a choice of what he wants to work with:
 - SORT DIRECTORY
 - ADDRESSBOOK
 - NOTEBOOK
 
 After choosing one of the three scripts, the user proceeds to direct work with the selected script.

### SORT DIRECTORY

This script allows the user to sort files by the following categories:
- "images": [".jpeg", ".png", ".jpg", ".svg", “.bmp”], 
- "documents": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx", “.rtf”], 
-"audio": [".mp3", ".ogg", ".wav", ".amr"], 
- "video": [".avi", ".mp4", ".mov", ".mkv"], 
- "archives": [".zip", ".gz", ".tar", “.rar”, '.7z' ] 
- "programming": [".php", ".js", ".py", ".html", ".css"]

 During sorting, the script unzips all archives and then places them together with other files into new folders - 'images', 'documents', 'audio', 'video', 'archives'.
 
 Runs the script using the command: `clean-folder {folder path}`
 
 ### ADDRESSBOOK
 
With the help of this script, the user can maintain an address book. It opens up opportunities to create, edit and delete information about contacts.  Also, all user actions are saved to a file using pickle, so contact data is not lost with each new launch.

To work with the script, you need to use the following commands:
- `add contact` - add new contact. Input user name and phone

**Example:** `add contact User_name 095-xxx-xx-xx`

- `add address` - add user address to contact. Input user name and address

**Example:** `add address User_name User_address`
- `add birthday` - add birthday to contact. Input user name and birthday in format yyyy-mm-dd

**Example:** `add User_name 1971-01-00`
- `add mail` - add e-mail address to contact. Input user name and e-mail

**Example:** `add mail User_name user123@gmail.com`
- `birthday soon` - command to display birthdays in a given interval (N-days)

**Example:** `birthday soon 7`
- `change address` - change user address. Input user name and address

**Example:** `change address User_name User_new_address`
- `change mail` - change user e-mail address. Input user name and e-mail

**Example:** `change mail User_name user123@gmail.com`
- `change phone` - change users old phone to new phone. Input user name, old phone and new phone

**Example:** `change User_name 095-xxx-xx-xx 050-xxx-xx-xx`
- `delete address` - delete user address from contact. Input user name

**Example:** `delete address User_name`
- `delete mail` - delete user e-mail address from contact. Input user name

**Example:** `delete mail User_name`
- `delete user` - delete contact (name and phones). Input user name

**Example:** `delete contact User_name`
- `delete phone` - delete phone of some User. Input user name and phone

**Example:** `delete phone User_name 099-xxx-xx-xx`
- `hello/hi` - greeting command to start working with the bot
- `help` - command for output helptext
- `phone` - show contacts of input user. Input user name

**Example:** `phone User_name`
- `search` - keyword search. Input keywords that you want

**Example:** `search KeyWord`
- `show all` - show all contacts

**Example:** `show all`
- `show list` - show list of contacts which contains N-users

**Example:** `show list 5` 
- `when celebrate` - show days to birthday of User/ Input user name

**Example:** `when celebrate User_name`
- `exit`/`bye`/`good bye`/`close` - exit bot

**Example:** `good bye`

### NOTEBOOK
This script helps the user to create, edit and delete notes and also provides the option to add tags to them.  In addition, the script can be used to search for notes or tags.  All your information will be stored in a file with pickle and will not be lost after exiting the program.

To work with the script, you need to use the following commands:

- `add` - add new note. Input note text and then input tag or tags (key words)

**Example:** `add`
- `change` - command for change existing note. Input note number and then input new text

**Example:** `change`
- `delete` - command for delete note. Input note number

**Example:** `delete 1`
- `find note` - command to find notes. Input note text that you want to find

**Example:** `find note KeyWord`
- `find tag` - command to find notes by tag. Input tag that you want to find
    
**Example:** `find tag Tag`
- `hello`/`hi` - greeting command to start working with the bot
- `help` - command for output helptext
- `show all` - show all notes

**Example:** `show all`
- `exit`/`bye`/`good bye`/`close` - exit bot
    
**Example:** `good bye`










