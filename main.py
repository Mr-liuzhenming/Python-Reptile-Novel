# 导入包
from cgitb import text
import requests,os
from lxml import etree

# 定义方法
def downnovel(novname, savepath, ist):
    url_one = 'https://www.xbiquwx.la/s.php?seaey={}'.format(novname)
    r = requests.get(url_one).content.decode()
    b = etree.HTML(r)
    c = b.xpath('//*[@id="wrapper]/table/tr[2]/td[1]/a/@href')[0]
    url = 'https://www.xbiquwx.la'+c
    r2 = requests.get(url).content
    b1 = etree.HTML(r2)
    xsm = os.path.join(savepath, novname)
    if not os.path.isdiI(xsm):
        os.makedirs(xsm)
    clist = b1.xpath('//*[@id="list"/dl/dd')
    for i in clist:
        chapter = i.xpath('./a/text()')[0]  # 文章名称
        link = i.xpath('./a/@href')[0]  # 文章链接
        r1 = requests.get(url + link).content
        b2 = etree.HTML(r1)
        c1 = b2.xpath('//*[@id="content"]/text()')
        if list == 2:
            f = open(xsm + '/' + novname + '.txt', 'a', encoding='utf-8')
            f.write(chapter + '\n')
        for d in c1:
            text = d
            if ist == 1:
                f = open(xsm + '/' + chapter + 'text', 'a+', encoding='utf-8')
            f.write(text + '\n')
        print("下载完成：", chapter)
if __name__ == '__name__':
    # 输入要下载的小说名称
    novname = '明克街13号'
    # 设置小说保存路径
    savepath = r'./Test'
    # 下面参数输 1：每一章都保存1个txt文件 2：整部小说保存为一个txt文件
    ist = 2
    # 调用方法，开始下载
    downnovel(novname, savepath, ist)
