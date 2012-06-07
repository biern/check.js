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

    def up(self, arg):
        """
        Go up `arg` times or up to parent.type == `arg`.
        Returns None on failure.
        """

        res = self
        if type(arg) == int:
            for i in range(arg):
                try:
                    res = res.parent
                except AttributeError:
                    return None

            return res

        if type(arg) == str:
            while res and not (res and res.type == arg):
                res = res.parent

            return res

    def count(self, *names):
        """
        Counts occurences parents of type in names
        """
        res = self.parent
        count = 0
        while res:
            if res.type in names:
                count += 1

            res = res.parent

        return count

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
