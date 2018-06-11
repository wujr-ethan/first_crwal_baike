# coding:utf-8

import requests

class HTMLDownloader(object):
    def download(self, url):
        if url is None:
            return None
        user_agent="User-Agent:Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)\
                AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
        headers = {'User-Agent':user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding='utf-8'
            return r.text
        return None
