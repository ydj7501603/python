#coding=utf-8
import urllib
import urllib2
import zlib
import re
import gzip
import StringIO
import time


def getHtml(url):
        request = urllib2.Request(url,headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Cookie':'PHPSESSID=qr3e6qtaomimcp2v6rpv23b2e1; CNZZDATA950900=cnzz_eid%3D2139419118-1449367098-http%253A%252F%252Fwww.1073.net%252F%26ntime%3D1455884302'
        }); 
        response = urllib2.urlopen(request,timeout=3);
        html = response.read();
        return html;

def getContents(page):
        pattern = re.compile('<h3><a href="htm_data/2/1602/(.*?).html" target="_blank" id="">(.*?)</a></h3>',re.S)
        items = re.findall(pattern,page);
        return items;


def saveFile(content,fileName):
        fileName=fileName+'.txt';
        f = open(fileName,'w+');
        f.write(content.decode('utf-8').encode('utf-8','ignore'));
        f.flush();
        f.close();

fileName = 'page';

num=1
content='--------------------------------------------------'
content+=str(time.strftime('%Y-%m-%d %H:%M:%S'))

while(num<=300):

        url = 'http://www.baidu.com/'+str(num);

        html = getHtml(url);
        items = getContents(html);

        content+='\r\n'
        for item in items:
                id = item[0]
                it = item[1]
                it = item[1].decode('gb2312','ignore').encode('utf-8','ignore');
                if "鍗楀簞鍥涗腑" in it:
                        print it+id;
                        content+=id+'###'+it+'###';
                        content+='\r\n'
        num+=1;

        time.sleep(0.8)

print content;


