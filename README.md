# MediaSeg

A tool to parse a given video file (`avi`) and segment it into different sections where conversations occur.

## Setup

1. Install python dependencies

```
pip install -r requirements.txt
```

2. Create temporary directory in root

```
mkdir tmp
```

## Usage

```
python -m mediaseg --file [path_to_file] --out-dir [path_to_dir] --date [yyyy-mm-dd] --start-time [xx:xx:xx] --end-time [xx:xx:xx] --mode [mode]
```

### Options

* `--file`: AVI file location
* `--out-dir`: Where to dump output of program
* `--date`: Date of video with format `yyyy-mm-dd` (default is current date)
* `--start-time`: Start time of the day with format `xx:xx:xx` (default is `10:00:00`)
* `--end-time`: Start time of the day with format `xx:xx:xx` (default is `22:00:00`)
* `--mode`: Mode for processing (default is `transcribe-to-html`)
