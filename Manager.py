# coding:utf-8
from HTMLDownloader import HTMLDownloader
from HTMLparser import HTMLparser
from URLmanager import URLmanager
from StoreDatas import StoreDatas

class SpinderMan(object):
    def __init__(self):
        self.downloader = HTMLDownloader()
        self.parser = HTMLparser()
        self.manager = URLmanager()
        self.output = StoreDatas()
    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while (self.manager.has_new_urls() and self.manager.old_urls_length() <= 100):
            try:
                new_url = self.manager.get_new_url()
                html_text = self.downloader.download(new_url)
                newer_url, raw_data = self.parser.parser(new_url, html_text)
                data = self.output.store_datas(raw_data)
                self.manager.add_new_urls(newer_url)
# except Exception as e:
#     print("crawl faild")
            finally:
                self.output.store_as_csv()

if __name__ == '__main__':
    spider_man = SpinderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.html")