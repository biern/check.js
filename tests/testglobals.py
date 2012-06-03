# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.insert(0, '../src')

from checkjs.parsers.antlr.parser import AntlrParser
from checkjs.analyzers.checkglobals import CheckGlobals


class TestGlobals(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        p = AntlrParser()
        cls.tree = p.parse_file('test_inputs/globals_test.js')
        cls.analyzer = CheckGlobals()

    def test_analyze(self):
        self.analyzer.analyze(self.tree)
        self.analyzer.print_result()
        self.assertEqual(
            set(['defined{0}'.format(i + 1) for i in range(5)]),
            set(self.analyzer.defines))
        self.assertEqual(
            set(['depend{0}'.format(i + 1) for i in range(5)]),
            set(self.analyzer.depends))


if __name__ == '__main__':
    unittest.main()
