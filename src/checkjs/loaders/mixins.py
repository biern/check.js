# -*- coding: utf-8 -*-

import logging
import urllib2


log = logging.getLogger('remote-loader-mixin')


class RemoteLoaderMixin(object):
    root_url = 'http://127.0.0.1'

    def get_file(self, path):
        if path.startswith('http://'):
            try:
                stream = urllib2.urlopen(path)
                return stream.read()
            except urllib2.HTTPError:
                self.errors.append('Unable to fetch file "{0}"'.\
                                   format(path))
                log.info('HTTPError during fetching "{0}"'.format(path))
                return None

        return super(RemoteLoaderMixin, self).get_file(path)

    def parse(self, path, parser):
        if path.startswith('remote://'):
            path = path.replace('remote://', self.root_url, 1)

        if path.startswith('http://'):
            stream = self.get_file(path)
            if stream is not None:
                return parser.parse_stream(stream)

            return None

        return super(RemoteLoaderMixin, self).parse(path, parser)
