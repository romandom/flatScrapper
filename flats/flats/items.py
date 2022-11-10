
from scrapy.item import Item, Field


import scrapy


class FlatsItem(scrapy.Item):
    title = Field()
    image_urls = Field()

