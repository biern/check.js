# -*- coding: utf-8 -*-

import logging
import pickle
import sys

sys.path.append('../src')

from checkjs.analyzers.globals import GlobalsAnalyzer
from checkjs.loaders.ext import ExtLoader
from checkjs.loaders.mixins import RemoteLoaderMixin
from checkjs.merger import Merger
from checkjs.parsers.antlr.parser import AntlrParser
from checkjs import utils


logging.basicConfig(level=logging.INFO)


class VideoIDLoader(RemoteLoaderMixin, ExtLoader):
    root_url = 'http://127.0.0.1:8000/extadmin_js/app'


if __name__ == '__main__':
    # Parser
    parser = AntlrParser()

    # Loader
    videoid_loader = {
        'prefix': 'VideoID',
        'root': 'http://127.0.0.1:8000/extadmin_js/app',
    }
    ext_loader = {
        'prefix': 'Ext',
        'skip': True,
    }

    loader = VideoIDLoader([ext_loader, videoid_loader])

    # Arguments
    if len(sys.argv) == 1:
        files = [videoid_loader['root'] + '.js']
    else:
        files = [sys.argv[1]]

    # Loading files
    # Use cached file data if possible
    cache = '{0}.cache'.format(files[0].rsplit('/', 1)[1])
    try:
        files_data = pickle.load(open(cache))
        print("Using Cache")
    except IOError:
        files_data = loader.load(files, parser, [GlobalsAnalyzer()])

        if loader.errors:
            print("Loader Errors:")
            for e in loader.errors:
                print(e)

            print('')

        pickle.dump(files_data, open(cache, 'w'))

    # Creating dependency list
    deps, missing = utils.to_dep_dict(files_data, ['ext', 'globals'], 'Ext.')
    print('Undefined Dependencies:')
    for m in missing:
        print(m)
    print('')

    # Merging
    m = Merger()
    print('Merge order:')
    for i, files in enumerate(m.make_dep_list(deps)):
        print('{0}: {1}'.format(i, ', '.join(files)))

    print('')

    print('Merging Files')
    m.merge(deps, open('merged.js', 'w'), loader)
