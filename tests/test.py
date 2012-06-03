# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

from checkjs.parsers.antlr.parser import AntlrParser

if __name__ == '__main__':
    p = AntlrParser()
    tree = p.parse_file(sys.argv[1])
    p.print_tree_info(tree)
