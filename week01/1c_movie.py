import requests
import lxml.etree
import pandas as pd


# 请求头
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent':user_agent}

# 获取《肖申克的救赎》豆瓣详情页
url = "https://movie.douban.com/subject/1292052/"
response = requests.get(url, headers=header)

"""
# 测试url获取是否正常
print(response.text)
print(f'返回码是：{response.status_code}')
"""

# xml化处理
selector = lxml.etree.HTML(response.text)

# 电影名称
film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称：{film_name}')

# 上映日期
plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映日期：{plan_date}')

# 豆瓣评分
rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'豆瓣评分：{rating}')

mylist = [film_name, plan_date, rating]
print(mylist)

movie1 = pd.DataFrame(data = mylist)

movie1.to_csv('/Users/zzz/Python001-class01/week01/movie1.csv', encoding='utf8', index=False, header=False)