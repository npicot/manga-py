# Manga-Downloader

## Supported resources (32)

- [x] http://desu.me
- [x] http://heymanga.me
- [x] http://manga-online.biz
- [x] http://mangabb.co
- [x] http://mangabox.me
- [x] http://mangaclub.ru
- [x] http://mangaeden.com
- [x] http://mangafox.me
- [x] http://mangafreak.net
- [x] http://mangago.me
- [x] http://mangahere.co
- [x] http://mangahome.com
- [x] http://mangahub.ru
- [x] http://mangainn.net
- [x] http://mangakakalot.com
- [x] http://manganel.com
- [x] http://mangaonlinehere.com
- [x] http://mangapanda.com
- [x] http://mangapark.me
- [x] http://mangareader.net
- [x] http://mangarussia.com
- [x] http://mangatan.net
- [x] http://mangatown.com
- [x] http://mintmanga.com
- [x] http://ninemanga.com
- [x] http://readmanga.me
- [x] http://selfmanga.ru
- [x] http://shakai.ru
- [x] http://unixmanga.nl
- [x] http://read.yagami.me
- [x] http://yaoichan.me
- [x] http://zingbox.me
---

## How to use

### Installation

```bash
git clone --recursive  https://github.com/yuru-yuri/Manga-Downloader.git
cd Manga-Downloader
# install requirements
pip3 -r requirements.txt
cd helpers/cloudflare_scrape
python setup.py install
```

### Downloading
__:warning:Notice! The name of the manga is always added to the path!__

__To change this behavior, add the key --no-name__

```bash
# download to ./manga directory
./manga.py -i -p -u http://manga-url-here/manga-name
# or download to /manga/destination/path/ directory
./manga.py -i -p -u http://manga-url-here/manga-name -d /manga/destination/path/
# or interactive mode
./manga.py -i -p
# skip 3 volumes
./manga.py --skip-volumes 3 -u http://manga-url-here/manga-name
# reverse volumes downloading (24 -> 1)
./manga.py --reverse-downloading -u http://manga-url-here/manga-name
```

### Help

```bash
./manga.py -h
# or
./manga.py --help
```
