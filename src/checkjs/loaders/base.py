# -*- coding: utf-8 -*-

from collections import defaultdict
import logging

log = logging.getLogger('base-loader')


class BaseLoader(object):

    def get_analyzers(self):
        return []

    def load(self, files, parser, analyzers=None):
        analyzers = self.get_analyzers() + (analyzers or [])
        self.errors = []
        self.not_loaded = []

        self.files_data = defaultdict(dict)
        self.to_parse = to_parse = set(files)
        parsed = set()

        while to_parse:
            f = to_parse.pop()
            if f in parsed:
                continue

            parsed.add(f)

            tree = self.parse(f, parser)

            if tree is None or parser.errors:
                self._parser_error(f, parser)
                parser.clean()
                continue

            self.analyze(f, analyzers, tree)

        return self.files_data

    def analyze(self, f, analyzers, tree):
        res = {}
        for a in analyzers:
            res[a.name] = a.analyze(tree)

        self.files_data[f] = res
        return res

    def parse(self, path, parser):
        try:
            return parser.parse_file(path)
        except NotImplementedError:
            return parser.parse_stream(self.get_file(path))

    def get_file(self, path):
        log.info('Loading {0}'.format(path))
        return open(path)

    def _parser_error(self, f, parser):
        err = 'Unable to parse file "{0}"'.format(f)
        log.info(err)
        self.errors.append(err)
        self.not_loaded.append(f)
