
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
import hashlib
import random
import socket

#progress bar helper - used anywhere a loop might take a noticeable amount of time
def progress_bar(current, total, prefix='', length=30):
    if total <= 0:
        return
    current = min(current, total)
    filled = int(length * current // total)
    bar = '#' * filled + '-' * (length - filled)
    percent = (current / total) * 100
    sys.stdout.write(f"\r{prefix} |{bar}| {percent:5.1f}% ({current}/{total})")
    sys.stdout.flush()
    if current >= total:
        sys.stdout.write('\n')

#import all the otther projects
def Greeter():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')
    #BUG FIX: had 4 quotes (r"""") instead of 3, the extra " was printing a stray quote mark above the logo
    print(r"""
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
===============================================
1.Py-Shell          |       11.Grep-searches
2.Organizer         |       12.ToDo-list
3.Dupe Finder       |       13.Art
4.Bulk Renamer      |       14.Calculator
5.Backup-zips       |       15.??????????
6.Cipher-caesar     |       16.???????????
7.Dir Sizes         |       17.??????????
8.Empty Folder      |       18.?????????
9.Ext Counter       |       19.????????????
10.Old Files        |       20.???????
================================================

Quit = Q                To Change directory = C""")               



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
        if path == 'home' or path == '~':
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
        #BUG FIX: os.getlogin() can throw OSError when there's no terminal attached, fall back to getpass
        try:
            print(f"User: {os.getlogin()}")
        except OSError:
            print(f"User: {getpass.getuser()}")

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

        #walk the tree once first so we know how many files we're checking, for the progress bar
        all_files = []
        for root, dirs, files in os.walk('.'):
            for file in files:
                all_files.append(os.path.join(root, file))

        found = False
        total = len(all_files)
        for i, file_path in enumerate(all_files, 1):
            file = os.path.basename(file_path)
            if keyword.lower() in file.lower():
                #BUG FIX: print after clearing the progress bar line so output doesn't get mangled
                print()
                print(file_path)
                found = True
            progress_bar(i, total, prefix='Searching')
        if total == 0:
            print("No files to search.")
        elif not found:
            print(f"No files found matching '{keyword}'.")

    #fetchs system info

    def fff():
        print("Fetching data...")
        steps = 20
        for i in range(steps + 1):
            progress_bar(i, steps, prefix='Fetching')
            time.sleep(0.1)
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
            print(open(file_name, errors='ignore').read())
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        except IsADirectoryError:
            print(f"{file_name} is a directory, not a file.")

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
        except OSError as e:
            print(f"Could not read info for {file_name}: {e}")

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
        head                          - show first N lines of a file
        tail                          - show last N lines of a file
        wc / word count               - count lines, words, characters
        diff / compare                - compare two files
        touch / new file              - create an empty file
        count files / file count      - count files in this directory
        bigfiles / big files          - find files over a size in MB

        SYSTEM
        fff / fakefastfetch           - show system info
        disk / space                  - show disk usage
        who am i / identity           - show current user
        time                          - show current date and time
        clr / clear                   - clear the screen
        env / environment             - list environment variables
        myip / my ip                  - show local network ip

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
        clear history / wipe history  - wipe the command history
        !! / last command             - repeat last command
        yes / repeat / loop           - repeat input forever
        note / journal                - append a timestamped note
        roll / dice                   - roll a dice
        genpass / password            - generate a random password
        countdown / timer             - countdown from N seconds
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
            print('INVALID INPUT TRY AGIAN.')
            print('-'*60)
            return

        if not sys.platform.startswith('win'):
            flag = '-c'
        else:
            flag = '-n'
        pingcommand = ['ping', flag, '1', ipdomain]
        try:
            result = subprocess.run(pingcommand, capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(result.stdout)
            else:
                print('cant reach')
        except FileNotFoundError:
            print("Ping command not available on this system.")
        except subprocess.TimeoutExpired:
            print("Ping timed out.")
        print('-'*60)

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
        #BUG FIX: this used to crash the whole program if zip_dir didn't exist
        if not os.path.isdir(zip_dir):
            print(f"Folder {zip_dir} not found.")
            return
        all_files = []
        for root, dirs, files in os.walk(zip_dir):
            for file in files:
                all_files.append(os.path.join(root, file))
        total = len(all_files)
        if total == 0:
            print(f"Folder {zip_dir} is empty, nothing to zip.")
            return
        with zipfile.ZipFile(zip_name, 'w') as z:
            for i, file_path in enumerate(all_files, 1):
                z.write(file_path)
                progress_bar(i, total, prefix='Zipping')
        print(f"Zipped {zip_dir} into {zip_name}.")

    #unzips a file

    def unzip():
        zip_name = input('Enter zip file name to extract: ')
        extract_dir = input('Enter folder to extract to: ')
        #BUG FIX: this used to crash the whole program if zip_name didn't exist or wasn't a real zip
        try:
            with zipfile.ZipFile(zip_name, 'r') as contents:
                members = contents.namelist()
                total = len(members)
                for i, member in enumerate(members, 1):
                    contents.extract(member, extract_dir)
                    progress_bar(i, total, prefix='Extracting')
            print(f"Extracted {zip_name} to {extract_dir}.")
        except FileNotFoundError:
            print(f"File {zip_name} not found.")
        except zipfile.BadZipFile:
            print(f"{zip_name} is not a valid zip file.")

    def raw(*cmd_parts):
        if cmd_parts:
            cmd = ' '.join(cmd_parts)
        else:
            cmd = input("Enter command: ")
        os.system(cmd)

    #creates a new empty file, or bumps the modified time if it already exists

    def touch(path=None):
        if path is None:
            path = input("What's the name ?")
        try:
            with open(path, 'a'):
                os.utime(path, None)
            print(f"Touched {path}.")
        except OSError as e:
            print(f"Could not touch {path}: {e}")

    #shows the first N lines of a file, defaults to 10

    def head(file_name=None, num_lines=None):
        if file_name is None:
            file_name = input("What's the name ?")
        if num_lines is None:
            num_lines = input("How many lines (blank for 10) ? ")
        if not num_lines:
            num_lines = '10'
        try:
            num_lines = int(num_lines)
        except ValueError:
            print("Enter a number.")
            return
        try:
            with open(file_name, errors='ignore') as f:
                for i, line in enumerate(f):
                    if i >= num_lines:
                        break
                    print(line, end='')
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        except IsADirectoryError:
            print(f"{file_name} is a directory, not a file.")

    #shows the last N lines of a file, defaults to 10

    def tail(file_name=None, num_lines=None):
        if file_name is None:
            file_name = input("What's the name ?")
        if num_lines is None:
            num_lines = input("How many lines (blank for 10) ? ")
        if not num_lines:
            num_lines = '10'
        try:
            num_lines = int(num_lines)
        except ValueError:
            print("Enter a number.")
            return
        try:
            with open(file_name, errors='ignore') as f:
                lines = f.readlines()
            for line in lines[-num_lines:]:
                print(line, end='')
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        except IsADirectoryError:
            print(f"{file_name} is a directory, not a file.")

    #counts lines, words, and characters in a file

    def wc(file_name=None):
        if file_name is None:
            file_name = input("What's the name ?")
        try:
            with open(file_name, errors='ignore') as f:
                text = f.read()
            lines = text.count('\n')
            words = len(text.split())
            chars = len(text)
            print(f"Lines: {lines}  Words: {words}  Characters: {chars}")
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        except IsADirectoryError:
            print(f"{file_name} is a directory, not a file.")

    #counts how many files sit in the current directory, not recursive

    def countfiles():
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        print(f"Files in this directory: {len(files)}")

    #lists environment variables

    def envvars():
        for key, value in os.environ.items():
            print(f"{key}={value}")

    #shows this machine's local network ip

    def myip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
            s.close()
            print(f"Local IP: {ip}")
        except OSError:
            print("Could not determine IP, are u connected to a network ?")

    #appends a quick timestamped note to notes.txt in the current folder

    def note(*text_parts):
        if text_parts:
            text = ' '.join(text_parts)
        else:
            text = input("What's the note ? ")
        try:
            with open('notes.txt', 'a') as f:
                f.write(f"[{datetime.datetime.now()}] {text}\n")
            print("Noted.")
        except OSError as e:
            print(f"Could not save note: {e}")

    #rolls a dice, defaults to 6 sides

    def diceroll(sides=None):
        if sides is None:
            sides = input("How many sides (blank for 6) ? ")
        if not sides:
            sides = '6'
        try:
            sides = int(sides)
            print(f"You rolled a {random.randint(1, sides)}")
        except ValueError:
            print("Enter a number.")

    #generates a random password, defaults to 12 characters

    def genpass(length=None):
        if length is None:
            length = input("How long (blank for 12) ? ")
        if not length:
            length = '12'
        try:
            length = int(length)
        except ValueError:
            print("Enter a number.")
            return
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"Password: {password}")

    #compares two files and says if they're identical or how many lines differ

    def diff(file1=None, file2=None):
        if file1 is None:
            file1 = input("First file ? ")
            file2 = input("Second file ? ")
        try:
            with open(file1, errors='ignore') as f1, open(file2, errors='ignore') as f2:
                content1 = f1.read()
                content2 = f2.read()
            if content1 == content2:
                print("Files are identical.")
            else:
                lines1 = content1.splitlines()
                lines2 = content2.splitlines()
                diff_count = sum(1 for a, b in zip(lines1, lines2) if a != b)
                diff_count += abs(len(lines1) - len(lines2))
                print(f"Files are different. {diff_count} line(s) differ.")
        except FileNotFoundError as e:
            print(f"File not found: {e.filename}")
        except IsADirectoryError as e:
            print(f"{e.filename} is a directory, not a file.")

    #finds files over a certain size (in MB) in the current directory tree, defaults to 50 MB

    def bigfiles(size_mb=None):
        if size_mb is None:
            size_mb = input("Show files over how many MB (blank for 50) ? ")
        if not size_mb:
            size_mb = '50'
        try:
            size_mb = float(size_mb)
        except ValueError:
            print("Enter a number.")
            return
        threshold = size_mb * (2**20)
        all_files = []
        for root, dirs, files in os.walk('.'):
            for file in files:
                all_files.append(os.path.join(root, file))

        found = False
        total = len(all_files)
        for i, file_path in enumerate(all_files, 1):
            try:
                size = os.path.getsize(file_path)
                if size > threshold:
                    print()
                    print(f"{file_path} - {size // (2**20)} MB")
                    found = True
            except OSError:
                pass
            progress_bar(i, total, prefix='Scanning')
        if total == 0:
            print("No files to scan.")
        elif not found:
            print(f"No files over {size_mb} MB found.")

    #wipes the command history list

    def clearhistory():
        history.clear()
        print("History cleared.")

    #fun countdown timer

    def countdown(seconds=None):
        if seconds is None:
            seconds = input("Countdown from how many seconds ? ")
        try:
            seconds = int(seconds)
        except ValueError:
            print("Enter a number.")
            return
        if seconds <= 0:
            print("Enter a number greater than 0.")
            return
        total = seconds
        remaining = seconds
        while remaining > 0:
            progress_bar(total - remaining, total, prefix=f'{remaining:>3}s')
            time.sleep(1)
            remaining -= 1
        progress_bar(total, total, prefix='  0s')
        print("Time's up!")

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

        'touch': touch,
        'create file': touch,
        'new file': touch,

        'head': head,
        'tail': tail,
        'wc': wc,
        'word count': wc,

        'count files': countfiles,
        'file count': countfiles,

        'env': envvars,
        'environment': envvars,

        'myip': myip,
        'my ip': myip,
        'ip': myip,

        'note': note,
        'journal': note,

        'roll': diceroll,
        'dice': diceroll,

        'genpass': genpass,
        'password': genpass,
        'generate password': genpass,

        'diff': diff,
        'compare': diff,

        'bigfiles': bigfiles,
        'big files': bigfiles,
        'find big files': bigfiles,

        'clear history': clearhistory,
        'wipe history': clearhistory,

        'countdown': countdown,
        'timer': countdown,
    }


    history = [ ]
    while True:
        print(os.getcwd())
        command = input(f"{getpass.getuser()}@{platform.node()} - ")

        if command.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            time.sleep(5)
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
                #BUG FIX: an unhandled error here used to crash the entire program, not just the command
                try:
                    commands[candidate](*parts[i:])
                except TypeError:
                    print("That command doesn't take extra words like that.")
                except Exception as e:
                    print(f"Something went wrong: {e}")
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

    target_path = pathlib.Path(target_dir).expanduser().resolve()

    # Verify folder exists
    if not target_path.is_dir():
        print(f"Error: '{target_path}' is not a valid directory.")
        time.sleep(5)
        return

    categories = {
        "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff', '.tif', '.heic', '.ico'],
        "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.csv', '.pptx', '.ppt',
                      '.odt', '.ods', '.odp', '.rtf', '.md', '.epub'],
        "Audio": ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma'],
        "Video": ['.mp4', '.mkv', '.mov', '.avi', '.wmv', '.flv', '.webm', '.m4v'],
        "Archives": ['.zip', '.rar', '.tar', '.7z', '.gz', '.bz2', '.xz', '.iso'],
        "Executables": ['.exe', '.msi', '.app', '.deb', '.rpm', '.dmg', '.apk', '.bin', '.appimage'],
        "Scripts_and_Code": ['.py', '.sh', '.bash', '.zsh', '.bat', '.ps1', '.js', '.ts', '.html',
                              '.css', '.json', '.xml', '.yaml', '.yml', '.c', '.cpp', '.h', '.java',
                              '.go', '.rs', '.rb', '.php', '.sql'],
        "Fonts": ['.ttf', '.otf', '.woff', '.woff2'],
    }

    # Build a fast extension -> category lookup
    ext_to_category = {
        ext: cat for cat, exts in categories.items() for ext in exts
    }

    # Catch-all bucket for any extension not explicitly listed above
    OTHER_CATEGORY = "Other"
    NO_EXTENSION_CATEGORY = "No_Extension"

    items = [item for item in target_path.iterdir() if not item.is_dir() and item.name != os.path.basename(__file__)]
    total = len(items)
    if total == 0:
        print("Nothing to organize here.")
        time.sleep(5)
        return

    for i, item in enumerate(items, 1):
        ext = item.suffix.lower()
        if not ext:
            category = NO_EXTENSION_CATEGORY
        else:
            category = ext_to_category.get(ext, OTHER_CATEGORY)

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
            print()
            print(f"Moved: {item.name} -> {category}/{dest_path.name}")
        except (PermissionError, OSError) as e:
            print()
            print(f"Could not move '{item.name}': {e}")
        progress_bar(i, total, prefix='Organizing')

    print("Organizing complete.")
    time.sleep(5)



