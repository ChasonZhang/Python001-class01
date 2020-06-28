import scrapy
from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector
from bs4 import BeautifulSoup as bs


class Top10Spider(scrapy.Spider):
    name = 'top10'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&sortId=1']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
            'Cookie': 'uuid_n_v=v1; uuid=551E9B80B85D11EAB4E28FB161D5B82B20B7B3F6B30D4415BD87C8FC120EA552; _csrf=b2fac22b64d62204dae47f958d75d3f3aa76ff800b3dab6cbd64d50d5ac9c13e; _lxsdk_cuid=172f53aa891c8-0dc14be1817201-31607402-13c680-172f53aa891c8; _lxsdk=551E9B80B85D11EAB4E28FB161D5B82B20B7B3F6B30D4415BD87C8FC120EA552; mojo-uuid=e6244ceab3bb39859e17a77dce2a70e6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593252162,1593252182; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593275271; __mta=221493543.1593252162022.1593275252543.1593275271827.19; _lxsdk_s=172f69a3bc3-933-662-261%7C%7C11',
            'Connection': 'keep-alive',
        }
        url = 'https://maoyan.com/films?showType=3&sortId=1'
        yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    # def parse(self, response):
    #     pass

    def parse(self, response):
        items = []
        # movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]  and position() <= 10')
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info" and position() <= 10]')
        for movie in movies[:10]:
            item = MaoyanmovieItem()
            # 获取电影名称film_name
            # film_name = tag.find('span').text
            film_name = movie.xpath('./div[1]/span[1]/text()')
            item['film_name'] = film_name.extract_first()
            # print(f'电影名称：{film_name}')
            # 获取电影类型film_type
            # film_type = tag.find_all('span')[2].next_sibling.strip()
            film_type = movie.xpath('./div[2]/text()')
            item['film_type'] = film_type[-1].extract().strip()
            # print(f'电影类型：{film_type}')
            # 获取上映时间film_date
            film_date = movie.xpath('./div[4]/text()')[-1].extract().strip()
            # film_date = tag.find_all('span')[-1].next_sibling.strip()
            item['film_date'] = film_date
            # print(f'上映时间：{film_date}')
            # print('\n')
            items.append(item)

        return items


    # def parse(self, response):
    #     items = []
    #     bs_info = bs(response.text, "html.parser")
    #     tags = bs_info.find_all('div', attrs={'class': 'movie-hover-info'}, limit=10)

    #     for tag in tags:
    #         item = MaoyanmovieItem()
    #         # 获取电影名称film_name
    #         film_name = tag.find('span').text
    #         item['film_name'] = film_name
    #         # print(f'电影名称：{film_name}')
    #         # 获取电影类型film_type
    #         film_type = tag.find_all('span')[2].next_sibling.strip()
    #         item['film_type'] = film_type
    #         # print(f'电影类型：{film_type}')
    #         # 获取上映时间film_date
    #         film_date = tag.find_all('span')[-1].next_sibling.strip()
    #         item['film_date'] = film_date
    #         # print(f'上映时间：{film_date}')
    #         # print('\n')
    #         items.append(item)
    #     return items