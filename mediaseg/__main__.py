import sys
import argparse
import os
import datetime
import os.path
import json

from .modules.parse import Parse
from .modes.transcribe_to_html import TranscribeToHtml

modes = [
    "transcribe-to-html"
]
 
def main():
    parser = argparse.ArgumentParser(description="MediaSeg: Python media segmentor")

    parser.add_argument("--file", help="AVI file to segment", required=True)
    parser.add_argument("--mode", help="Mode for processing", default="transcribe-to-html", choices=modes)
    parser.add_argument("--out-dir", help="Output directory", default="tmp")

    args = parser.parse_args()

    file    = args.file
    mode    = args.mode
    out_dir = args.out_dir

    if mode == "transcribe-to-html":
        cmd = TranscribeToHtml(file=file, out_dir=out_dir)
        cmd.execute()

if __name__ == "__main__":
    main()
