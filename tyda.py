#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from bs4 import BeautifulSoup
import requests as requests


class Tyda():

    def tyd(self, word):
        html = requests.get('http://tyda.se/search/{}?lang%5B0%5D=en&lang%5B1%5D=sv'.format(word)).content
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        search_results = soup.select('div.box-searchresult > div.box')
        for search_result in search_results:
            name_elem = search_result.select_one('h1')
            if not name_elem:
                name_elem = search_result.select_one('h2')
            if not name_elem:
                continue
            print (name_elem.get_text().strip())
            synonyms = search_result.select('ul.list-synonyms li.item')
            if synonyms:
                print ('   SYNONYMS')
                for synonym in synonyms:
                    text_elem = synonym.select_one('h3 > a')
                    text = ''
                    if text_elem:
                        text = text_elem.get_text().strip()
                    desc = ''
                    desc_elem = synonym.select_one('span.syn-desc')
                    if desc_elem:
                        desc = desc_elem.get_text().strip()
                    print ('    - ', text, desc)
            language = search_result.select_one('ul.list-translations li.item-title span img')
            word_class = search_result.select_one('div.word-class')
            translations = search_result.select('ul.list-translations li.item > a')
            if translations:
                print ('   TRANSLATIONS - ' + word_class.get_text().strip())
                if language:
                    print ('      ' + language['title'])
                for translation in translations:
                    print ('       - ' + translation.get_text().strip())

    def did_you_mean(self, word):
        response = requests.get('http://tyda.se/complete?word={}&lang%5B%5D=en&lang%5B%5D=sv'.format(word))
        response_json = response.json()
        # print(response_json)
        if response_json['status'] == 1:
            print ('\nDid you mean:')
            for item in response_json['items']:
                print ('   ' + item['langid'])
                for word in item['words']:
                    print ('    - ' + word['word'])
        print('')

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1][:1] == '-':
        print ('usage: tyda search_word')
        exit(0)
    words = ' '.join(sys.argv[1:])
    tyda = Tyda()
    tyda.did_you_mean(words)
    tyda.tyd(words)
