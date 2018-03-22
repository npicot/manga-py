from manga_dl.provider import Provider
from .helpers.std import Std


class PsychoPlayCo(Provider, Std):

    def get_archive_name(self) -> str:
        return 'vol_{:0>3}'.format(self.get_chapter_index())

    def get_chapter_index(self) -> str:
        ch = self.chapter
        idx = self.re.search('/read/[^/]+/([^/]+)', ch)
        return idx.group(1)

    def get_main_content(self):
        return self._get_content('{}/series/{}')

    def get_manga_name(self) -> str:
        return self._get_name('/(?:series|read)/([^/]+)')

    def get_chapters(self):
        _chapter = 'a.media-link'
        items = self._elements(_chapter)
        selector = '.pagination li:not([class]) a'
        pages = self.document_fromstring(self.content, selector)
        n = self.http().normalize_uri
        for i in pages:  # TODO! Warning!
            items += self._elements(_chapter, self.http_get(n(i.get('href'))))
        return items

    def get_files(self):  # TODO! Warning!
        parser = self.html_fromstring(self.chapter)
        return self._images_helper(parser, '.img-responsive', 'data-src')

    def get_cover(self) -> str:
        item = self._elements('.profile-cover-img')
        if item:
            return self.parse_background(item[0])


main = PsychoPlayCo