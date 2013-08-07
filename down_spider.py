import urllib
import re #正则
def downURL(url,filename):
    print url
    print filename
    try:
        fp=urllib.urlopen(url)
    except:
        print 'download exception'
        return 0
    op=open(filename,"wb")
    while 1:
        s=fp.read()
        if not s:
            break
        op.write(s)
        fp.close()
        fp.close()
        return 1

def getURL(url):
    try:
        fp=urllib.urlopen(url)
    except:
        print 'get url exception'
        return 0
    pattern=re.compile("http://sports.sina.com.cn/[^\>]+.shtml")#http://sports.sina.com.cn/[^>]+.shtml
    while 1:
        s=fp.read()
        if not s:
            break
        for u in urls:
            print u
        
    fp.close()
    return urls

def spider(startURL,times):
    urls=[]
    urls.append(startURL)
    i=0
    while 1:
        if i>times:
            break
        if len(urls)>0:
            url=urls.pop(0)
            print url,len(urls)
            downURL(url,str(i)+'.html')
            i=i+1
            if len(urls)<times:
                urllsit=getURL(url)
                for url in urllist:
                    if urls.count(url)==0:
                        url.append(url)
        else:
            break
    return 1

spider('http://www.sina.com.cn',5)

