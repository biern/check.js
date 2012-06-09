# -*- coding: utf-8 -*-

import logging
import os

from checkjs.analyzers.ext import ExtAnalyzer
from checkjs.loaders.base import BaseLoader

log = logging.getLogger('ext-loader')


class ExtLoader(BaseLoader):
    """
    Tries to load all ext modules that this module depends on
    """

    def __init__(self, extloaders):
        super(ExtLoader, self).__init__()
        self.extloaders = extloaders

    def get_analyzers(self):
        return [ExtAnalyzer()]

    def analyze(self, path, analyzers, tree):
        data = super(ExtLoader, self).analyze(path, analyzers, tree)
        self.to_parse.update(
            (path for path in self._paths_from_names(
                    data['ext']['uses'], self.extloaders))
            )
        return data

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
