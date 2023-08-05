# pylint: disable=W0622
"""cubicweb-elasticsearch application packaging information"""

modname = 'elasticsearch'
distname = 'cubicweb-elasticsearch'

numversion = (0, 6, 2)
version = '.'.join(str(num) for num in numversion)

license = 'LGPL'
author = 'LOGILAB S.A. (Paris, FRANCE)'
author_email = 'contact@logilab.fr'
description = 'Simple ElasticSearch indexing integration for CubicWeb'
web = 'http://www.cubicweb.org/project/%s' % distname

__depends__ = {'cubicweb': '>= 3.24.0', 'six': '>= 1.4.0',
               'cwtags': None,
               'elasticsearch': '>=2.0.0,<3.0.0',
               'elasticsearch-dsl': '<5.0.0',
               'beautifulsoup4': None,
               }

__recommends__ = {}

classifiers = [
    'Environment :: Web Environment',
    'Framework :: CubicWeb',
    'Programming Language :: Python',
    'Programming Language :: JavaScript',
]
