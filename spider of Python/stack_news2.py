""" database：SqlServer2008 r2
    author:solheng
    time:2017-05-31        """
import requests
from bs4 import BeautifulSoup
from time import sleep
import pymssql
import re
all_urls = []
news_data_title = []
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

def get_url_text():  # 获取单个新闻页面的新闻内容
    num_news = 0  # 申明一个变量统计爬取文章的数量
    global url
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
                global file_title
                file_title = soup.find('h1').get_text()
            except AttributeError:
                pass

            global t
            t = ''  # 申明写入的文件的初始局部变量
            try:
                global news_time
                news_time = soup.find('span', class_='timer').get_text()  # 获取新闻页面的发布时间
                global news_date
                date_pat = '\d{4}-\d*-\d*'  # 匹配发布日期
                news_date = re.findall(date_pat,news_time)
            except AttributeError:
               pass
            for text in soup.select('div.content > p'):
                info = text.get_text()
                t += info

        tit = file_title
        i = t
        u = url
        n = news_time
        n2 = news_date
        conn = pymssql.connect(host='********', user='********', password='********', database='********',charset='utf8')
        c = conn.cursor()
        sql = 'INSERT INTO BDNews(title,info,url,newsTime,newsDate) VALUES (%s,%s,%s,%s,%s)'
        try :
            c.execute(sql,(tit,i,u,n,n2,))
        except pymssql.OperationalError:
            pass
        conn.commit()
        c.close()
        conn.close()
        print('ok')

if __name__ == '__main__':
    get_links_and_title()
    get_url_text()
