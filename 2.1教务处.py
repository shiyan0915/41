"""

1.爬取福大教务通知https://jwch.fzu.edu.cn/jxtz.htm要求:

。获取教务通知(最近100条即可，但需要获取总页数或条数)

。提取通知信息中的"通知人“(如:质量办、计划科)、标题、日期、详情链接.

。爬取通知详情的html,可能存在附件",提取附件名,附件下载次数,附件链接吗，有能力请尽可能将附件爬取下来。。上述内容- 律要去除回车、括号等无用符号

。把除附件外爬取到的数据存入数据库中
"""
import requests
from lxml import html
etree=html.etree
import pymysql

if __name__ == "__main__":

    db = pymysql.connect(
    host="localhost",
    user="shiyan",
    password="123456",
    database = "fzu"
    )

    cursor = db.cursor()

    cursor.execute("CREATE DATABASE if not exists fzu")


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76'
    }
    url ='https://jwch.fzu.edu.cn/jxtz.htm'
    page_text=requests.get(url=url,headers=headers).content
    tree=etree.HTML(page_text)
    li_list=tree.xpath('//div[@class="box-gl clearfix"]/ul[1]/li')
    #print(li_list)
    number=tree.xpath('//div[@class="ecms_pag"]/div[1]/div[1]/span[1]/span[9]/a/text()')[0]#总页数
    notice=[]
    while 1:
        page=0
        if page==0:
            url=url
            page+=1
        elif page!=0:
            for page in range(number-1)[::-1]:
                url = 'https://jwch.fzu.edu.cn/jxtz/{}.htm'.format(page)
        page_text=requests.get(url=url,headers=headers).content
        tree=etree.HTML(page_text)
        li_list=tree.xpath('//div[@class="box-gl clearfix"]/ul[1]/li')
        for li in  li_list:
            if len(notice)>=99:
                break
            href = li.xpath('./a/@href')[0]
            detail_url='https://jwch.fzu.edu.cn/'+href#链接
            detail_page_text = requests.get(url=detail_url,headers=headers).content
            detail_tree=etree.HTML(detail_page_text)
            detail_name=detail_tree.xpath('//p[@class="w-main-dh-text"]/a[3]/text()')[0]#通知人
            detail_title=detail_tree.xpath('//div[@class="wapper"]/form[1]/div[1]/div[1]/div[1]/div[1]/h4/text()')[0]#标题
            detail_time=detail_tree.xpath('//div[@class="wapper"]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span/text()')[0]#日期
            notice.append(detail_title)
            sql = "insert into notice (detail_name,detail_title,detail_url,detail_time) values('%s','%s','%s','%s')" % (detail_name, detail_title, detail_url, detail_time)
            cursor.execute(sql)
            if detail_tree.xpath('//ul[@style="list-style-type:none;"]')!=[]:#附件
                fujian_list=detail_tree.xpath('//ul[@style="list-style-type:none;"]/li')
                for fujian in fujian_list:
                    fujian_title=fujian.xpath('./a/text()')[0]#附件名
                    #fujian_cishu=fujian.xpath('./span/text()')[0]#附件下载次数
                    fujian_url=fujian.xpath('./a/@href')[0]#附件链接
            print("爬取成功")

        cursor.close()
        db.close()














