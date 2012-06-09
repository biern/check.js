# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

from checkjs.parsers.antlr.parser import AntlrParser
from checkjs.analyzers.ext import ExtAnalyzer
from checkjs.analyzers.globals import GlobalsAnalyzer


if __name__ == '__main__':
    p = AntlrParser()
    tree = p.parse_file(sys.argv[1])

    tree.print_tree()

    print('Checking "{0}"\n'.format(sys.argv[1]))

    a = ExtAnalyzer()
    a.analyze(tree)
    a.print_result()

    print('---')

    a = GlobalsAnalyzer()
    a.analyze(tree)
    a.print_result()
