#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2

import re
from bs4 import BeautifulSoup,element
import os


class Novel:
    def __init__(self, server_url, author, book_name, update_time, description, latest_chapter_name, latest_chapter_url):
        self.server_url = server_url
        self.author = author
        self.book_name = book_name
        self.update_time = update_time
        self.description = description


def test1():
    server = "http://www.biquge.com/0_168/"

    content = urllib2.urlopen(server)
    html = content.read()
    s = BeautifulSoup(html, "lxml")

    novel_info = ('category', 'author', 'book_name', 'read_url', 'status', 'update_time', 'latest_chapter_name', 'latest_chapter_url')
    head_tag = s.head
    for i in novel_info:
        novel_property = re.compile("og:novel:%s" % i)
        property_tag = head_tag.find(property=novel_property)
        if property_tag is not None:
            print property_tag.get('content')

    body_tag = s.find_all('dd')
    for i in body_tag:
        if i.find('a') is not None:
            print i.find('a').string + i.find('a').get('href')


def test2():
    server = "http://www.xxbiquge.com/5_5422/1068322.html"

    article_content = urllib2.urlopen(server)
    article_html = article_content.read()

    article_s = BeautifulSoup(article_html, "lxml")
    print article_s.find(id="content")


def test3():
    # url
    server1 = "http://www.officeplus.cn/List.shtml?cat=PPT&tag=&order=1"

    html1 = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """

    home_path = os.environ['HOME']
    html_path = os.path.join(home_path, "tmp")
    s = BeautifulSoup(open(html_path + "/office.html"), "lxml")

if __name__ == "__main__":

    test1()




