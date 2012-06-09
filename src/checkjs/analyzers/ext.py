# -*- coding: utf-8 -*-

from collections import defaultdict

from checkjs.analyzers.base import Analyzer


class ExtAnalyzer(Analyzer):
    name = 'ext'

    def analyze(self, tree):
        self.clean()
        self.tree_recur(tree)
        return self._make_result()

    def _make_result(self):
        return {
            'requires': self.depends[1],  # tmp alias
            'uses': sum(self.depends.values(), []),
            'depends': self.depends[1],
            'defines': self.defines,
        }

    def clean(self):
        super(ExtAnalyzer, self).clean()
        self.defines = []
        self.depends = defaultdict(list)

    def _add_depends(self, name, base=None):
        level = 0
        if base and type(base) != int:
            level = self.count_call_depth(base)

        if not type(name) == str:
            name = name.text

        self.depends[level].append(name)

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

        if idents[1] in ('create', 'define', 'application'):
            getattr(self, '_handle_ext_{0}'.format(idents[1]))(node)

    def _handle_ext_create(self, node):
        arg = node.arguments[0][0]
        if arg.type != 'StringLiteral':
            return

        self._add_depends(arg, node.parent)

    def _handle_ext_define(self, node):
        arg = node.arguments[0][0]
        if arg.type != 'StringLiteral':
            self.error("Bad Ext.define call", node)
            return

        self._add_defines(arg)

        app_name = arg.text.split('.')[0]

        self._handle_ext_object_properties(node.arguments[1][0], app_name)

    def _handle_ext_application(self, node):
        self._handle_ext_object_properties(node.arguments[0][0])

        name = None
        controllers = []
        for prop in node.arguments[0][0]:
            if prop.name.text == 'name':
                name = prop.value[0].text
            if prop.name.text == 'controllers':
                controllers = self.extract_list_items(prop.value)
                # controllers = [value[0].text for value in prop.value[0]]

        self.depends[0].extend(
            '{0}.controller.{1}'.format(name, c) for c in controllers)

    def _handle_ext_object_properties(self, node, app_name=None):
        if node.type != 'Object':
            self.error("Bad Ext call", node)
            return

        for prop in node:
            if prop.name.text == 'extend':
                self._add_depends(prop.value[0], node)

            if prop.name.text == 'requires':
                for name in self.extract_list_items(prop.value):
                    self._add_depends(name, node)

            if app_name and prop.name.text in ('views', 'stores', 'models'):
                values = self.extract_list_items(prop.value)
                self.depends[1].extend(
                    ('{0}.{1}.{2}'.format(app_name, prop.name.text[:-1], v) \
                         for v in values))
