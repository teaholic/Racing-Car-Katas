"""This is a second, slightly harder problem on the same theme as the first."""

# This is for Python 3
import html as html_converter

# for Python 2 uncomment this line
#import cgi as html_converter
from typing import List


class FileRepository:

    """Read the file and note the positions of the page breaks so we can access them quickly"""
    def _get_breaks(self, filename) -> List[int]:
        breaks: List[int] = [0]
        with open(filename, "r", encoding="UTF-8") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.rstrip()
                if "PAGE_BREAK" in line:
                    page_break_position = f.tell()
                    breaks.append(f.tell())
            breaks.append(f.tell())
            return breaks

    def get_lines(self, filename, page) -> List[str]:
        lines = []
        breaks = self._get_breaks(filename)
        page_start = breaks[page]
        page_end = breaks[page + 1]
        with open(filename, "r", encoding="UTF-8") as f:
            f.seek(page_start)
            while f.tell() != page_end:
                line = f.readline()
                line = line.rstrip()
                if "PAGE_BREAK" in line:
                    continue
                lines.append(line)
        return lines


class HtmlPagesConverter:
    def __init__(self, repository: FileRepository):
        self.repository = repository

    def get_html_page(self, filename: str, page):
        """Return html page with the given number (zero indexed)"""
        html = ""
        lines = self.repository.get_lines(filename=filename, page=page)
        for line in lines:
            html += html_converter.escape(line, quote=True)
            html += "<br />"
        return html

