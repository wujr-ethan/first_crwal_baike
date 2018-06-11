# coding:utf-8
from lxml import etree
from urllib.parse import urljoin

class HTMLparser(object):
    def parser(self, page_url, page_text):
        if page_url is None or page_text is None:
            return None
        
        html = etree.HTML(page_text)
        new_urls = self._get_new_urls(page_url, html)
        new_datas = self._get_new_datas(page_url, html)
        return new_urls, new_datas

    def _get_new_urls(self, page_url, html):
        urls = set()
        all_url = html.xpath(".//div[@class='lemma-summary']//a[@target='_blank']/@href")
        if all_url is None:
            return None
        for url in all_url:
            if url is not None:
                abs_url = urljoin(page_url, url)
                urls.add(abs_url)
        
        return urls
    
    def _get_new_datas(self, page_url, html):
        datas = {}
        description = html.xpath(".//meta[@name='description']/@content")
        title = html.xpath(".//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()")
        datas['url'] = page_url
        datas['title'] = title
        datas['description'] = description
        return datas