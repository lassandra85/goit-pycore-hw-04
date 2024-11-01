import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def visualize_directory(path: Path, level: int = 0):

    if not path.exists() or not path.is_dir():

        print(f"{Fore.RED}Error: '{path}' is not a valid directory.")
        return

    for item in path.iterdir():

        indent = "    " * level 

        if item.is_dir():

            print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}/") 
            visualize_directory(item, level + 1) 

        else:

            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}") 

def main():
    
    if len(sys.argv) < 2:

        print("Usage: python script.py <directory_path>")
        return

    directory_path = Path(sys.argv[1])

    visualize_directory(directory_path)

if __name__ == "__main__":
    main()