def dupe_finder(target_dir=None):
    # Prompt if no directory given
    if target_dir is None:
        target_dir = input("What folder would you like to scan for duplicates? (Leave blank for current): ").strip()
        if not target_dir:
            target_dir = os.getcwd()

    target_path = pathlib.Path(target_dir).expanduser().resolve()

    # Verify folder exists
    if not target_path.is_dir():
        print(f"Error: '{target_path}' is not a valid directory.")
        time.sleep(5)
        return

    print("Scanning for duplicates, this might take a sec...")

    # Walk the tree once first so we know the total file count, for the progress bar
    all_files = []
    for root, dirs, files in os.walk(target_path):
        for file in files:
            if file != os.path.basename(__file__):
                all_files.append(os.path.join(root, file))

    # Group files by content hash, not by name, so renamed copies still get caught
    hashes = {}
    total = len(all_files)
    for i, file_path in enumerate(all_files, 1):
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
        except (PermissionError, OSError):
            progress_bar(i, total, prefix='Hashing')
            continue
        hashes.setdefault(file_hash, []).append(file_path)
        progress_bar(i, total, prefix='Hashing')

    dupes_found = False
    for file_hash, paths in hashes.items():
        if len(paths) > 1:
            dupes_found = True
            print("\nDuplicate set found:")
            for i, path in enumerate(paths, 1):
                print(f"  {i}. {path}")
            choice = input("Delete which ones? (numbers separated by spaces, blank to skip): ").strip()
            if not choice:
                continue
            for num in choice.split():
                try:
                    index = int(num) - 1
                    os.remove(paths[index])
                    print(f"Deleted {paths[index]}")
                except (ValueError, IndexError):
                    print(f"Skipped invalid choice: {num}")
                except OSError as e:
                    print(f"Could not delete: {e}")

    if not dupes_found:
        print("No duplicates found.")
    print("Duplicate scan complete.")
    time.sleep(5)



