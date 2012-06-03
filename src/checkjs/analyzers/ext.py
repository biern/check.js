# -*- coding: utf-8 -*-

from checkjs.analyzers.base import Analyzer


class ExtAnalyzer(Analyzer):

    def analyze(self, tree):
        self.defines = []
        self.depends = []
        self.tree_recur(tree)

    def analyze_call(self, node):
        """
        TODO: docs
        """

        if node.identifier[0].type == 'FunctionExpression':
            return

        idents = self.extract_identifier(node.identifier)
        if idents[0] != 'Ext' or len(idents) < 2:
            return

        if idents[1] == 'create':
            self._handle_ext_create(node)

    def _handle_ext_create(self, node):
        arg = node.arguments[0][0]
        if arg.type != 'StringLiteral':
            return

        self.depends.append(
            arg.text.split('.'))
