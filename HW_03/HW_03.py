import sys

from pathlib import Path

from colorama import Fore, Back, Style

path_from_terminal = sys.argv

directory_path = Path(path_from_terminal[1])


def print_dir_content(current_dir=Path('.'), shift=0, extensions_colors=None):
    if extensions_colors is None:
        extensions_colors = {'.py': Fore.MAGENTA, '.png': Fore.MAGENTA, '.jpeg': Fore.MAGENTA, '.txt': Fore.MAGENTA }

    for path in current_dir.iterdir():
        if path.is_dir():
            print(' ' * shift + f'- {path.name}')
            print_dir_content(path, shift + 2)
        else:
            styles = extensions_colors[path.suffix]
            print(' ' * shift + styles + path.name + Style.RESET_ALL)

print(print_dir_content(directory_path))