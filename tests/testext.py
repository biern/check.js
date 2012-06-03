# -*- coding: utf-8 -*-
import unittest

from testbase import ParseTest

from checkjs.analyzers.ext import ExtAnalyzer


class TestGlobals(ParseTest):
    filename = 'test_inputs/test_ext.js'

    def setUp(self):
        self.analyzer = ExtAnalyzer()

    def test_globals(self):
        self.analyzer.analyze(self.tree)
        self.analyzer.print_result()


if __name__ == '__main__':
    unittest.main()
