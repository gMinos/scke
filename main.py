#!/usr/bin/env python


import subprocess
import argparse
import re
from colorama import Fore, Style


def print_with_color(text: str, color: str = Fore.Green) -> None:
    print(f'{color}{text}{Style.RESET_ALL}')


def run_command(mode: str, id: int) -> None:
    subprocess.run(['xinput', mode, id])


def search_keyboard_identifier():
    ouput: str = subprocess.getoutput(
        'xinput list', capture_ouput=True, text=True).stdout
