# -*- coding: utf-8 -*-
import codecs
import sys

import antlr3

from JavaScriptLexer import JavaScriptLexer, \
     CALL, CALL_IDENTIFIER, CALL_ARGUMENTS, FUNCTION, \
     FUNCTION_EXPR, FUNCTION_PARAMETERS, VARIABLE_DECL
from JavaScriptParser import JavaScriptParser, tokenNames


from checkjs.parser import Parser, Node


class AntlrParser(Parser):
    tokens_map = {
        CALL: ('Call', ['identifier', 'arguments'])
    }

    def parse_file(self, path):
        file_stream = antlr3.ANTLRFileStream(path, 'utf-8')
        lexer = JavaScriptLexer(file_stream)
        parser = JavaScriptParser(antlr3.CommonTokenStream(lexer))

        program = parser.program()

        return self._convert_tree(program.tree)

    def print_tree_info(self, tree, indent=0):
        print('{}{}: {}'.format(' ' * 2 * indent,
                                tree.name,
                                tree.text))
        for c in tree:
            self.print_tree_info(c, indent + 1)

    def _convert_tree(self, tree):
        children = []
        for c in tree.getChildren():
            children.append(self._convert_tree(c))

        try:
            data = self.tokens_map[tree.type]
        except KeyError:
            data = (tokenNames[tree.type], [])

        return Node(data[0], codecs.encode(tree.text or '', 'utf-8'),
                    children, data[1])

if __name__ == '__main__':
    p = AntlrParser()
    tree = p.parse_file(sys.argv[1])
    p.print_tree_info(tree)
