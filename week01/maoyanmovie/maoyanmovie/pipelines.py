# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        film_date = item['film_date']
        output = f'{film_name},{film_type},{film_date}\n'
        with open('/Users/zzz/Python001-class01/week01/Maoyan_Movie_Top_10_scrapy.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item