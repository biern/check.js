# -*- coding: utf-8 -*-

import logging
import os
import sys

sys.path.append('../src')

from checkjs.loaders.ext import ExtLoader
from checkjs.loaders.mixins import RemoteLoaderMixin
from checkjs.parsers.antlr.parser import AntlrParser


logging.basicConfig(level=logging.INFO)


class VideoIDLoader(RemoteLoaderMixin, ExtLoader):
    root_url = 'http://127.0.0.1:8000/extadmin_js/app'


if __name__ == '__main__':
    parser = AntlrParser()
    loader = VideoIDLoader()

    app = '.js'
    videoid_loader = {
        'prefix': 'VideoID',
        'root': 'http://127.0.0.1:8000/extadmin_js/app',
    }
    ext_loader = {
        'prefix': 'Ext',
        'skip': True,
    }

    if len(sys.argv) == 1:
        files = ['remote://.js']
    else:
        files = [sys.argv[1]]

    loader.load(parser, files, [ext_loader, videoid_loader])
