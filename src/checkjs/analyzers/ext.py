# -*- coding: utf-8 -*-

from checkjs.analyzers.base import Analyzer


class ExtAnalyzer(Analyzer):

    def analyze(self, tree):
        self.clean()
        self.defines = []
        self.depends = []
        self.tree_recur(tree)

    def print_result(self):
        print("   Defines ext: {0}".format(self.defines))
        print("Depends on ext: {0}".format(self.depends))

    def _add_depends(self, node):
        self.depends.append(node.text)

    def _add_defines(self, node):
        self.defines.append(node.text)

    def analyze_call(self, node):
        """
        TODO: docs
        """

        if node.identifier[0].type == 'FunctionExpression':
            return

        idents = self.extract_identifier(node.identifier)
        if idents[0] != 'Ext' or len(idents) < 2:
            return

        if idents[1] in ('create', 'define'):
            getattr(self, '_handle_ext_{0}'.format(idents[1]))(node)

    def _handle_ext_create(self, node):
        arg = node.arguments[0][0]
        if arg.type != 'StringLiteral':
            return

        self._add_depends(arg)

    def _handle_ext_define(self, node):
        arg = node.arguments[0][0]
        if arg.type != 'StringLiteral':
            self.error("Bad Ext.define call", node)
            return

        self._add_defines(arg)

        self._handle_ext_object_properties(node.arguments[1][0])

    def _handle_ext_object_properties(self, node):
        if node.type != 'Object':
            self.error("Bad Ext call", node)
            return

        for prop in node:
            if prop.name.text == 'extend':
                self._add_depends(prop.value[0])
