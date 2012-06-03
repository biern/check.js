# -*- coding: utf-8 -*-


class Parser(object):

    def __init__(self):
        pass

    def parse_file(self, filepath):
        pass


class Node(object):
    def __init__(self, type, text, children, attrs, parent=None):
        self.type = type
        self.text = text
        self.children = children
        self.parent = parent
        self.attrs = attrs

    def print_tree(self, indent=0):
        indent_str = ' ' * 2 * indent
        print('{}{}: {}'.format(
                indent_str, self.type, self.text))

        for c in self:
            c.print_tree(indent + 1)

    def __unicode__(self):
        return "{0}: {1}".format(self.name, self.text)

    def __getitem__(self, item):
        return self.children[item]

    def __iter__(self):
        for c in self.children:
            yield c

    def __len__(self):
        return len(self.children)

    def __getattr__(self, attr):
        try:
            return self.children[self.attrs.index(attr)]
        except ValueError:
            raise AttributeError(attr)