def bulk_rename(target_dir=None):
    # Renames every file in a folder to prefix + number, in order
    if target_dir is None:
        target_dir = input("What folder has the files to rename? (Leave blank for current): ").strip()
        if not target_dir:
            target_dir = os.getcwd()

    target_path = pathlib.Path(target_dir).expanduser().resolve()

    if not target_path.is_dir():
        print(f"Error: '{target_path}' is not a valid directory.")
        time.sleep(5)
        return

    prefix = input("Prefix to add (blank for none): ")
    start_num = input("Starting number (blank for 1): ").strip()
    try:
        counter = int(start_num) if start_num else 1
    except ValueError:
        print("Enter a number.")
        time.sleep(5)
        return

    files = sorted([f for f in target_path.iterdir() if f.is_file() and f.name != os.path.basename(__file__)])
    if not files:
        print("No files found.")
        time.sleep(5)
        return

    #BUG FIX: renaming files one by one in place could overwrite a not-yet-renamed file
    #if its target name happened to match. Renaming to unique temp names first avoids that.
    total = len(files)
    temp_paths = []
    for i, f in enumerate(files, 1):
        temp_path = target_path / f".__rename_tmp_{i}_{f.name}"
        try:
            f.rename(temp_path)
            temp_paths.append(temp_path)
        except OSError as e:
            print(f"Could not stage {f.name} for renaming: {e}")
        progress_bar(i, total, prefix='Staging')

    for i, temp_path in enumerate(temp_paths, 1):
        new_name = f"{prefix}{counter}{temp_path.suffix}"
        new_path = target_path / new_name
        try:
            temp_path.rename(new_path)
            print(f"Renamed -> {new_name}")
            counter += 1
        except OSError as e:
            print(f"Could not rename {temp_path.name}: {e}")
        progress_bar(i, len(temp_paths), prefix='Renaming')

    print("Bulk rename complete.")
    time.sleep(5)



