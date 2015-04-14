# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Field


class Movie(scrapy.Item):

    """ Movie item"""

    url = scrapy.Field()
    title = scrapy.Field()
    director = scrapy.Field()
    writer = scrapy.Field()
    performer = scrapy.Field()
    m_type = scrapy.Field()
    country = scrapy.Field()
    language = scrapy.Field()
    release_date = scrapy.Field()
    film_length = scrapy.Field()
    intro = scrapy.Field()
