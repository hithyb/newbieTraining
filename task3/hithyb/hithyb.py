# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 17:10:00 2015

@author: Administrator
"""
import random
import httplib
import urllib2
import re
def getnum(urls):
    url=getaim(urls)
    p='<div class="topBox ">\t\r\n\t\t(.*?)\t\r\n\t</div>'
    try:
        req=urllib2.Request(url)
        page=urllib2.urlopen(req).read()   
    except:
        print u'网络错误'
    finddata=re.findall(p,page,re.S)
    num=eval(finddata[0])
    return num



def getaim(url):
    p='/commend/(.*?)htm'
    try:
        req=urllib2.Request(url)
        page=urllib2.urlopen(req).read()   
    except:
        print u'网络错误'
    finddata=re.findall(p,page,re.S)
    aimpage="http://today.hit.edu.cn/commend/"+finddata[0][:7]+"1.htm"
    return aimpage

    
    
def shua(url,times):
    tmp=getaim(url)
    aimpage=tmp[23:]
    for i in range(1,times+1):
        conn = httplib.HTTPConnection("today.hit.edu.cn")
        a = random.randint(1,255)
        b = random.randint(0,255)
        c = random.randint(0,255)
        d = random.randint(0,255)
        ipAddress = "%d.%d.%d.%d" % (a,b,c,d)
        headers={"X-Forwarded-For":ipAddress,"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0"}
        conn.request("HEAD",aimpage,"",headers)
        res=conn.getresponse()
        if res.reason=="OK" :
            print i,"ok"
        else:
            print i,"fail"
        conn.close()




print u"搞哪个"
url=raw_input()
n=getnum(url)
print u"已经有",n,u"个赞了"
print u"搞到多少"
aimnum=eval(raw_input())
shua(url,aimnum-n)