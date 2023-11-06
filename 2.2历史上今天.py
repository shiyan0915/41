"""2.爬取百度百科历史上的今天https://baike.baidu.com/calendar/
要求:

。获取- -年内每天的历史上的今天发生了什么，包括年份，事件类型(birth、 death等)， 标题,简要内容。.上述内容一 -律要去除回车、括号等无用符号

。把爬取到的数据存入数据库中"""

import requests
from lxml import html
import json
etree=html.etree
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76'
    }
    url = 'https://baike.baidu.com/calendar/'
    page_text=requests.get(url=url,headers=headers).content
    tree=etree.HTML(page_text)
    dd_list=tree.xpath('//div[@class="events-container"]/div[1]//dd')
    #print(dd_list)
    fp = open('2.2历史上今天.txt', 'w', encoding='utf-8')
    for dd in dd_list:
        year=dd.xpath('./div[1]/text()')[0]#年份
        type=dd.xpath('./div[3]/div[1]/div[1]/div[1]/a/a/text()')[0]#事件类型
        title=dd.xpath('./div[3]/div[1]/div[1]/div[1]/a/text()')[0]#标题
        content=dd.xpath('./div[3]/div[2]/text()')[0]#简要内容
        fp.write(year)
        fp.write(type)
        fp.write(title)
        fp.write(content)
        json.dump(dd_list, fp=fp, ensure_ascii=False)
        print("爬取成功")
    fp.close()

