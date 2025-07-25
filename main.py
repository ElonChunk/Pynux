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

PYSystem.Clear()  # Clear the terminal screen
PYSystem.Title("Pynux - Fan-Made Linux Terminal")

colorama.init(autoreset=True)

# for rich console output
console = Console()

# colours of prompt_toolkit
YELLOW = '\033[93m'
RESET = '\033[39m'


commands = ["test", "credits", "devlog", "ls", "mkdir", "cd", "nano", "rm", "rn", "updates", "reports", 
            "pwd", "clear", "mv", "cp", "cat", "ip", "ping", "whoami"]
command_completer = WordCompleter(commands, ignore_case=True)
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
Version: 1.0.1v
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

def nano_command(filename):
    console.print(f"[cyan]Opening '{filename}' in nano editor...[/]")
    console.print("[dim]Type your text below. Type ':wq' alone on a line to save and quit.[/]")

    # If the file already exists, show its content first
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
            if content:
                console.print(f"[dim]--- Existing File Content ---[/]")
                console.print(content)
                console.print(f"[dim]--- End ---[/]")

    lines = []
    while True:
        line = input()
        if line.strip() == ":wq":
            break
        lines.append(line)

    try:
        with open(filename, 'w') as f:
            f.write("\n".join(lines))
        console.print(f"[green]Saved '{filename}' successfully.[/]")
    except Exception as e:
        console.print(f"[red]Error saving file: {e}[/]")

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

def main():
    print_banner()
    get_reports()
    while True:
        # Get the current directory for the prompt
        current_dir = os.getcwd()
        prompt_text = HTML(f'<ansicyan>Pynux~</ansicyan> <ansibrightblue>{current_dir}</ansibrightblue> &gt;&gt; ')
        prompt = session.prompt(prompt_text, completer=command_completer)

        if prompt == "test":
            print_test()

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

        elif prompt.startswith("nano "):
            filename = prompt[5:].strip()
            if filename:
                nano_command(filename)
            else:
                console.print("[red]Usage: nano <filename>[/]")

        elif prompt == "devlog":
            get_dev_log()

        elif prompt == "ls":
            ls_command()

        else:
            print(colorama.Fore.RED + "Unknown command. Type 'test' to run a test function.")

if __name__ == "__main__":
    main()
    # Additional functionality can be added here later
