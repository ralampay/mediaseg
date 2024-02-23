import os
import uuid

from bs4 import BeautifulSoup

from ..modules.parse import Parse
from ..app_helper import get_filename

class TranscribeToHtml:
    def __init__(self, 
        file : str = "", 
        out_dir : str = "",
        date_str : str = "",
        start_time : str = "",
        end_time : str = ""
    ):
        self.file       = file
        self.out_dir    = out_dir
        self.date_str   = date_str
        self.start_time = start_time
        self.end_time   = end_time

    def execute(self):
        self.parser = Parse(file=self.file, date_str=self.date_str, start_time=self.start_time)
        self.parser.execute()

        self.filename = get_filename(self.file)

        generated_html_content = self._generate_html()

        file_to_write = f"{self.out_dir}/{self.filename}.html"
        with open(file_to_write, "w") as file:
            file.write(generated_html_content)

        print(f"Output: {file_to_write}")

    def _generate_html(self):
        soup = BeautifulSoup(features="html.parser")

        html = soup.new_tag("html")

        head = soup.new_tag("head")
        style = soup.new_tag('style')
        style.string = "table { width: 100%; border-collapse: collapse; } th, td { border: 1px solid black; padding: 8px; }"
        head.append(style)

        title = soup.new_tag("title")
        title.string = self.filename
        head.append(title)

        body = soup.new_tag("body")

        h1 = soup.new_tag("h1")
        h1.string = self.filename

        h2 = soup.new_tag("h2")
        h2.string = self.date_str

        body.append(h1)
        body.append(h2)

        table = soup.new_tag("table")

        thead = soup.new_tag("thead")
        tbody = soup.new_tag("tbody")

        tr_head = soup.new_tag("tr")

        th_label_id = soup.new_tag("th")
        th_label_id.string = "ID"

        th_label_start = soup.new_tag("th")
        th_label_start.string = "Start"

        th_label_end = soup.new_tag("th")
        th_label_end.string = "End"

        th_label_start_timestamp = soup.new_tag("th")
        th_label_start_timestamp.string = "Start Timestamp"

        th_label_end_timestamp = soup.new_tag("th")
        th_label_end_timestamp.string = "End Timestamp"

        th_label_content = soup.new_tag("th")
        th_label_content.string = "Content"

        tr_head.append(th_label_id)
        tr_head.append(th_label_start)
        tr_head.append(th_label_end)
        tr_head.append(th_label_start_timestamp)
        tr_head.append(th_label_end_timestamp)
        tr_head.append(th_label_content)

        thead.append(tr_head)

        for item in self.parser.transcriber.content:
            tr = soup.new_tag("tr")

            td_id = soup.new_tag("td")
            td_id.string = str(item['id'])

            td_start_time = soup.new_tag("td")
            td_start_time.string = str(item['start_time'])

            td_end_time = soup.new_tag("td")
            td_end_time.string = str(item['end_time'])

            td_start_timestamp = soup.new_tag("td")
            td_start_timestamp.string = str(item['start_timestamp'])

            td_end_timestamp = soup.new_tag("td")
            td_end_timestamp.string = str(item['end_timestamp'])

            td_text = soup.new_tag("td")
            td_text.string = item['text']

            tr.append(td_id)
            tr.append(td_start_time)
            tr.append(td_end_time)
            tr.append(td_start_timestamp)
            tr.append(td_end_timestamp)
            tr.append(td_text)

            tbody.append(tr)

        table.append(thead)
        table.append(tbody)
        body.append(table)
        html.append(head)
        html.append(body)

        soup.append(html)

        return str(soup)
