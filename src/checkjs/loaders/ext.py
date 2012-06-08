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
            tree = self._parse(f, parser)

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

        # for file, analyzers in files_data.items():
        #     print('{0}:'.format(file))
        #     if not analyzers:
        #         print("    ERROR")
        #         continue

        #     for name, data in analyzers.items():
        #         print('  {0}:'.format(name))
        #         for key, value in data.items():
        #             print('    {0}: {1}'.format(key, value))

    def _parse(self, path, parser):
        return parser.parse_file(path)

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
