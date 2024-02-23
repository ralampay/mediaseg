import sys
import argparse
import os
import datetime
import os.path
import json
from datetime import datetime

from .modules.parse import Parse
from .modes.transcribe_to_html import TranscribeToHtml

modes = [
    "transcribe-to-html"
]
 
def main():
    current_date = datetime.now()
    date_format = "%Y-%m-%d"
    current_date_str = current_date.strftime(date_format)

    parser = argparse.ArgumentParser(description="MediaSeg: Python media segmentor")

    parser.add_argument("--file", help="AVI file to segment", required=True)
    parser.add_argument("--mode", help="Mode for processing", default="transcribe-to-html", choices=modes)
    parser.add_argument("--out-dir", help="Output directory", default="tmp")
    parser.add_argument("--date", help="Date of the video file (Format: yyyy-mm-dd)", default=current_date_str)
    parser.add_argument("--start-time", help="Start time of the video", default="10:00:00")
    parser.add_argument("--end-time", help="Start time of the video", default="22:00:00")

    args = parser.parse_args()

    file        = args.file
    mode        = args.mode
    out_dir     = args.out_dir
    date_str    = args.date
    start_time  = args.start_time
    end_time    = args.end_time

    if mode == "transcribe-to-html":
        cmd = TranscribeToHtml(
            file=file, 
            out_dir=out_dir, 
            date_str=date_str, 
            start_time=start_time, 
            end_time=end_time
        )

        cmd.execute()

if __name__ == "__main__":
    main()
