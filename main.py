import time
import colorama
import os
from pystyle import System as PYSystem
from rich.console import Console
from rich import print as rprint
from rich.text import Text
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import HTML
import sys
import shutil
import requests
import zipfile
import io
import pyttsx3
import datetime
import calendar

PYSystem.Clear()  # Clear the terminal screen
PYSystem.Title("Pynux - Fan-Made Linux Terminal")

colorama.init(autoreset=True)

# for rich console output
console = Console()

start_time = time.time()
history = []
aliases = {}


# colours of prompt_toolkit
YELLOW = '\033[93m'
RESET = '\033[39m'


commands = ["test", "credits", "devlog", "ls", "mkdir", "cd", "rm", "rn", "updates", "reports", 
            "pwd", "clear", "mv", "cp", "cat", "ip", "ping", "whoami", "wget", "apt", "discord", "reload",
            "alias", "say", "calendar", "touch", "echo", "uptime", "history"]
session = PromptSession()

# get desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
os.chdir(desktop_path)

def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def print_banner():
    print(colorama.Fore.LIGHTGREEN_EX + "========================================================================")
    print(colorama.Fore.CYAN + """

 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄        ▄  ▄         ▄  ▄       ▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░▌      ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌
▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌░▌     ▐░▌▐░▌       ▐░▌ ▐░▌   ▐░▌ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌       ▐░▌  ▐░▌ ▐░▌  
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌   ▐░▐░▌   
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌    ▐░▌    
▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌   ▐░▌░▌   
▐░▌               ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌  ▐░▌ ▐░▌  
▐░▌               ▐░▌     ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌ ▐░▌   ▐░▌ 
▐░▌               ▐░▌     ▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌
 ▀                 ▀       ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀ 
                                                               
Fan-Made Linux Terminal running On Python 3.11.4
Only runnable for Windows OS from 10 - 11
Version: 1.0.5v
""")
    print(colorama.Fore.LIGHTGREEN_EX + "===========================================================================")
    print(colorama.Fore.YELLOW + f"Current Time: {get_current_time()}")

def print_test():
    print(colorama.Fore.LIGHTBLUE_EX + "This is a test function. It can be used for debugging or testing purposes.")

def credits_to_elon():
    print(colorama.Fore.LIGHTMAGENTA_EX + "Made by ElonChunk. Credits to some python coders who helped me on some errors with this and the fuctionality.")

def get_dev_log():
    try:
        response = requests.get("https://raw.githubusercontent.com/ElonChunk/Pynux/main/dev_log.txt")
        if response.status_code == 200:
            print(colorama.Fore.LIGHTCYAN_EX + response.text)
        else:
            print(colorama.Fore.RED + "Failed to retrieve the development log.")
    except requests.RequestException as e:
        print(colorama.Fore.RED + f"An error occurred: {e}")

def get_reports():
    try:
        response = requests.get("https://raw.githubusercontent.com/ElonChunk/Pynux/main/reports.txt")
        if response.status_code == 200:
            print(colorama.Fore.LIGHTCYAN_EX + response.text)
        else:
            print(colorama.Fore.RED + "Failed to retrieve the reports.")
    except requests.RequestException as e:
        print(colorama.Fore.RED + f"An error occurred: {e}")

def get_updates():
    try:
        response = requests.get("https://raw.githubusercontent.com/ElonChunk/Pynux/main/updates.txt")
        if response.status_code == 200:
            print(colorama.Fore.LIGHTCYAN_EX + response.text)
        else:
            print(colorama.Fore.RED + "Failed to retrieve the updates.")
    except requests.RequestException as e:
        print(colorama.Fore.RED + f"An error occurred: {e}")

# starter linux commands
def ls_command():
    items = os.listdir()
    for item in items:
        if os.path.isdir(item):
            console.print(f"[bold yellow]{item}/[/]")  # Folders in blue with slash
        elif item.endswith(".py"):
            console.print(f"[green]{item}[/]")  # Python files in green
        elif item.endswith(".txt"):
            console.print(f"[white]{item}[/]")  # Text files in magenta
        else:
            console.print(f"{item}")  # Normal files default color

