# -*- coding: utf-8 -*-

import logging
import sys

sys.path.append('../src')

from checkjs.analyzers.globals import GlobalsAnalyzer
from checkjs.loaders.base import BaseLoader
from checkjs.loaders.mixins import DirectoryLoaderMixin
from checkjs.merger import Merger
from checkjs.parsers.antlr.parser import AntlrParser
from checkjs import utils


logging.basicConfig(level=logging.INFO)


class DirLoader(DirectoryLoaderMixin, BaseLoader):
    pass


if __name__ == '__main__':
    # Parser
    parser = AntlrParser()

    # Loader
    loader = DirLoader()

    # Arguments
    files_data = loader.load('test_inputs/circular/', parser,
                             [GlobalsAnalyzer()])

    if loader.errors:
        print("Loader Errors:")
        for e in loader.errors:
            print(e)

        print('')

    # Creating dependency list
    deps, missing = utils.to_dep_dict(files_data, ['globals'])
    print('Undefined Dependencies:')
    for m in sorted(missing):
        print(m)
    print('')

    # Merging
    m = Merger()

    print('Circular dependencies?')
    circular = m.check_circular(deps)
    for c in circular:
        print(c)

    if circular:
        exit()

    print('Merge order:')
    for i, files in enumerate(m.make_dep_list(deps)):
        print('{0}: {1}'.format(i, ', '.join(files)))

    print('')

    m.merge(deps, open('circular.js', 'w'))
