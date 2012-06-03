# -*- coding: utf-8 -*-
import unittest

from testbase import ParseTest

from checkjs.analyzers.checkglobals import CheckGlobals


class TestGlobals(ParseTest):
    filename = 'test_inputs/test_globals.js'

    def setUp(self):
        self.analyzer = CheckGlobals()

    def test_globals(self):
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
