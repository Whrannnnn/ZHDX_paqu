import requests
import bs4
from bs4 import BeautifulSoup


# 爬取url的信息，输出url的相关内容，返回给其他程序
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 提取HTML信息中关键数据，并且放入一个List列表中
def fillUnivList(ulist, html):
    # 利用soup对html代码进行解析
    soup = BeautifulSoup(html, "html.parser")
    # 解析tbody所在的位置，在tbody标签中找到tr标签
    for tr in soup.find('tbody').children:
        # 利用isinstance()过滤非标签类型的其他信息，必须是bs4中定义的element.Tag类型
        if isinstance(tr, bs4.element.Tag):
            # 在tr标签中找到td标签的相关信息，将所有的td标签存入一个名为tds的列表当中
            a = tr('a')
            tds = tr('td')  # 将所有的td标签存为一个列表类型
            ulist.append([tds[0].text.strip(), a[0].string.strip(), tds[4].text.strip()])  # 11.17更新后代码
        # 原来代码ulist.append([tds[0].string.strip(),a[0].string.strip(),tds[4].string.strip()])


# 将UnivList中的信息打印出来，num表示要打印出来多少信息
def printUnivList(ulist, num):
    # "{3}^12"指的是打印学校排名使用chr(12288)来进行填充，"^"表示居中对齐
    tplt = "{0:^10}\t{1:{3}^12}\t{2:^10}"
    # 0、1、2为槽,{3}表示若宽度不够,使用format的3号位置处的chr(12288)(中文空格)进行填充
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
     # unifo列表用于存储大学排名
    unifo = []
    url = "https://www.shanghairanking.cn/rankings/bcur/2020"
    html = getHTMLText(url)
    # 装入列表unifo中
    fillUnivList(unifo, html)
    printUnivList(unifo, 20)


main()