def backup(target_dir=None):
    # Zips a whole folder up with a timestamp in the name so old backups don't get overwritten
    if target_dir is None:
        target_dir = input("What folder would you like to back up? (Leave blank for current): ").strip()
        if not target_dir:
            target_dir = os.getcwd()

    target_path = pathlib.Path(target_dir).expanduser().resolve()

    if not target_path.is_dir():
        print(f"Error: '{target_path}' is not a valid directory.")
        time.sleep(5)
        return

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{target_path.name}_backup_{timestamp}.zip"

    all_files = []
    for root, dirs, files in os.walk(target_path):
        for file in files:
            all_files.append(os.path.join(root, file))

    total = len(all_files)
    if total == 0:
        print("Nothing to back up here.")
        time.sleep(5)
        return

    try:
        with zipfile.ZipFile(backup_name, 'w') as z:
            for i, file_path in enumerate(all_files, 1):
                arcname = os.path.relpath(file_path, target_path)
                z.write(file_path, arcname)
                progress_bar(i, total, prefix='Backing up')
        print(f"Backed up {target_path} to {backup_name}.")
    except OSError as e:
        print(f"Backup failed: {e}")
    time.sleep(5)



def cipher():
    # Simple caesar cipher, encode or decode some text
    text = input("Text to encode/decode: ")
    shift_input = input("Shift amount (blank for 3): ").strip()
    try:
        shift = int(shift_input) if shift_input else 3
    except ValueError:
        print("Enter a number.")
        time.sleep(5)
        return

    mode = input("Encode or decode ? (e/d): ").strip().lower()
    if mode == 'd':
        shift = -shift

    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    print(f"Result: {result}")
    time.sleep(5)



