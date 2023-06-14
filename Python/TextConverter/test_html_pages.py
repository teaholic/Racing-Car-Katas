from unittest import TestCase
from unittest.mock import MagicMock

from html_pages import HtmlPagesConverter


class TestHtmlPagesConverter(TestCase):

    def test_convert_to_html(self):
        repository = MagicMock()
        repository.get_lines.return_value = ["Hello world", "How do you do?"]

        expected = "Hello world<br />How do you do?<br />"""
        actual = HtmlPagesConverter(repository).get_html_page('f', 1)
        self.assertEqual(actual, expected)
