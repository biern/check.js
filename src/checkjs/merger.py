# -*- coding: utf-8 -*-
import logging

from collections import defaultdict

from checkjs.loaders.base import BaseLoader

log = logging.getLogger('merger')


class MergeError(Exception):
    pass


class Merger(object):

    def merge(self, deps, out, loader=None):
        if loader is None:
            loader = BaseLoader()

        circular = self.check_circular(deps)
        if circular:
            err = 'Circular dependency: {0}'.format(circular)
            log.error(err)
            raise MergeError(err)

        dep_list = self.make_dep_list(deps)
        self.merge_dep_list(dep_list, out, loader)

    def make_dep_list(self, files):
        # dependency resolver borrowed from:
        # http://code.activestate.com/recipes/576570-dependency-resolver/
        deps = dict((k, set(files[k])) for k in files)
        result = []
        while deps:
            # values not in keys (items without dep)
            t = set(i for v in deps.values() for i in v) - set(deps.keys())
            # and keys without value (items without dep)
            t.update(k for k, v in deps.items() if not v)
            # can be done right away
            if not t:
                err = 'Unable to resolve dependencies'
                log.error(err)
                raise MergeError(err)

            result.append(t)
            # and cleaned up
            deps = dict(((k, v - t) for k, v in deps.items() if v))

        return result

    def check_circular(self, files):
        circular = set()

        def recur(root, bases=[]):
            if root in bases:
                path = tuple(bases + [root])
                for c in circular:
                    if set(c) == set(path):
                        break
                else:
                    circular.add(path)

                return

            for dep in files.get(root, []):
                recur(dep, bases + [root])

        for base in files:
            for node in files[base]:
                recur(node, [base])

        return circular

    def merge_dep_list(self, dep_list, out, loader):
        for files in dep_list:
            for f in files:
                out.write('// file: {0}\n'.format(f))
                out.write(loader.get_file(f))
                out.write('\n')

    def make_dep_tree(self, root, files):
        """
        Files are defined as dict of filenames with filenames they depend on.
        ie: { file1: [file2, file3],
              file2: [file3, file5] }
        """
        in_tree = set()
        errors = defaultdict(set)

        def recur(node, cache):
            in_tree.add(node)
            for dep in files[node]:
                if dep == node:
                    continue

                # if dep in in_tree:
                #     errors['circular'].add(dep)
                #     continue

                if dep not in files:
                    errors['missing'].add(dep)
                    continue

                cache[dep] = {}
                recur(dep, cache[dep])

        tree = {root: {}}
        recur(root, tree[root])
        return tree, errors

    def flatten_dep_tree(self, tree):
        """
        Creates a flat list from a tree, in which each item may depend only on
        previoius items.
        """

        res = []

        def recur(node):
            for key, deps in node.items():
                recur(deps)
                if key not in res:
                    res.append(key)

        recur(tree)
        return res

    def print_tree(self, tree, indent=0):
        for k in sorted(tree):
            print('{0}{1}'.format(' ' * 4 * indent, k))
            self.print_tree(tree[k], indent + 1)
