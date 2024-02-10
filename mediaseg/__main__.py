import sys
import argparse
import os
import datetime
import os.path
import json

from modules.parse import Parse

def main():
    parser = argparse.ArgumentParser(description="MediaSeg: Python media segmentor")

    parser.add_argument("--file", help="File to segment", required=True)

    args = parser.parse_args()

    file = args.file

    print(f"Parsing file {file}...")

    cmd = Parse(file=file)

    cmd.execute()

if __name__ == "__main__":
    main()
