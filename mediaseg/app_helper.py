import os
from termcolor import colored

def is_avi_file(file):
    _, extension = os.path.splitext(file)
    print(f"extension: {extension}")

    return extension.lower() == ".avi"

def print_error(message):
    print(colored(f"Error: {message}", "red"))
