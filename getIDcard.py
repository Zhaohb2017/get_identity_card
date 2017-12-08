# -*- coding: utf-8 -*-
# python -version = 2.7
# Author：赵华兵
# Data : 2017-12-7
# 实现目的: 从网站获取身份证号码

import requests,sys,re,csv,os,datetime,xlrd

from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

def main (url,pathName,in_number=2):
    print datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    Name_Null = []
    Number_Null = []
    number=0
    while number<in_number:


        rq=requests.get(url)
        bsObj=BeautifulSoup(rq.text)
        namelist = bsObj.find_all("div",{"class":"table-con"})
        for name in namelist:
              name=name.get_text("span")
              name1=str(name)
              # print name1
              XM_list=name1[5:33]
              XM=XM_list[0:3]
              # print XM_list.split()[0]
              # print len(XM_list.split()[0])
              # print XM_list.split()[1]
              # print len(XM_list.split()[1])
              if len(XM_list.split()[0]) == 9 and len(XM_list.split()[1])==18:
                  Name_Null.append(XM_list.split()[0])
                  Number_Null.append(XM_list.split()[1])

        number += 1

        d=dict(zip(Name_Null,Number_Null))
        path=os.getcwd()+'/'+pathName
        with open(path, 'wb') as cf:
            writer = csv.writer(cf)
            writer.writerow(['shader', 'file'])
            for key, value in d.items():
                writer.writerow([key, value])
            cf.flush()
        cf.close()
print 'Done!'


if __name__ =="__main__":
    main(url="http://id.8684.cn/",pathName='GetIDcard.csv')