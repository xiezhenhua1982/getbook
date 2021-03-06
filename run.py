import sys
import time
from getbook.gen import BookGen


def run(url):
    begin = time.time()
    g = BookGen(None)
    d = g.parse(url, force=True)
    end = time.time()

    print(d['title'])
    print('------------')
    print('%(lang)s %(publisher)s %(author)s %(pubdate)s' % d)
    print('------------')
    print(d['attachments'])
    print('------------')
    print(d['content'])
    print('------------')
    print(end - begin)


run(sys.argv[1])