def dir_sizes(target_dir=None):
    # Shows how big each file/folder inside a directory is, biggest first
    if target_dir is None:
        target_dir = input("What folder would you like to analyze? (Leave blank for current): ").strip()
        if not target_dir:
            target_dir = os.getcwd()

    target_path = pathlib.Path(target_dir).expanduser().resolve()

    if not target_path.is_dir():
        print(f"Error: '{target_path}' is not a valid directory.")
        time.sleep(5)
        return

    items = list(target_path.iterdir())
    total = len(items)
    if total == 0:
        print("Nothing here to measure.")
        time.sleep(5)
        return

    sizes = {}
    for i, item in enumerate(items, 1):
        if item.is_dir():
            total_size = 0
            for root, dirs, files in os.walk(item):
                for file in files:
                    try:
                        total_size += os.path.getsize(os.path.join(root, file))
                    except OSError:
                        continue
            sizes[item.name + "/"] = total_size
        elif item.is_file():
            try:
                sizes[item.name] = item.stat().st_size
            except OSError:
                pass
        progress_bar(i, total, prefix='Measuring')

    if not sizes:
        print("Nothing here to measure.")
        time.sleep(5)
        return

    for name, size in sorted(sizes.items(), key=lambda x: x[1], reverse=True):
        if size < 2**20:
            print(f"{name}: {size // 2**10} KB")
        else:
            print(f"{name}: {size // 2**20} MB")
    time.sleep(5)



def empty_folders(target_dir=None):
    # Finds empty subfolders and offers to delete them all
    if target_dir is None:
        target_dir = input("What folder would you like to scan for empty subfolders? (Leave blank for current): ").strip()
        if not target_dir:
            target_dir = os.getcwd()

    target_path = pathlib.Path(target_dir).expanduser().resolve()

    if not target_path.is_dir():
        print(f"Error: '{target_path}' is not a valid directory.")
        time.sleep(5)
        return

    empties = []
    for root, dirs, files in os.walk(target_path, topdown=False):
        if not dirs and not files and pathlib.Path(root) != target_path:
            empties.append(root)

    if not empties:
        print("No empty folders found.")
        time.sleep(5)
        return

    print("Empty folders found:")
    for folder in empties:
        print(f"  {folder}")

    choice = input("Delete all of these ? (y/n): ").strip().lower()
    if choice == 'y':
        total = len(empties)
        for i, folder in enumerate(empties, 1):
            try:
                os.rmdir(folder)
                print()
                print(f"Removed {folder}")
            except OSError as e:
                print()
                print(f"Could not remove {folder}: {e}")
            progress_bar(i, total, prefix='Deleting')
    time.sleep(5)



