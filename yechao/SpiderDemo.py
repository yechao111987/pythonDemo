# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

page = 1
url = 'http://soccer.hupu.com/'
str1 = 21321172
url2 = "http://bbs.hupu.com/" + str(str1) + ".html"
# 21321172
while str1 <= 21321172:
    try:
        request = urllib2.Request(url2)
        response = urllib2.urlopen(url2)
        print '------'
        print response.read()
        content = response.read().decode('utf-8')
        pattern = re.compile('<div class="subhead">.*<span>(.*?)<a  href.*')
        items = re.findall(pattern, content)
        print '---'
        for item in items:
            print items[0]
        print '222'
        str1 = str1 + 1
    except urllib2.URLError, e:
        str1 = str1 + 1
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
