#!/usr/bin/env python


import subprocess
import argparse
import re
from colorama import Fore, Style


def print_with_color(text: str, color: str) -> None:
    print(f'{color}{text}{Style.RESET_ALL}')


def run_command(mode: str, id: int) -> None:
    subprocess.run(['xinput', mode, id])


def search_keyboard_identifier() -> list[int]:
    output: str = subprocess.run(
        ['xinput', 'list'], capture_output=True, text=True).stdout
    id: list[int] = re.findall(
        r'AT Translated Set 2 keyboard\s+id=(\d+)+', output)
    return id


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Enable or disable the keyboard')
    parser.add_argument(
        "-e", "--enable", help="Enable the keyboard", action="store_true")
    parser.add_argument(
        "-d", "--disable", help="Disable the keyboard", action="store_true")

    args = parser.parse_args()
    id: list[int] = search_keyboard_identifier()

    if args.enable:
        run_command('enable', id[0])
        print_with_color('Keyboard enabled', Fore.GREEN)
    elif args.disable:
        run_command('disable', id[0])
        print_with_color('Keyboard disabled', Fore.RED)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
