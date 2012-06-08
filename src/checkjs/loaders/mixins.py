# -*- coding: utf-8 -*-

import logging
import urllib2


log = logging.getLogger('remote-loader-mixin')


class RemoteLoaderMixin(object):
    root_url = 'http://127.0.0.1'

    def _parse(self, path, parser):
        if path.startswith('remote://'):
            path = path.replace('remote://', self.root_url, 1)

        if path.startswith('http://'):
            try:
                stream = urllib2.urlopen(path)
                return parser.parse_stream(stream.read())
            except urllib2.HTTPError:
                self.errors.append('Unable to fetch file "{0}"'.\
                                   format(path))
                log.info('HTTPError during fetching "{0}"'.format(path))
                return None

        return super(RemoteLoaderMixin, self)._parse(path, parser)
