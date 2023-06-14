import unittest
from unittest.mock import MagicMock

from text_converter import UnicodeFileToHtmlTextConverter

class TestUnicodeFileToHtmlTextConverter(unittest.TestCase):
    
    def test_convert_to_html(self):
        repository = MagicMock()
        repository.open.return_value = ["Hello world"]
        html_converter = MagicMock()
        html_converter.escape.return_value = "Hello world<br />"
        converter = UnicodeFileToHtmlTextConverter(repository=repository, html_converter_client=html_converter)

        expected = "Hello world<br /><br />"
        actual = converter.convert_to_html(full_filename_with_path="full_filename_with_path")

        assert repository.open.called_once()
        assert html_converter.escape.called_once()
        self.assertEqual(actual, expected)
