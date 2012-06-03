# -*- coding: utf-8 -*-


class Parser(object):

    def __init__(self):
        pass

    def parse_file(self, filepath):
        pass


class Node(object):
    def __init__(self, name, text, children, attrs):
        self.name = name
        self.text = text
        self.children = children
        self.attrs = attrs

    def __getitem__(self, item):
        return self.children[item]

    def __iter__(self):
        for c in self.children:
            yield c

    def __getattr__(self, attr):
        try:
            return self.children[self.attrs.index(attr)]
        except ValueError:
            raise AttributeError(attr)
