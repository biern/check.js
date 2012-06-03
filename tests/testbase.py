import unittest
import sys

sys.path.insert(0, '../src')

from checkjs.parsers.antlr.parser import AntlrParser


class ParseTest(unittest.TestCase):
    filename = None

    @classmethod
    def setUpClass(cls):
        p = AntlrParser()
        cls.tree = p.parse_file(cls.filename)
