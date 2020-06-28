import scrapy
from bs4 import BeautifulSoup


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    # def parse(self, response):
    #     pass


def start_requests(self):
    for i in range(0, 10):
        url = f'https://movie.douban.com/top250?start={i*25}'
        yield scrapy.Request(url=url, callback=self.parse)

def parse(self, response):
    item = []
    soup = BeautifulSoup(response.text, 'html.parser')
    title_list = soup.find_all('div', attrs={'class': 'hd'})
    for i in range(len(title_list)):
        item = DoubanmovieItem()
        

