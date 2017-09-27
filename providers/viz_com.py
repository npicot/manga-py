#!/usr/bin/python3
# -*- coding: utf-8 -*-

from lxml.html import document_fromstring
import re
from helpers.exceptions import UrlParseError

domainUri = 'https://www.viz.com'


def get_main_content(url, get=None, post=None):
    name = get_manga_name(url)
    return get('{}/shonenjump/chapters/{}'.format(domainUri, name))


def get_volumes(content=None, url=None, get=None, post=None):
    items = document_fromstring(content).cssselect('.o_products .chapter-text > a')
    return [i.get('href') for i in items]


def get_archive_name(volume, index: int = None):
    return 'vol_{:0>3}'.format(index)


def get_images(main_content=None, volume=None, get=None, post=None):
    volume_id = re.search('/chapter/[^/]+/(\d+)', volume)
    params = [
        'device%5Fid=3',
        # 'page={}',
        'manga%5Fid={}'.format(volume_id.groups()[0]),
        'loadermax=1',
    ]

    uri = '{}/manga/get_manga_url?'.format(domainUri)
    uri += '&'.join(params)

    images = []

    n = 0
    while n < 199:

        content = get('{}&page={}'.format(uri, n)).encode()

        parser = document_fromstring(content).cssselect('ImageLoader')

        if not len(parser):
            break
        print(n)

        for i in parser:
            img_url = i.get('url')
            if img_url.find('blankpage.jpg') > 0:
                break
            images.append(img_url)

        n += 2

    return images

    """
    curl 'https://www.viz.com/manga/get_manga_url?device%5Fid=3&page=16&manga%5Fid=6098&loadermax=1' -H 'x-requested-with: ShockwaveFlash/27.0.0.130' -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.55' -H 'authority: www.viz.com' -H 'referer: https://www.viz.com/shonenjump/chapter/claymore-chapter-7/6098?read=1' --compressed
    """


def get_manga_name(url, get=None):
    name = re.search('\\.com/shonenjump/chapters/([^/]+)', url)
    if not name:
        return UrlParseError()
    return name.groups()[0]
    """
    :param url: str
    :param get: request.get
    :return: str
    """
    pass
