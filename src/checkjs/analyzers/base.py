# -*- coding: utf-8 -*-


class Analyzer(object):
    """
    Base analyzer class that defines some helper methods
    """
    name = "base"

    def print_result(self):
        for k, v in self._make_result().items():
            print('{0}: {1}'.format(k, v))

    def extract_string(self, node):
        return node.text[1:-1]

    def tree_recur(self, node, **extra):
        meth = getattr(self, 'analyze_{0}'.format(node.type.lower()), None)
        if meth:
            res = meth(node, **extra)
            if res:
                extra = res

        for c in node:
            self.tree_recur(c, **extra)

    def count_call_depth(self, node):
        return node.count('FunctionExpression', 'Call')

    def count_func_depth(self, node):
        return node.count('FunctionExpression', 'FunctionDeclaration')

    def extract_identifier(self, node):
        """
        Extracts identifier and all its members (stops on other node types)
        """

        ident = [node[0].text]
        for c in node[1:]:
            if c.type != 'Member':
                break

            ident.append(c.identifier.text)

        return ident

    def extract_list_items(self, node):
        return [value[0].text for value in node[0]]

    def clean(self):
        self.errors = []

    def error(self, msg, node=None):
        self.errors.append((msg, node))