def ext_count(target_dir=None):
    # Counts how many files of each extension live in a folder tree
    if target_dir is None:
        target_dir = input("What folder would you like to scan? (Leave blank for current): ").strip()
        if not target_dir:
            target_dir = os.getcwd()

    target_path = pathlib.Path(target_dir).expanduser().resolve()

    if not target_path.is_dir():
        print(f"Error: '{target_path}' is not a valid directory.")
        time.sleep(5)
        return

    all_files = []
    for root, dirs, files in os.walk(target_path):
        for file in files:
            all_files.append(file)

    total = len(all_files)
    if total == 0:
        print("No files found.")
        time.sleep(5)
        return

    counts = {}
    for i, file in enumerate(all_files, 1):
        ext = pathlib.Path(file).suffix.lower()
        if not ext:
            ext = '(no extension)'
        counts[ext] = counts.get(ext, 0) + 1
        progress_bar(i, total, prefix='Counting')

    for ext, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{ext}: {count}")
    time.sleep(5)



def old_files(target_dir=None):
    # Finds files that haven't been touched in a while, good for cleanup
    if target_dir is None:
        target_dir = input("What folder would you like to scan? (Leave blank for current): ").strip()
        if not target_dir:
            target_dir = os.getcwd()

    target_path = pathlib.Path(target_dir).expanduser().resolve()

    if not target_path.is_dir():
        print(f"Error: '{target_path}' is not a valid directory.")
        time.sleep(5)
        return

    days_input = input("Show files untouched for how many days (blank for 30): ").strip()
    try:
        days = int(days_input) if days_input else 30
    except ValueError:
        print("Enter a number.")
        time.sleep(5)
        return

    cutoff = time.time() - (days * 86400)
    all_files = []
    for root, dirs, files in os.walk(target_path):
        for file in files:
            all_files.append(os.path.join(root, file))

    total = len(all_files)
    if total == 0:
        print("No files found.")
        time.sleep(5)
        return

    found = False
    for i, file_path in enumerate(all_files, 1):
        try:
            mtime = os.path.getmtime(file_path)
            if mtime < cutoff:
                last_mod = datetime.datetime.fromtimestamp(mtime)
                print()
                print(f"{file_path} - last modified {last_mod}")
                found = True
        except OSError:
            pass
        progress_bar(i, total, prefix='Scanning')

    if not found:
        print(f"No files older than {days} days found.")
    time.sleep(5)



def grep(target_dir=None):
    # Searches inside files for a keyword, not just filenames like 'search' does
    if target_dir is None:
        target_dir = input("What folder would you like to search? (Leave blank for current): ").strip()
        if not target_dir:
            target_dir = os.getcwd()

    target_path = pathlib.Path(target_dir).expanduser().resolve()

    if not target_path.is_dir():
        print(f"Error: '{target_path}' is not a valid directory.")
        time.sleep(5)
        return

    keyword = input("What text are you searching for ? ")

    all_files = []
    for root, dirs, files in os.walk(target_path):
        for file in files:
            all_files.append(os.path.join(root, file))

    total = len(all_files)
    if total == 0:
        print("No files found.")
        time.sleep(5)
        return

    found = False
    for i, file_path in enumerate(all_files, 1):
        try:
            with open(file_path, 'r', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    if keyword.lower() in line.lower():
                        print()
                        print(f"{file_path}:{line_num}: {line.strip()}")
                        found = True
        except OSError:
            pass
        progress_bar(i, total, prefix='Searching')

    if not found:
        print(f"No matches found for '{keyword}'.")
    time.sleep(5)



def todo():
    # Quick and dirty todo list, saved to todo.txt in whatever folder you ran this from
    todo_file = 'todo.txt'
    try:
        with open(todo_file) as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    if not lines:
        print("Nothing on the list yet.")
    else:
        print("Current tasks:")
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line.strip()}")

    action = input("add / done / remove / nothing ? ").strip().lower()
    if action == 'add':
        task = input("What's the task ? ")
        lines.append(f"[ ] {task}\n")
        with open(todo_file, 'w') as f:
            f.writelines(lines)
        print("Added.")
    elif action == 'done':
        num = input("Which number ? ")
        try:
            index = int(num) - 1
            if index < 0:
                raise IndexError
            lines[index] = lines[index].replace('[ ]', '[x]', 1)
            with open(todo_file, 'w') as f:
                f.writelines(lines)
            print("Marked done.")
        except (IndexError, ValueError):
            print("Could not find that task.")
    elif action == 'remove':
        num = input("Which number ? ")
        try:
            index = int(num) - 1
            if index < 0:
                raise IndexError
            removed = lines.pop(index)
            with open(todo_file, 'w') as f:
                f.writelines(lines)
            print(f"Removed: {removed.strip()}")
        except (IndexError, ValueError):
            print("Could not find that task.")
    time.sleep(5)



