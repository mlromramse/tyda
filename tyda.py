#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys

from bs4 import BeautifulSoup
import requests as requests


class Tyda():

    def tyd(self, word):
        html = requests.get('http://tyda.se/search/{}?lang%5B0%5D=en&lang%5B1%5D=sv'.format(word)).content
        # print html
        soup = BeautifulSoup(html, 'html.parser')
        anchors = soup.select('ul.list-translations li.item > a')
        for item in anchors:
            print item.get_text()
        # print anchors


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: tyda search_word'
        exit(0)
    Tyda().tyd(sys.argv[1])
