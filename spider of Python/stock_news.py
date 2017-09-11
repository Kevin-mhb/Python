source:
      http://news.cnstock.com/news/sns_yw/index.html
      view-source:http://news.cnstock.com/news/sns_yw/index.html  (html文档)


import requests
from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep,ctime
import os
import threading
import queue

all_urls = []
news_data_title = []
#for item in range(1,116):
#    pages_list = []
#    pages = 'http://news.cnstock.com/news/sns_yw/'+str(item)
#    for page in pages:
#        pages_list.append(page)
page_url = ['{}{}'.format('http://news.cnstock.com/news/sns_yw/',page) for page in range(1,116)]#获得115页所有的url


def get_links_and_title():     #获得目录页面的新闻标题和新闻链接
    for one_page in page_url:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
        html = requests.get(one_page, headers=headers)
        metadata = html.text
        soup = BeautifulSoup(metadata, 'html.parser')
        links_part = soup.find_all('ul',class_='new-list article-mini')  #此处获得相关新闻模块的源码
        for links in links_part:
            a = links.find_all('a')
            for one in a:
                #print(one)
                href = one.attrs['href']
                all_urls.append(href)#将链接放到列表中

                news_title = one.get_text()  #attrs['title']  #使用此方法期间遇到有的a标签没有title属性导致报错
                news_data_title.append(news_title)  #将标题放到列表中
                pprint('新闻链接:{}'.format(href))
                pprint('新闻标题:{}'.format(news_title))
    #print(len(all_urls))  此方法统计所有页面的新闻链接数量  （共计3451个）

def get_url_text():  # 获取单个新闻页面的新闻内容
    file_directory = r'C:\Users\马海斌\Desktop\文件\programing\GitHub\Python\spider of Python'  # 创建文件目录
    news_index = 1  # 申明文件初始的索引号
    num_news = 0  # 申明一个变量统计爬取文章的数量
    for url in all_urls:
        num_news += 1
        if num_news == 1000:
            sleep(10)  #设置睡眠条件和时间
            num_news = 0
        else:
            html = requests.get(url)
            metadata = html.text
            soup = BeautifulSoup(metadata,'html.parser')
            try:
                file_title = soup.find('h1').get_text()
            except AttributeError:
                pass

            file_title = file_title.replace('*','')
            file_title = file_title.replace('|','')
            file_title = file_title.replace('?', '')
            file_title = file_title.replace('"', '')
            file_title = file_title.replace('"', '')
            file_title = file_title.replace('>', '')
            file_title = file_title.replace('<', '')
            file_title = file_title.replace(':', '')
            file_title = file_title.replace('\\', '')
            file_title = file_title.replace('/', '')
            file_title = file_title.replace('\r\n', '')

            t = ''  # 申明写入的文件的初始局部变量
            try:
                news_time = soup.find('span', class_='timer').get_text()  # 获取新闻页面的发布时间
                t += '<新闻发布时间：{}>'.format(news_time)
            except AttributeError:
                pass

            for text in soup.select('div.content > p'):
                t += text.get_text()
            t += '<新闻链接：{}>'.format(url)  #文件中加上url

            #print(t)
            with open(os.path.join(file_directory, str(file_title)) + '.txt', 'a',encoding='utf8') as file:
                file.write(t)
                news_index += 1
    #text = soup.find_all('p') 此方法不够精确
    #t = ''
    #for w in text:
    #    t += w.get_text()
    #pprint(t)
if __name__ == '__main__':

    get_links_and_title() # 得到所有的标题链接

    get_url_text() # 得到单链接的新闻文本