def _clear_screen():
    # same clear logic used in Py-Shell, kept standalone here since this isn't nested in PyShell
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def ascii_gallery():
    # Animated big-ascii-art slideshow. 20 frames, cycles through with a progress bar at the bottom.
    arts = [
("Cat", r"""
                  /\_____/\
                 /  o   o  \
                |     ^     |
                 \   ___   /
                  \_______/
                 /|       |\
                / |       | \
               *  |       |  *
                  |_______|
                 /         \
                /  /     \  \
               *  *       *  *
""".rstrip('\n')),

("Skull", r"""
              _.-''''''-._
            .'  _      _  '.
           /   (_)    (_)   \
          |   ______________ |
          |  /              \|
          | |    X      X    |
          |  \   \  ^^  /   /|
           \  '.___\/\/___.'/
            '.    '----'   .'
              '-._______.-'
               /||||||||\
              /_||_||_||_\
             (___)(___)(___)
""".rstrip('\n')),

("Bomb", r"""
                       \   /
                        \ /
                     ____V____
                    /  spark  \
                   |   ~~~~~   |
                    \_________/
                   .-'  ___  '-.
                  /   .'   '.   \
                 |   /  ###  \   |
                 |  | ####### |  |
                 |  | ####### |  |
                 |   \  ###  /   |
                  \   '.___.'   /
                   '-._______.-'
                      |     |
                      '-----'
""".rstrip('\n')),

("Ghost", r"""
                  .-''''''-.
                 /  o    o  \
                |            |
                |     __     |
                |    /  \    |
                 \   \__/   /
                  \________/
                  |  |  |  |
                  |  |  |  |
                 /\  /\  /\  /\
                /  \/  \/  \/  \
""".rstrip('\n')),

("Heart", r"""
              ***       ***
            *******   *******
          ***************** ***
         ***********************
         ***********************
          *********************
            *****************
              *************
                *********
                  *****
                    *
""".rstrip('\n')),

("Rocket", r"""
                     /\
                    /  \
                   / /\ \
                  /_/  \_\
                 |  ____  |
                 | |    | |
                 | | () | |
                 | |____| |
                /| /----\ |\
               / |/      \| \
              /__/        \__\
                 |  ____  |
                /   /  \   \
               /===/    \===\
              FIRE         FIRE
""".rstrip('\n')),

("Robot", r"""
                ___________
               |  o     o  |
               |     ^     |
               |  \_____/  |
                -----------
               /|    |    |\
              | |    |    | |
              | |____|____| |
               \____| |____/
                    | |
                  __| |__
                 |_______|
                 |   |   |
                 |___|   |___|
                (___)     (___)
""".rstrip('\n')),

("Alien", r"""
                    ___
                 .-'   '-.
                /  O   O  \
               |     ^     |
                \  \___/  /
                 '-.___.-'
               /     |     \
              /      |      \
             |   .---+---.   |
             |  /    |    \  |
              \/     |     \/
                     |
                  /  |  \
                 /   |   \
""".rstrip('\n')),

("Fire", r"""
                     (   )
                  (   )  )
                (    (   )  )
              )    (   )    (
                (  )    )  )
              (    )  (   )
            )    (  WW   )  (
          (   )  (  WWWW  ) (
        (  ) ( WW  WWWWWW  WW )
       ( )( WWW  WWWWWWWWWW  WWW )
        WWWWWWWWWWWWWWWWWWWWWWWWW
""".rstrip('\n')),

("Lightning", r"""
                      /\
                     /  \
                    /    \
                   /      \
                  /        \
                 /__________\
                      \
                       \
                        \
                  _______\______
                 /              \
                /                \
               /__________________\
""".rstrip('\n')),

("Snake", r"""
        ___
       /   \
      | O   |____________
       \___/             \____
                               \____
                                    \____
                              ____/
                         ____/
                    ____/
              _____/
        _____/
       /
      (  hisssss...
       \_____________
""".rstrip('\n')),

("Spider", r"""
            \           /
             \         /
              \_______/
           .--' O   O '--.
          /     \___/     \
         |     ___|___     |
          \   /   |   \   /
           \ /    |    \ /
        ----+-----+-----+----
           / \    |    / \
          /   \   |   /   \
         /     \  |  /     \
""".rstrip('\n')),

("Dragon", r"""
                                    ^\___/^
                                  ./  o o  \.
                  ___,,,,,,,,___ |    ~    | ___,,,,,,___
            ,;;;'''           '''-,_,-'''           '''';;;,
          ,;'                                                ';,
         /                       /\  /\                        \
        |                       /  \/  \                        |
         \                     /        \                      /
          ';,                /            \                 ,;'
            ''';;,,,,,,,,;;'''              '';;,,,,,,,,;;'''
""".rstrip('\n')),

("Crown", r"""
            *           *           *
           /|\         /|\         /|\
          / | \       / | \       / | \
         /  |  \     /  |  \     /  |  \
        /   |   \   /   |   \   /   |   \
       /____|____\ /____|____\ /____|____\
      |                                    |
      |   ______________________________   |
      |  |______________________________|  |
      |____________________________________|
""".rstrip('\n')),

("Diamond", r"""
                  /\
                 /  \
                /    \
               /------\
              /        \
             /          \
            /            \
            \            /
             \          /
              \        /
               \      /
                \    /
                 \  /
                  \/
""".rstrip('\n')),

("Mushroom", r"""
                  .--------.
               .-'  o  o    '-.
              /    .------.    \
             |    /        \    |
             |   |  o    o  |   |
              \   \        /   /
               '-. '------' .-'
                  '--------'
                     |  |
                     |  |
                    _|  |_
                   |______|
""".rstrip('\n')),

("UFO", r"""
                  .-=========-.
              .-'  o   o   o  '-.
            .'   o    UFO    o   '.
           /=======================\
          |  o   *   o   *   o   *  |
           \=======================/
                  |   |   |
                  V   V   V
                 beam beam beam
""".rstrip('\n')),

("Sword", r"""
                      /\
                     /  \
                    /    \
                   |      |
                   |      |
                   |      |
                   |      |
                   |      |
              ======      ======
                   |      |
                   |  ||  |
                   | |  | |
                   |_|  |_|
""".rstrip('\n')),

("Trophy", r"""
                ___________
               '._  ===  _.'
                  '.   .'
              ______|   |______
             /  ,-.  \ /  ,-.  \
            |  ( + )  |  ( + )  |
             \  '-'  / \  '-'  /
              '.___.'   '.___.'
                  |       |
                  |       |
                 _|_______|_
                |___________|
""".rstrip('\n')),

("GG", r"""
            ######    ######
           ##         ##
           ##   ####  ##   ####
           ##    ##   ##    ##
           ##  #####  ##  #####
            ######    ######

              good game!
        thanks for watching :)
""".rstrip('\n')),
    ]

    total = len(arts)
    for i, (name, art) in enumerate(arts, 1):
        _clear_screen()
        print(f"=== ASCII GALLERY ({i}/{total}): {name} ===")
        print(art)
        print()
        progress_bar(i, total, prefix=f'{name:<10}')
        time.sleep(1.2)
    print("\nThat's the whole gallery. GG!\n")
    time.sleep(5)
