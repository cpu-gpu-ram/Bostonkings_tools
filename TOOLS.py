
#Hello this is a summarey of all my tools this is a free to use resource



#ALL NESSECARY PACKAGES
import shlex
import sys
import os
import subprocess
import platform
import getpass
import pathlib
import shutil
import time
import datetime
import zipfile

#import all the otther projects
def Greeter():
    print(r""""
    __  __
  /  |/  | _  _
 / /| /| |/ // /
/_/ |_/  |_/  /
         /__/
   ______   ______   ______   __       ______
  /_  __/  / __  /  / __  /  /_/      / ____/
   / /    / /  / / / /  / / / /      _\___ \
  / /    / /__/ / / /__/ / / /___   /____/ /
 /_/    /______/ /______/ /_____/  /______/""")
    print(r"""
Welcome select the number that matchs the tool that u wish to use
before using this please read the read me for help in Py-Shell and any other tool type sos/help
check out my profile at: https://github.com/cpu-gpu-ram
emergency exit Ctrl c""")
    print(r"""
1.Py-Shell-human readable shell cover
Quit = Q""")



def PyShell():
    #copy and paste from my py-shell repo
    print(r"""
    ____             ____  _          _ _
    |  _ \ _   _     / ___|| |__   ___| | |
    | |_) | | | |____\___ \| '_ \ / _ \ | |
    |  __/| |_| |_____|__) | | | |  __/ | |
    |_|    \__, |    |____/|_| |_|\___|_|_|
            |____|
    V2.3

    """)
    #greets the user
    programs_list = []
    print(f"Welcome to Py-Shell! , {getpass.getuser()}" \
    "\nThis program will translate your commands into shell/bash." \
        "\nType 'exit' to quit the program.")

    #list all files in the directory
    def ls():
        files = os.listdir('.')
        for file in files:
            print(file)

    #changes the directory (needs to be updated) for one line cmd with out losing compatablity for thee old way

    def cd(path=None):
        if path is None:
            path = input('What directory/path ?')
        if path == 'home':
            path = os.path.expanduser('~')
        try:
            os.chdir(path)
            print(f"Changed directory to {path}")
        except FileNotFoundError:
            print(f"Directory {path} not found.")
    #makes new directory needs to be updated for one line cmd

    def mkdir(path =None):
        if path is None:
            path = input("What's the name ?")
        try:
            os.mkdir(path)
            print(f"Directory {path} created.")
        except FileExistsError:
            print(f"Directory {path} already exists.")

    #deletes an empty directory need to update so it can delete a full directory in one cmd

    def rmdir(path =None):
        if path is None:
            path = input("What's the name ?")
        try:
            os.rmdir(path)
            print(f"Directory {path} removed.")
        except FileNotFoundError:
            print(f"Directory {path} not found.")
        except OSError:
            print(f"Directory {path} is not empty.")

    #copies file need to update for one cmd to copy

    def cp(src =None, dst =None):
        if src is None:
            src = input("What's the name ?")
            dst = input("What the desintation ? (path/folder name)")
        try:
            shutil.copy(src, dst)
            print(f"File {src} copied to {dst}.")
        except shutil.Error:
            print(f"Failed to copy {src} to {dst}.")

    #moves file need to update for one cmd to copy

    def mv(src =None, dst =None):
        if src is None:
            src = input("What's the name ?")
            dst = input("What the desintation ? (path/folder name)")

        try:
            shutil.move(src, dst)
            print(f"File {src} moved to {dst}.")
        except shutil.Error:
            print(f"Failed to move {src} to {dst}.")

    #removes file need to update for one cmd to copy

    def rm(path =None):
        if path is None:
            path = input("What's the name ?")

        try:
            os.remove(path)
            print(f"File {path} removed.")
        except FileNotFoundError:
            print(f"File {path} not found.")

    #repeats the users input until crash

    def yes():
        usr_input = input()
        while True:
            print(usr_input)


    #outputs uername

    def who_am_i():
        print(f"User: {os.getlogin()}")

    #clears terminal

    def clr():
        if sys.platform.startswith('win'):
            os.system('cls')
        else:
            os.system('clear')

    #outputs current user directorys file tree

    def file_tree():
        for root, dirs, files in os.walk('.'):
            level = root.replace(os.getcwd(), '').count(os.sep)
            indent = ' ' * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                print(f"{subindent}{file}")

    #Shows disk space

    def disk():
        if shutil.disk_usage('.'):
            total, used, free = shutil.disk_usage('.')
            print(f"Total: {total // (2**30)} GB")
            print(f"Used: {used // (2**30)} GB")
            print(f"Free: {free // (2**30)} GB")

    #search current directory for keyword

    def search(keyword =None):
        if keyword is None:
            keyword = input("What we looking for boss ? ")

        found = False
        for root, dirs, files in os.walk('.'):
            for file in files:
                if keyword.lower() in file.lower():
                    print(os.path.join(root, file))
                    found = True
        if not found:
            print(f"No files found matching '{keyword}'.")

    #fetchs system info

    def fff():
        print("Fetching data...")
        time.sleep(2)
        print("Data fetched successfully!")
        print(platform.platform())
        print(f"Python version: {platform.python_version()}")
        print(f"User: {getpass.getuser()}")
        print(f"Current working directory: {os.getcwd()}")
        print(f"System architecture: {platform.architecture()[0]}")
        print(f"Processor: {platform.processor()}")
        print(f"Machine: {platform.machine()}")
        print(f"Node: {platform.node()}")
        print(f"System: {platform.system()}")
        print(f"Release: {platform.release()}")
        print(f"Version: {platform.version()}")
        print(';)')

    #command history

    def log():
        print(history)

    #reads out files

    def peek(file_name =None):
        if file_name is None:
            file_name = input("What's the name ?")

        try:
            print(open(file_name).read())
        except FileNotFoundError:
            print(f"File {file_name} not found.")

    #get system date and time


    def date():
        now = datetime.datetime.now()
        print(f"Current date and time: {now}")

    #Shows basic info about a file

    def file_info(file_name =None):
        if file_name is None:
            file_name = input("What's the name ?")

        try:
            file_path = pathlib.Path(file_name)
            print(f"File name: {file_path.name}")
            sizeinbytes = file_path.stat().st_size
            if sizeinbytes < 2**10:
                print(f"File size: {sizeinbytes} bytes")
            elif sizeinbytes < 2**20:
                print(f"File size: {sizeinbytes // 2**10} KB")
            elif sizeinbytes < 2**30:
                print(f"File size: {sizeinbytes // 2**20} MB")
            else:
                print(f"File size: {sizeinbytes // 2**30} GB")
            print(f"File created: {datetime.datetime.fromtimestamp(file_path.stat().st_ctime)}")
            print(f"File modified: {datetime.datetime.fromtimestamp(file_path.stat().st_mtime)}")
        except FileNotFoundError:
            print(f"File {file_name} not found.")

    #Should print all commands

    def help():
        print("""
        ============ PY-SHELL COMMANDS ============

        FILE MANAGEMENT
        ls / list files / files       - list files in current directory
        cd / change directory         - change directory
        mkdir / make folder           - create new directory
        rmdir / remove directory      - delete empty directory
        cp / copy                     - copy a file
        mv / move / rename            - move or rename a file
        rm / remove / destroy         - delete a file
        tree / file tree              - show directory tree

        FILE VIEWING
        peek / cat                    - read a text file
        file info                     - show file size and dates
        search                        - search for files by name

        SYSTEM
        fff / fakefastfetch           - show system info
        disk / space                  - show disk usage
        who am i / identity           - show current user
        time                          - show current date and time
        clr / clear                   - clear the screen

        NETWORK
        ping / connect                - ping an ip or domain

        PROGRAMS
        raw / bash / shell / terminal - run any bash command directly

        ARCHIVE
        zip / archive                 - zip a folder
        unzip / unarchive             - extract a zip file

        MISC
        calc                          - basic calculator
        log / history                 - show command history
        !! / last command             - repeat last command
        yes / repeat / loop           - repeat input forever
        help / sos / save me          - show this menu
        exit                          - quit Py-Shell

        ===========================================
        """)

    #checks if a site/ip is up

    def Ping(ipdomain =None):
        if ipdomain is None:
            ipdomain = input("What's the name ?")

        print('-'*60)
        if not ipdomain or ' ' in ipdomain or '.' not in ipdomain:
            print ('INVALID INPUT TRY AGIAN.')
            print('-'*60)
            return1 = False
        else:
            return1 = True
            if not sys.platform.startswith('win'):
                flag = '-c'
            else:
                flag = '-n'
            pingcommand =  ['ping' , flag, '1', ipdomain]
            result = subprocess.run(pingcommand, capture_output=True, text=True)
            if return1 == True:
                print (result.stdout)
            else:
                print ('cant reach')

    #my alternative to the up arrow on windows

    def up():
        if len(history) < 2:
            print('No history yet.')
        else:
            print(history[-2])

    #zips a file

    def zipfunc():
        zip_name = input('Enter zip file name (include .zip): ')
        zip_dir = input('Enter folder to zip: ')
        with zipfile.ZipFile(zip_name, 'w') as z:
            for root, dirs, files in os.walk(zip_dir):
                for file in files:
                    z.write(os.path.join(root, file))
        print(f"Zipped {zip_dir} into {zip_name}.")

    #unzips a file

    def unzip():
        zip_name = input('Enter zip file name to extract: ')
        extract_dir = input('Enter folder to extract to: ')
        with zipfile.ZipFile(zip_name, 'r') as contents:
            contents.extractall(extract_dir)
        print(f"Extracted {zip_name} to {extract_dir}.")

    def raw(cmd=None):
        if cmd is None:
            cmd = input("Enter command: ")
        os.system(cmd)

    #My second project ever basic two digit calc

    def calc():
        try:
            A = int(input('1st number = '))
            B = int(input('2nd number = '))
        except ValueError:
            print('Numbers only please.')
            return
        op = input('operation + - * / = ')
        if op == '+':
            ans = A + B
        elif op == '-':
            ans = A - B
        elif op == '/':
            ans = A / B
        elif op == '*':
            ans = A * B
        else:
            print('invalid input')
            return
        print(f'Answer is {ans}')
    #Command dictionary
    commands = {
    #File managment
        'ls': ls,
        'list files': ls,
        'files': ls,
        'current': ls,
        'cd': cd,
        'change folder': cd,
        'change directory': cd,
        'switch directory': cd,
        'switch folder': cd,
        'mkdir': mkdir,
        'make folder': mkdir,
        'make directory': mkdir,
        'new folder': mkdir,
        'new directory': mkdir,
        'rmdir': rmdir,
        'remove folder': rmdir,
        'remove directory': rmdir,
        'destroy folder': rmdir,
        'destroy directory': rmdir,
        'cp': cp,
        'copy': cp,
        'copy file': cp,
        'copy files': cp,
        'duplicate': cp,
        'reproduce':cp,
        'mv': mv,
        'move': mv,
        'move file': mv,
        'move files': mv,
        'rename': mv,
        'transport': mv,
        'rm': rm,
        'remove': rm,
        'remove file': rm,
        'remove files': rm,
        'destroy files': rm,
            'destroy file': rm,
            'destroy': rm,


        'yes': yes,
        'repeat': yes,
        'loop': yes,
        'who am i': who_am_i,
        'identity': who_am_i,


        'clr': clr,
        'clear': clr,
        'file tree': file_tree,
            'tree': file_tree,


        'disk': disk,
        'space': disk,


        'search': search,


        'fff': fff,
        'fake fast fetch': fff,
            'fakefastfetch': fff,


        'log': log,
        'history': log,
        'cmd': log,

        'cat': peek,
        'peek': peek,

        'time': date,

        'file info': file_info,
        'help': help,
        'sos':help,
        'save me': help,
        'connect':Ping,
        'ping': Ping,
        '!!': up,
        'zip': zipfunc,
        'archive': zipfunc,
        'unzip': unzip,
        'unarchive': unzip,
        'raw': raw,
        'bash': raw,
        'shell': raw,
        'terminal': raw,
        'calc': calc,
    }


    history = [ ]
    while True:
        print(os.getcwd())
        command = input(f"{getpass.getuser()}@{platform.node()} - ")

        if command.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        try:
            parts = shlex.split(command)
        except ValueError:
            print("Invalid input.")
            continue

        if not parts:
            continue

        history.append(command)

        # check longest match first
        matched = False
        for i in range(len(parts), 0, -1):
            candidate = ' '.join(parts[:i]).lower()
            if candidate in commands:
                commands[candidate](*parts[i:])
                matched = True
                break

        if not matched:
            print("Command not recognized. Please try again.")




