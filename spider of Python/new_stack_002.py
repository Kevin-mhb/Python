import requests
from bs4 import BeautifulSoup
from pprint import pprint   
from time import sleep,ctime
import os 
import threading
import queue

all_urls = []
news_data_title = []
page_url = ['{}{}'.format('http://www.njupt.edu.cn/72/list.htm',page) for page in range(1,2)]

def get_links_and_title():
    for one_page in page_url:
        headers = {
        	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
        html = requests.get(one_page, headers=headers)
        metadata = html.text
        print(metadata)
        soup = BeautifulSoup(metadata, 'html.parser')
        links_part = soup.find_all('table',align="left")  
        print(links_part)
        for links in links_part:
            a = links.find_all('a')
            for one in a:
                href = one.attrs['href']
                all_urls.append(href)
                news_title = one.get_text()
                news_data_title.append(news_title)
                print(href)
                print(news_title)  
                pprint('新闻链接:{}'.format(href))
                pprint('新闻标题:{}'.format(news_title))  


def get_url_text():
    file_directory = r'C:\Users\马海斌\Desktop\文件\programing\Python\爬取文件'  
    news_index = 1  
    num_news = 0  
    for url in all_urls:
        num_news += 1
        if num_news == 1000:
            sleep(10)  
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

            t = ''  
            try:
                news_time = soup.find('span', class_='timer').get_text() 
                t += '<新闻发布时间：{}>'.format(news_time)
            except AttributeError:
                pass

            for text in soup.select('div.content > p'):
                t += text.get_text()
            t += '<新闻链接：{}>'.format(url)  

            with open(os.path.join(file_directory, str(file_title)) + '.txt', 'a',encoding='utf8') as file:
                file.write(t)
                news_index += 1


if __name__ == '__main__':

    get_links_and_title() 
    get_url_text() 
