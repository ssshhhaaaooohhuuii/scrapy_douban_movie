# coding: utf8

import scrapy

from scrapy import Request
from scrapy_douban_movie.items import Movie


class Spider(scrapy.Spider):

    """ Movie Spider """

    name = "movie_spider"

    start_urls = ["http://movie.douban.com/tag/"]

    RULES = {
        "cates": r"//table[@class='tagCol']/tbody/tr/td/a[@class='tag']/@href",
        "movie_list": r"//div[@class='mod movie-list']/dl/dt/a/@href",
        "title": r"//div[@id='content']/h1/span[@property='v:itemreviewed']/text()"
    }

    def parse(self, response):
        """ parse """
        cates = response.xpath(
            self.RULES["cates"]).extract()
        for url in cates[:3]:
            real_url = url[:url.rindex("/")] + "/movie"
            yield Request(real_url, self.parse_cate_page)

    def parse_cate_page(self, response):
        """ parse cate page """
        movie_list = response.xpath(
            self.RULES["movie_list"]).extract()
        for url in movie_list[:4]:
            yield Request(url, self.parse_detail)

    def parse_detail(self, response):
        """ parse detail """
        movie = Movie()
        movie["title"] = title = response \
            .xpath(self.RULES["title"]).extract()[0]
        movie["url"] = response.url
        return movie
