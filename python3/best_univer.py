# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import bs4
import sys
import imp

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    #print soup
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])
            #print "tds[0].string",tds[0].string
    #print 'tr',tr

def printUnivList(ulist,num):
    tplt = "{:^10}\t{:^10}\t{:^10}"
    print (tplt.format("排名","学校名称","分数"))
    for i in range(num):
        u = ulist[i]
        print (tplt.format(u[0],u[1],u[2]))


if __name__=='__main__':
    imp.reload(sys)
    imp.setdefaultencoding('utf-8')

    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  #20
