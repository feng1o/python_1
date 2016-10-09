# -*- coding: utf-8 -*-
import sys
import os
import re
import urllib
import urllib2
import threading


# an example of Baidu image search
# :http://image.baidu.com/i?ct=201326592&lm=-1&tn=result_pageturn&pv=&word=%E5%91%B5%E5%91%B5&z=0&pn=0&cl=2&ie=utf-8#pn=0
carrot_pos = "D:\\Python\\workspace\\Spider\\Carrot\\pos"
carrot_neg = "D:\\Python\\workspace\\Spider\\Carrot\\neg"
AbaloneMushroom_pos = "D:\\Python\\workspace\\Spider\\Abalone Mushroom\\pos"
AbaloneMushroom_neg = "D:\\Python\\workspace\\Spider\\Abalone Mushroom\\neg"
Apple_pos = "D:\\Python\\workspace\\Spider\\Apple\pos"
Apple_neg = "D:\\Python\\workspace\\Spider\\Apple\neg"
greenpepper_pos = "D:\\Python\\workspace\\Spider\\green pepper\\pos"
greenpepper_neg = "D:\\Python\\workspace\\Spider\\green pepper\\neg"
Greenvegetables_pos = "D:\\Python\\workspace\\Spider\\Green vegetables\\pos"
Greenvegetables_neg = "D:\\Python\\workspace\\Spider\\Green vegetables\\neg"
Pitaya_pos = "D:\\Python\\workspace\\Spider\\Pitaya\\pos"
Pitaya_neg = "D:\\Python\\workspace\\Spider\\Pitaya\\neg"
Potato_pos = "D:\\Python\\workspace\\Spider\\Potato\\pos"
Potato_neg = "D:\\Python\\workspace\\Spider\\Potato\\neg"
Tomatoes_pos = "D:\\Python\\workspace\\Spider\\Tomatoes\\pos"
Tomatoes_neg = "D:\\Python\\workspace\\Spider\\Tomatoes\\neg"
pospath = [carrot_pos, AbaloneMushroom_pos, Apple_pos, greenpepper_pos,
           Greenvegetables_pos, Pitaya_pos, Potato_pos, Tomatoes_pos]
negpath = [carrot_neg, AbaloneMushroom_neg, Apple_neg, greenpepper_neg,
           Greenvegetables_neg, Pitaya_neg, Potato_neg, Tomatoes_neg]

carrot_content = "%E9%B2%8D%E9%B1%BC%E8%8F%87"
AbaloneMushroom_content = '%E9%B2%8D%E9%B1%BC%E8%8F%87'
Apple_content = '%E8%83%BD%E5%90%83%E7%9A%84%E8%8B%B9%E6%9E%9C'
greenpepper_content = '%E9%9D%92%E6%A4%92%E5%9B%BE%E7%89%87'
Greenvegetables_content = '%E9%9D%92%E8%8F%9C%E5%9B%BE%E7%89%87'
Pitaya_content = '%E7%81%AB%E9%BE%99%E6%9E%9C%E5%9B%BE%E7%89%87'
Potato_content = '%E9%A9%AC%E9%93%83%E8%96%AF%E5%9B%BE%E7%89%87'
Tomatoes_content = '%E8%A5%BF%E7%BA%A2%E6%9F%BF%E5%9B%BE%E7%89%87'
content = [carrot_content, AbaloneMushroom_content, Apple_content, greenpepper_content, /, Pitaya_content, Potato_content, Tomatoes_content]

posnum = 20000
negsum = 5000
url1 = "http://image.baidu.com/i?ct=201326592&lm=-1&tn=result_pageturn&pv=&word="
url2 = "&z=0&pn=0&cl=2&ie=utf-8#pn=0"
url3 = "&z=0&pn="
url4 = "&cl=2&ie=utf-8#pn=0"
url11 = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1470135785167_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%83%A1%E8%90%9D%E5%8D%9C'
url12 = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1470134297380_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%B2%8D%E9%B1%BC%E8%8F%87'
url13 = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1470128818506_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%83%BD%E5%90%83%E7%9A%84%E8%8B%B9%E6%9E%9C'
url14 = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1470134429734_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%9D%92%E6%A4%92%E5%9B%BE%E7%89%87&f=3&oq=%E9%9D%92%E6%A4%92&rsp=7'
url15 = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1470134492754_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%9D%92%E8%8F%9C%E5%9B%BE%E7%89%87'
url16 = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1470134527255_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%81%AB%E9%BE%99%E6%9E%9C%E5%9B%BE%E7%89%87+'
url17 = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1470134652339_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%A9%AC%E9%93%83%E8%96%AF%E5%9B%BE%E7%89%87&f=3&oq=%E9%A9%AC%E9%93%83%E8%96%AF&rsp=0'
url18 = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1470134694910_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%A5%BF%E7%BA%A2%E6%9F%BF%E5%9B%BE%E7%89%87'
urll = [url11, url12, url13, url14, url15, url16, url17, url18]

