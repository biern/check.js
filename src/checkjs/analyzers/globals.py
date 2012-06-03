# -*- coding: utf-8 -*-

from checkjs.analyzers.base import Analyzer


class GlobalsAnalyzer(Analyzer):

    def analyze(self, tree):
        self.defines = []
        self.depends = []
        self.tree_recur(tree, {'defined': []})
        self.depends = list(set(self.depends) - set(['this']))
        self.defines = list(set(self.defines))

    def tree_recur(self, node, kwargs):
        """
        If 'meth' returns a value it is treated as a new context for children
        calls
        """

        # TODO: Czy to nie zadziała czasem razem z extra? (defined.append(dupa))
        meth = getattr(self, 'analyze_{0}'.format(node.type.lower()), None)
        if meth:
            res = meth(node, kwargs)
            if res:
                kwargs = res

        for c in node:
            self.tree_recur(c, kwargs)

    def print_result(self):
        print("Defines globals: [{0}]".format(', '.join(self.defines)))
        print("Depends on globals: [{0}]".format(', '.join(self.depends)))

    def analyze_call(self, node, kwargs):
        defined = kwargs['defined']
        if node.identifier[0].type == 'FunctionExpression':
            return

        idents = self.extract_identifier(node.identifier)
        if idents[0] not in defined:
            self.depends.append(idents[0])

    def analyze_functiondeclaration(self, node, kwargs):
        defined = kwargs['defined']
        if node.parent.parent is None:
            self.defines.append(node.identifier.text)

        return {'defined': [param.text for param in node.params] + \
                    defined}

    def analyze_functionexpression(self, node, kwargs):
        defined = kwargs['defined']
        return {'defined': [param.text for param in node.params] + \
                    defined}

    def analyze_assignment(self, node, kwargs):
        defined = kwargs['defined']
        self.check_global_memberexpr(node.args.right, defined)
        idents = self.extract_identifier(node.args.left)
        if len(idents) == 1 and node.operator.text == '=':
            if idents[0] not in defined:
                self.defines.append(idents[0])
        else:
            self.check_global_memberexpr(node.args.left, defined)

    def analyze_variabledecl(self, node, kwargs):
        """
        Modify parent's context instead of creating new one
        """

        defined = kwargs['defined']
        if len(node) > 1:
            self.check_global_memberexpr(node.value, defined)

        kwargs['defined'] = [node.identifier.text] + defined

    def check_global_memberexpr(self, node, defined):
        if node.type == 'MemberExpr' and node.base.type == 'Identifier' and \
                node.base.text not in defined:
            self.depends.append(node.base.text)
            return True

        return False
