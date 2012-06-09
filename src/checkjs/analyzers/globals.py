# -*- coding: utf-8 -*-

from collections import defaultdict

from checkjs.analyzers.base import Analyzer


class GlobalsAnalyzer(Analyzer):
    name = 'globals'
    skip_names = set(['this', 'arguments', 'undefined', 'true', 'false'])

    def analyze(self, tree):
        self.clean()
        self.tree_recur(tree, {'defined': []})
        # self.defines = list(set(self.defines))
        # self.depends = list(set(self.depends) - \
        #                     self.skip_names - \
        #                     set(self.defines))
        return self._make_result()

    def _make_result(self):
        skip_names = self.skip_names.union(set(self.defines))
        return {
            'depends': list(set(self.depends[0]) - skip_names),
            'uses': list(set(sum(self.depends.values(), [])) - skip_names),
            'defines': list(set(self.defines)),
        }

    def clean(self):
        super(GlobalsAnalyzer, self).clean()
        self.defines = []
        self.depends = defaultdict(list)

    def _add_depends(self, name, base=None):
        level = 0
        if base and type(base) != int:
            level = self.count_func_depth(base)

        if not type(name) == str:
            name = name.text

        self.depends[level].append(name)

    def tree_recur(self, node, kwargs):
        """
        If 'meth' returns a value it is treated as a new context for children
        calls
        """

        # TODO: Czy to nie zadziała czasem razem z extra?
        meth = getattr(self, 'analyze_{0}'.format(node.type.lower()), None)
        if meth:
            res = meth(node, kwargs)
            if res:
                kwargs = res

        for c in node:
            self.tree_recur(c, kwargs)

    def analyze_call(self, node, kwargs):
        defined = kwargs['defined']
        if node.identifier[0].type == 'FunctionExpression':
            return

        idents = self.extract_identifier(node.identifier)
        if idents[0] not in defined:
            self._add_depends(idents[0], node)

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

    def analyze_memberexpr(self, node, kwargs):
        defined = kwargs['defined']

        assignment = node.up('Assignment')
        if assignment and assignment.args.left == node:
            return

        # vardecl = node.up('VariableDecl')
        # if vardecl and vardecl.identifier == node:
        #     return

        if node.type == 'MemberExpr' and node.base.type == 'Identifier' and \
                node.base.text not in defined:
            self._add_depends(node.base.text, node)

    def check_global_memberexpr(self, node, defined):
        if node.type == 'MemberExpr' and node.base.type == 'Identifier' and \
                node.base.text not in defined:
            self._add_depends(node.base.text, node)
            return True

        return False
