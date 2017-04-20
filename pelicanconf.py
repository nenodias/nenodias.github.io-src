#!/usr/bin/env python
"""PelicanConf."""
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Horácio Dias Baptista Neto'
SITENAME = 'Nenodias'
SITESUBTITLE = 'Doing the best code or not so...'
SITEURL = 'http://nenodias.github.io'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('TryPix', 'http://trypix.wordpress.com/'),
         ('You Tube', 'http://youtube.com/'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/nenodias'),
          ('Linkedin', 'https://www.linkedin.com/in/nenodias92'),)

DEFAULT_PAGINATION = 10
THEME = 'theme/'
MD_EXTENSIONS = [
    'fenced_code',
    'codehilite(css_class=highlight, linenums=True)',
    'extra'
]
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
