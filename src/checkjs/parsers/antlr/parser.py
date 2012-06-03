# -*- coding: utf-8 -*-
import codecs
import sys

import antlr3

from JavaScriptLexer import JavaScriptLexer, \
     CALL, CALL_IDENTIFIER, CALL_ARGUMENTS, FUNCTION, \
     FUNCTION_EXPR, FUNCTION_PARAMETERS, VARIABLE_DECL, \
     MEMBER, MEMBER_EXPR, ASSIGNMENT, OPERATOR_ARGS, \
     VARIABLE_DECL, OBJECT, PROPERTY
from JavaScriptParser import JavaScriptParser, tokenNames


from checkjs.parser import Parser, Node


class AntlrParser(Parser):
    tokens_map = {
        CALL: ('Call', ['identifier', 'arguments']),
        MEMBER: ('Member', ['identifier']),
        FUNCTION: ('FunctionDeclaration', ['identifier', 'params', 'body']),
        FUNCTION_EXPR: ('FunctionExpression', ['params', 'body']),  # TODO
        ASSIGNMENT: ('Assignment', ['operator', 'args']),
        OPERATOR_ARGS: ('OperatorArguments', ['left', 'right']),
        OBJECT: ('Object', []),
        PROPERTY: ('Property', ['name', 'value']),
        MEMBER_EXPR: ('MemberExpr', ['base']),
        VARIABLE_DECL: ('VariableDecl', ['identifier', 'value']),
    }

    def parse_file(self, path):
        file_stream = antlr3.ANTLRFileStream(path, 'utf-8')
        lexer = JavaScriptLexer(file_stream)
        parser = JavaScriptParser(antlr3.CommonTokenStream(lexer))

        program = parser.program()

        return self._convert_tree(program.tree)

    def print_tree_info(self, tree, indent=0):
        print('{}{}: {}'.format(' ' * 2 * indent,
                                tree.type,
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
            data = (tokenNames[tree.type], [], True)

        if len(data) > 2:
            text = (tree.text or '') if data[2] else ''
            if data[0] == 'StringLiteral':
                text = text[1:-1]
        else:
            text = ''

        node = Node(data[0], codecs.encode(text, 'utf-8'),
                    children, data[1])
        for c in node:
            c.parent = node

        return node

if __name__ == '__main__':
    p = AntlrParser()
    tree = p.parse_file(sys.argv[1])
    p.print_tree_info(tree)
