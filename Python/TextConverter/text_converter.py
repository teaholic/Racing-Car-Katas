
# This is for Python 3
import html as html_converter

# for Python 2 uncomment this line
#import cgi as html_converter
from Python.TextConverter.repository import FileRepository


class UnicodeFileToHtmlTextConverter:

    def __init__(self, repository: FileRepository, html_converter_client):
        self.repository = repository
        self.html_converter_client = html_converter_client

    def convert_to_html(self, full_filename_with_path):
        f = self.repository.open(full_filename_with_path)
        html = ""
        for line in f:
            line = line.rstrip()
            html += self.html_converter_client.escape(line, quote=True)
            html += "<br />"
        print(html)
        return html