def mkdir_command(folder_name):
    try:
        os.mkdir(folder_name)
        console.print(f"[green]Folder '{folder_name}' created successfully.[/]")
    except FileExistsError:
        console.print(f"[red]Error: Folder '{folder_name}' already exists.[/]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def rn_command(old_name, new_name):
    if not os.path.exists(old_name):
        console.print(f"[red]Error: '{old_name}' does not exist.[/]")
        return
    try:
        os.rename(old_name, new_name)
        console.print(f"[green]Renamed '{old_name}' to '{new_name}'.[/]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def cd_command(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        console.print(f"[red]Error: The folder '{path}' does not exist.[/]")
    except NotADirectoryError:
        console.print(f"[red]Error: '{path}' is not a directory.[/]")
    except PermissionError:
        console.print(f"[red]Error: You don’t have permission to access '{path}'.[/]")
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/]")

def rm_command(name):
    if not os.path.exists(name):
        console.print(f"[red]Error: '{name}' does not exist.[/]")
        return
    try:
        if os.path.isfile(name):
            os.remove(name)
            console.print(f"[yellow]File '{name}' deleted.[/]")
        elif os.path.isdir(name):
            shutil.rmtree(name)
            console.print(f"[yellow]Folder '{name}' deleted.[/]")
    except Exception as e:
        console.print(f"[red]Error deleting '{name}': {e}[/]")

def pwd_command():
    console.print(f"[green]{os.getcwd()}[/]")

def clear_command():
    PYSystem.Clear()

def mv_command(src, dest):
    try:
        shutil.move(src, dest)
        console.print(f"[green]Moved '{src}' to '{dest}'.[/]")
    except Exception as e:
        console.print(f"[red]Error moving: {e}[/]")

def cp_command(src, dest):
    try:
        if os.path.isfile(src):
            shutil.copy2(src, dest)
            console.print(f"[green]Copied '{src}' to '{dest}'.[/]")
        elif os.path.isdir(src):
            shutil.copytree(src, dest)
            console.print(f"[green]Copied directory '{src}' to '{dest}'.[/]")
        else:
            console.print(f"[red]Error: '{src}' not found.[/]")
    except Exception as e:
        console.print(f"[red]Error copying: {e}[/]")

def cat_command(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            console.print(f"[white]{content}[/]")
    except FileNotFoundError:
        console.print(f"[red]File '{filename}' not found.[/]")
    except Exception as e:
        console.print(f"[red]Error reading file: {e}[/]")

def ip_command():
    import socket
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        console.print(f"[cyan]Local IP: {ip_address}[/]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def ping_command(host):
    import subprocess
    try:
        subprocess.run(["ping", "-n", "4", host])
    except Exception as e:
        console.print(f"[red]Error: {e}[/]")

def whoami_command():
    console.print(f"[cyan]{os.getlogin()}[/]")

def wget_command(url):
    try:
        filename = url.split("/")[-1] or "downloaded_file"
        console.print(f"[cyan]Downloading from:[/] {url}")
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            console.print(f"[green]Downloaded '{filename}' successfully.[/]")
        else:
            console.print(f"[red]Failed to download. Status code: {response.status_code}[/]")
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Error: {e}[/]")

# TEST PACKAGES!!

# === COMMAND LOADER FOR packages/ ===

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # path to main2.py
COMMANDS_DIR = os.path.join(BASE_DIR, "packages")      # your actual command directory

def init_directories():
    os.makedirs(COMMANDS_DIR, exist_ok=True)

def load_commands():
    commands = {}
    if not os.path.exists(COMMANDS_DIR):
        print(f"[ERROR] {COMMANDS_DIR}")
        return commands

    for fname in os.listdir(COMMANDS_DIR):
        if fname.endswith(".py"):
            cmd_name = fname[:-3]
            with open(os.path.join(COMMANDS_DIR, fname), "r", encoding="utf-8") as f:
                commands[cmd_name] = f.read()
    return commands

def execute_command(commands_packages, name, args):
    if name not in commands_packages:
        return  # maybe it's a built-in, don't error

    scope = {
        "__name__": "__main__",
        "__args__": args,
        "commands": commands_packages
    }

    try:
        exec(commands_packages[name], scope)
        if "run" in scope and callable(scope["run"]):
            scope["run"](args, commands_packages)
    except Exception as e:
        print(f"[ERROR] While executing '{name}': {e}")

# END OF TEST PACKAGES!
# apt test!

def apt_command(args):
    packages_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "packages")
    changed = False  # <- Track changes

    if not args:
        console.print("[yellow]Usage:[/]")
        console.print(" - apt install <name>")
        console.print(" - apt uninstall <name>")
        console.print(" - apt list")
        return False

    sub = args[0]

    if sub == "install":
        if len(args) < 2:
            console.print("[red]Usage: apt install <name> or apt install *[/]")
            return False

        names = []

        # Handle wildcard: install all packages from GitHub repo
        if args[1] == "*":
            console.print("[cyan]Fetching package list from GitHub...[/]")

            try:
                response = requests.get("https://api.github.com/repos/ElonChunk/PynuxPackages/contents")
                if response.status_code == 200:
                    data = response.json()
                    names = [item['name'][:-3] for item in data if item['name'].endswith('.py')]
                else:
                    console.print(f"[red]Failed to fetch file list (status {response.status_code})[/]")
                    return False
            except Exception as e:
                console.print(f"[red]Error fetching package list: {e}[/]")
                return False

        else:
            # Install a single package
            names = [args[1]]

        installed = []
        for name in names:
            url = f"https://raw.githubusercontent.com/ElonChunk/PynuxPackages/main/{name}.py"
            filepath = os.path.join(packages_dir, f"{name}.py")

            try:
                response = requests.get(url)
                if response.status_code == 200:
                    with open(filepath, "w", encoding="utf-8", newline="") as f:
                        cleaned_text = response.text.replace("\r\n", "\n").replace("\r", "\n")
                        f.write(cleaned_text)
                    installed.append(name)
                else:
                    console.print(f"[red]Package '{name}' not found. Status: {response.status_code}[/]")
            except Exception as e:
                console.print(f"[red]Error installing '{name}': {e}[/]")

        if installed:
            console.print(f"[green]Successfully installed: {', '.join(installed)}[/]")
            return True
            
    elif sub == "uninstall":
        if len(args) < 2:
            console.print("[red]Usage: apt uninstall <name>[/]")
            return False
        name = args[1]
        filepath = os.path.join(packages_dir, f"{name}.py")
        if os.path.exists(filepath):
            os.remove(filepath)
            console.print(f"[yellow]Uninstalled '{name}'.[/]")
            changed = True
        else:
            console.print(f"[red]'{name}' is not installed.[/]")

    elif sub == "list":
        files = [f[:-3] for f in os.listdir(packages_dir) if f.endswith(".py")]
        console.print("[cyan]Installed packages:[/]")
        for pkg in sorted(files):
            console.print(" -", pkg)

    else:
        console.print(f"[red]Unknown subcommand: {sub}[/]")

    return changed  # <-- Tell main() that something changed

#end of apt test
# new commands
def touch_command(filename):
    try:
        with open(filename, 'a'):
            os.utime(filename, None)
        print(f"[+] Created empty file: {filename}")
    except Exception as e:
        print(f"[!] Error creating file: {e}")

def echo_command(args):
    if ">" in args:
        parts = ' '.join(args).split(">")
        message = parts[0].strip()
        filename = parts[1].strip()
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(message + '\n')
            print(f"[+] Written to {filename}")
        except Exception as e:
            print(f"[!] Error writing to file: {e}")
    else:
        print(' '.join(args))

def uptime_command():
    seconds = int(time.time() - start_time)
    mins, sec = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    print(f"[+] Uptime: {hrs}h {mins}m {sec}s")

def history_command():
    for i, cmd in enumerate(history, 1):
        print(f"{i}: {cmd}")

def alias_command(args):
    if "=" in ' '.join(args):
        name, real = ' '.join(args).split("=", 1)
        aliases[name.strip()] = real.strip()
        print(f"[+] Alias created: {name.strip()} = '{real.strip()}'")
    else:
        print("[!] Usage: alias ll='ls -l'")

def say_command(args):
    if not args:
        print("[!] Usage: say <text>")
        return
    text = ' '.join(args)
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"[!] Text-to-speech error: {e}")

def calendar_command():
    now = datetime.datetime.now()
    print(calendar.month(now.year, now.month))
# end of new commands

def main():
    commands_packages = load_commands()
    command_completer = WordCompleter(commands + list(commands_packages.keys()), ignore_case=True)
    init_directories()
    print_banner()
    get_reports()
    while True:
        # Get the current directory for the prompt
        current_dir = os.getcwd()
        prompt_text = HTML(f'<ansicyan>Pynux~</ansicyan> <ansibrightblue>{current_dir}</ansibrightblue> &gt;&gt; ')
        prompt = session.prompt(prompt_text, completer=command_completer)

        if not prompt:
            continue

        parts = prompt.split()
        cmd_name = parts[0]
        cmd_args = parts[1:]
        execute_command(commands_packages, cmd_name, cmd_args)

        if cmd_name == "apt":
            changed = apt_command(cmd_args)
            if changed:
                commands_packages = load_commands()  # Reload installed packages
                command_completer = WordCompleter(commands + list(commands_packages.keys()), ignore_case=True)

        elif prompt == "test":
            print_test()

        elif prompt == "discord":
            print(colorama.Fore.BLUE + "Official Pynux Discord Server: https://discord.gg/ucJBsh86e3")

        elif prompt == "":
            continue

        elif prompt == " ":
            continue
        
        elif cmd_name == "alias":
            alias_command(cmd_args)

        elif cmd_name == "say":
            say_command(cmd_args)
        
        elif cmd_name == "calendar":
            calendar_command()
        
        elif cmd_name == "touch":
            if len(cmd_args) == 1:
                touch_command(cmd_args[0])
            else:
                print("[!] Usage: touch <filename>")
        
        elif cmd_name == "echo":
            echo_command(cmd_args)
        
        elif cmd_name == "uptime":
            uptime_command()
        
        elif cmd_name == "history":
            history_command()
        
        elif prompt == "credits":
            credits_to_elon()
        
        elif prompt == "updates":
            get_updates()
        
        elif prompt == "reports":
            get_reports()

        elif prompt.startswith("mkdir "):
            folder_name = prompt[6:].strip()
            if folder_name:
                mkdir_command(folder_name)
            else:
                console.print("[red]Usage: mkdir <foldername>[/]")

        elif prompt == "pwd":
            pwd_command()

        elif prompt == "clear":
            clear_command()

        elif prompt.startswith("mv "):
            parts = prompt.split()
            if len(parts) == 3:
                mv_command(parts[1], parts[2])
            else:
                console.print("[red]Usage: mv <source> <destination>[/]")

        elif prompt.startswith("cp "):
            parts = prompt.split()
            if len(parts) == 3:
                cp_command(parts[1], parts[2])
            else:
                console.print("[red]Usage: cp <source> <destination>[/]")

        elif prompt.startswith("cat "):
            filename = prompt[4:].strip()
            if filename:
                cat_command(filename)
            else:
                console.print("[red]Usage: cat <filename>[/]")

        elif prompt == "ip":
            ip_command()

        elif prompt.startswith("ping "):
            host = prompt[5:].strip()
            if host:
                ping_command(host)
            else:
                console.print("[red]Usage: ping <host>[/]")

        elif prompt == "whoami":
            whoami_command()

        elif prompt.startswith("rn "):
            parts = prompt.split()
            if len(parts) == 3:
                rn_command(parts[1], parts[2])
            else:
                console.print("[red]Usage: rn <oldname> <newname>[/]")

        elif cmd_name == "reload":

            clear_command()
            print(" pynux reloaded")
            return main()  # Call main() again to restart

        elif prompt.startswith("cd "):
            path = prompt[3:].strip()
            if path:
                cd_command(path)
            else:
                console.print("[red]Usage: cd <foldername>[/]")

        elif prompt.startswith("rm "):
            name = prompt[3:].strip()
            if name:
                rm_command(name)
            else:
                console.print("[red]Usage: rm <file_or_folder>[/]")

        elif prompt.startswith("wget "):
            url = prompt[5:].strip()
            if url:
                wget_command(url)
            else:
                console.print("[red]Usage: wget <url>[/]")

        elif prompt == "devlog":
            get_dev_log()

        elif prompt == "ls":
            ls_command()

        elif cmd_name not in commands and cmd_name not in commands_packages:
            console.print("[red]Unknown command. Type 'test' to run a test function.[/]")


if __name__ == "__main__":
    main()
    # Additional functionality can be added here later

