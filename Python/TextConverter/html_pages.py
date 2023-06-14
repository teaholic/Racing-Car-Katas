"""This is a second, slightly harder problem on the same theme as the first."""

# This is for Python 3
import html as html_converter

# for Python 2 uncomment this line
#import cgi as html_converter
from typing import List

from repository import FileRepository


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

