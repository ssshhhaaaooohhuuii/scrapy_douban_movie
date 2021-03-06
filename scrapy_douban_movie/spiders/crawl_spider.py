# coding: utf8

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy_douban_movie.items import Movie


class Spider(CrawlSpider):

    """ Movie Spider """

    name = "movie_crawler"

    start_urls = ["http://movie.douban.com/tag/"]

    rules = (
        Rule(LinkExtractor(allow=('.tag/.*/?focus=movie'))),
        Rule(LinkExtractor(allow=('type=tag_more&amp;name=.*&amp;focus=movie&amp;mod=movie'))),
        Rule(LinkExtractor(allow=('object_id=\d+&amp;type=tag&amp;object_kind=\d+')),
             callback="parse_detail")
    )

    def parse_detail(self, response):
        """ parse detail """
        title_regx = r"//div[@id='content']/h1/span[@property='v:itemreviewed']/text()"
        movie = Movie()
        title = response.xpath(title_regx).extract()[0]
        print title
        movie["title"] = title
        movie["url"] = response.url
        return movie