finished = 0


def GetImage(index):
    global posnum
    global negnum
    global pospath
    global negpath
    global content
    global urll
    global finished

    i = index
    print index
    logname = pospath[i] + "\\ImageMessage.txt"  # ,"w"
    flog = open(logname, "w")
    count = 0
    successcount = 0
    flag = 1
    # 正样本下载
    for j in range(0, 334):
        # url1 + content[i] + url3 + str(j*60) +url4
        url = urll[i] + "&pn=" + str(j * 60)
        sock = urllib.urlopen(url)
        # print url

        # 正则表达式匹配下载地址·
        reg = re.compile(
            "(?<=objURL\":\")(http.*?\.(jpg|gif|png|bmp|jpeg|JPG))")
        html = sock.read()
        results = reg.findall(html)
        if results:
            os.chdir(pospath[i])
            for one in results:

               # 统计
                count = count + 1
                if (count > posnum):
                    print "down loadfinish"
                    flag = -1
                    break

                imgeurl = one[0]
                print "image:", one[0]
                # print imgeurl.rindex('.'),len(imgeurl)
                succname = imgeurl[
                    int(imgeurl.rindex('.')) + 1:int(len(imgeurl))]

                try:
                    savename = pospath[i] + "\\" + str(count) + "." + succname
                    downloadimge = urllib2.urlopen(
                        one[0], timeout=5)  # , data, timeout)
                    f = open(savename, "wb")
                    f.write(downloadimge.read())
                    f.close()

                    size = os.path.getsize(savename)
                    flog.writelines("%s %s %s" % (savename, str(size), one[0]))
                    print "Download Success"
                    successcount = successcount + 1

                except BaseException, e:
                    flog.writelines("%s %s %s" % (savename, e, one[0]))
                    print "Fail download %s ... Error %s" % (imgeurl, e)
    flog.close()

    # 负样本下载
    logname = negpath[i] + "\\ImageMessage.txt"  # ,"w"
    flog = open(logname, "w")
    count = 0
    successcount = 0
    flag = 1
    for j in range(334, 418):
        #url = url1 + content[i] + url3 + str(j*60) +url4
        url = urll[i] + "&pn=" + str(j * 60)
        sock = urllib.urlopen(url)

        # 正则表达式匹配下载地址·
        reg = re.compile(
            "(?<=objURL\":\")(http.*?\.(jpg|gif|png|bmp|jpeg|JPG))")
        html = sock.read()
        results = reg.findall(html)
        if results:
            os.chdir(negpath[i])
            for one in results:

               # 统计
                count = count + 1
                if (count > negnum):
                    print "down loadfinish"
                    flag = -1
                    break

                imgeurl = one[0]
                print "image:", one[0]
                # print imgeurl.rindex('.'),len(imgeurl)
                succname = imgeurl[
                    int(imgeurl.rindex('.')) + 1:int(len(imgeurl))]

                try:
                    savename = negpath[i] + "\\" + str(count) + "." + succname
                    downloadimge = urllib2.urlopen(
                        one[0], timeout=5)  # , data, timeout)
                    f = open(savename, "wb")
                    f.write(downloadimge.read())
                    f.close()

                    size = os.path.getsize(savename)
                    flog.writelines("%s %s %s" % (savename, str(size), one[0]))
                    print "Download Success"
                    successcount = successcount + 1

                except BaseException, e:
                    flog.writelines("%s %s %s" % (savename, e, one[0]))
                    print "Fail download %s ... Error %s" % (imgeurl, e)
    flog.close()
    finished = finished + 1

if __name__ == '__main__':
    # 初始化线程
    threads = []
    for k in range(0, 8):
        t = threading.Thread(target=GetImage, args=(k,))
        threads.append(t)
        threads[k].start()
        # print k
print finished
while finished is not 8:
    continue
print "finished: (%s/%s) downloaded"
