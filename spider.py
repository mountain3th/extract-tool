#coding=utf-8

import urllib
from bs4 import *

base_url = 'http://bbs.tianya.cn/post-develop-1868959-%d.shtml'

def get_text(url):
    html = urllib.urlopen(url).read().decode('utf-8')
    return html

if __name__ == '__main__':
    for i in range(1, 583):
        print i
        content = get_text(base_url % i)
        soup = BeautifulSoup(content)
        for div in soup.find_all('div', js_username='%E9%AA%91%E7%99%BD%E9%A9%AC%E7%9A%84%E5%86%9C%E6%B0%91'):
            string = div.select('div.bbs-content')[0].get_text()
            if u'【' in string and u'】' in string:
                with open('scrap.txt', 'a') as scrap:
                    scrap.write(string.encode('utf-8'))
