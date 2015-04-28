# coding: utf8

from proxymanager import ProxyManager

class ProxyMiddleware(object):

    def __init__(self):
        self.proxy_manager = ProxyManager("proxy_list.txt", 6)

    def process_request(self, request, spider):
        request.meta["proxy"] = self.proxy_manager.get_proxy()
