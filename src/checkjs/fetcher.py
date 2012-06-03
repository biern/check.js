# -*- coding: utf-8 -*-


class FileFetcher(object):

    def __init__(self, parser):
        self._cache = {}
        self.parser = parser

    def fetch_file(self, path):
        path = self.convert_path(path)
        try:
            return self._cache[path]
        except KeyError:
            return self._cache.setdefault(path, self.parser.parse(path))

    def convert_path(self, path):
        return path
