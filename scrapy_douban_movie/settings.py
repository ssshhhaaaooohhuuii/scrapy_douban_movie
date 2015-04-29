# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_douban_movie project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_douban_movie'

SPIDER_MODULES = ['scrapy_douban_movie.spiders']
NEWSPIDER_MODULE = 'scrapy_douban_movie.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'scrapy_douban_movie.proxymw.ProxyMiddleware': 100,
}

DOWNLOAD_TIMEOUT = 10

CONCURRENT_REQUESTS = 100

RETRY_TIMES = 7

RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 408, 403]

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 6.3; WOW64)"
    "AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/39.0.2171.71 Safari/537.36"
)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_douban_movie (+http://www.yourdomain.com)'
