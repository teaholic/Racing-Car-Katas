import unittest
from unittest.mock import MagicMock

from text_converter import UnicodeFileToHtmlTextConverter

class UnicodeFileToHtmlTextConverterTest(unittest.TestCase):
    
    def test_convert_to_html(self):
        repository = MagicMock()
        repository.open.return_value = ["Hello world"]
        html_converter = MagicMock()
        html_converter.escape.return_value = "Hello world<br />"

        expected = "Hello world<br /><br />"
        converter = UnicodeFileToHtmlTextConverter(repository=repository, html_converter_client=html_converter)
        actual = converter.convert_to_html(full_filename_with_path="full_filename_with_path")
        self.assertEqual(actual, expected)