def organizer(target_dir=None):
    # Prompt if no directory given
    if target_dir is None:
        target_dir = input("What folder would you like to organize? (Leave blank for current): ").strip()
        if not target_dir:
            target_dir = os.getcwd()

    target_path = Path(target_dir).expanduser().resolve()

    # Verify folder exists
    if not target_path.is_dir():
        print(f"Error: '{target_path}' is not a valid directory.")
        return

    categories = {
        "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.csv'],
        "Audio": ['.mp3', '.wav', '.aac'],
        "Video": ['.mp4', '.mkv', '.mov'],
        "Archives": ['.zip', '.rar', '.tar', '.7z'],
    }

    # Build a fast extension -> category lookup
    ext_to_category = {
        ext: cat for cat, exts in categories.items() for ext in exts
    }

    for item in target_path.iterdir():
        # Skip directories
        if item.is_dir():
            continue

        # Never touch the script itself
        if item.name == "TOOLS.py":
            continue

        ext = item.suffix.lower()
        category = ext_to_category.get(ext)
        if category is None:
            continue  # Unrecognized extension, leave it alone

        dest_dir = target_path / category
        dest_dir.mkdir(exist_ok=True)

        dest_path = dest_dir / item.name

        # Resolve naming conflicts with a counter suffix
        if dest_path.exists():
            stem, suffix = item.stem, item.suffix
            counter = 1
            while dest_path.exists():
                dest_path = dest_dir / f"{stem}_{counter}{suffix}"
                counter += 1

        try:
            shutil.move(str(item), str(dest_path))
            print(f"Moved: {item.name} -> {category}/{dest_path.name}")
        except (PermissionError, OSError) as e:
            print(f"Could not move '{item.name}': {e}")
            continue

    print("Organizing complete.")

#main loop
switch = True
while switch == True:
    Greeter()
    command = input()
    if command == 'q':
        switch = False
    elif command == '1':
        PyShell()
    elif command == '2':
        organizer()
    else:
        print('invaild input fuck you read to docs')
        time.sleep(5)
