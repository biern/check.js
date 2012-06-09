# -*- coding: utf-8 -*-

from collections import defaultdict
import logging
import os

from checkjs.analyzers.ext import ExtAnalyzer

log = logging.getLogger('ext-loader')


class ExtLoader(object):

    def load(self, parser, files, extloaders=None, extra_analyzers=None):
        analyzers = tuple([ExtAnalyzer()] + (extra_analyzers or []))
        self.errors = []

        files_data = defaultdict(dict)
        to_parse = set(files)
        parsed = set()

        while to_parse:
            f = to_parse.pop()
            if f in parsed:
                continue

            parsed.add(f)
            log.info('Loading {0}'.format(f))
            tree = self.parse(f, parser)

            if tree is None:
                log.info('Unable to parse file {0}'.format(f))
                continue

            data = files_data[f]
            for analyzer in analyzers:
                data[analyzer.name] = analyzer.analyze(tree)

            if not extloaders:
                continue

            # Parse all except already parsed
            to_parse.update(
                (path for path in \
                     self._paths_from_names(
                        data['ext']['uses'], extloaders)
                 if path not in parsed))

        if self.errors:
            print("ERRORS:")
            for err in self.errors:
                print(err)

        return files_data

    def parse(self, path, parser):
        try:
            return parser.parse_file(path)
        except NotImplementedError:
            return parser.parse_stream(self.get_file(path))

    def get_file(self, path):
        return open(path)

    def _paths_from_names(self, names, extloaders):
        """
        Returns absolute filesystem paths based on names in ext dotted format
        and defined extloaders
        """

        for name in names:
            for loader in extloaders:
                if not name.startswith('{0}.'.format(loader['prefix'])):
                    continue

                if loader.get('skip'):
                    break

                yield self._path_from_name(name, loader)
                break

            else:
                self._add_name_error(name)

    def _path_from_name(self, name, loader):
        dotpath = name.replace(loader['prefix'], '', 1)[1:]
        return '{0}.js'.format(
            os.path.join(loader['root'], *dotpath.split('.')))

    def _add_name_error(self, name):
        self.errors.append('Unable to resolve name {0} to path'.format(name))