def adcalc():
    expression = input("Enter expression (spaces between everything, e.g., 2 + 3 * 4): ")
    digits = expression.split()

    try:
        # Start with the first number
        result = float(digits[0])

        # Loop through the operators and next numbers
        for i in range(1, len(digits), 2):
            op = digits[i]
            next_num = float(digits[i+1])

            if op == '+':
                result += next_num
            elif op == '-':
                result -= next_num
            elif op == '*':
                result *= next_num
            elif op == '/':
                result /= next_num
            else: raise ValueError

        print(f"Result: {result}")
    except Exception:
        print("Error: Make sure to use spaces (e.g., 5 + 10 * 2)")
        time.sleep(5)
    time.sleep(5)
#main loop
switch = True
while switch == True:
    Greeter()
    command = input().strip().lower()
    #BUG FIX: Greeter() tells the user "Quit = Q" but this used to only match lowercase 'q'
    if command == 'q':
        switch = False
    elif command == 'c':
        path = input('What directory/path ?')
        if  path == 'home' or path == '~':
            path = os.path.expanduser('~')
        try:
            os.chdir(path)
            print(f"Changed directory to {path}")
            time.sleep(5)
        except FileNotFoundError:
            print(f"Directory {path} not found.")
            time.sleep(5)
    
    elif command == '1':
        PyShell()
    elif command == '2':
        organizer()
    elif command == '3':
        dupe_finder()
    elif command == '4':
        bulk_rename()
    elif command == '5':
        backup()
    elif command == '6':
        cipher()
    elif command == '7':
        dir_sizes()
    elif command == '8':
        empty_folders()
    elif command == '9':
        ext_count()
    elif command == '10':
        old_files()
    elif command == '11':
        grep()
    elif command == '12':
        todo()
    elif command == '13':
        ascii_gallery()
    elif command == '14':
        adcalc()
    else:
        print('invaild input fuck you read to docs')
        time.sleep(5)
