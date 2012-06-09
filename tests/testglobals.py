# -*- coding: utf-8 -*-

import unittest

from testbase import ParseTest

from checkjs.analyzers.globals import GlobalsAnalyzer


class TestGlobals(ParseTest):
    filename = 'test_inputs/test_globals.js'

    def setUp(self):
        self.analyzer = GlobalsAnalyzer()

    def test_globals(self):
        result = self.analyzer.analyze(self.tree)
        self.analyzer.print_result()
        self.assertEqual(
            set(['defined{0}'.format(i + 1) for i in range(5)]),
            set(result['defines']))
        self.assertEqual(
            set(['depend{0}'.format(i + 1) for i in range(8)]),
            set(result['uses']))


if __name__ == '__main__':
    unittest.main()
