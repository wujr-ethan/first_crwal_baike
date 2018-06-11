# coding:utf-8

class URLmanager(object):
    def __init__(self):
        self.new_urls_set = set()
        self.old_urls_set = set()
    
    def new_urls_length(self):
        '''
        Return the number of new urls
        '''
        return len(self.new_urls_set)

    def old_urls_length(self):
        '''
        Return the number of old urls
        '''
        return len(self.old_urls_set)

    def has_new_urls(self):
        '''
        Detemine whether there is no new urls
        '''
        return self.new_urls_length() != 0
    
    def add_new_url(self, url):
        '''
        Add new url
        '''
        if url is None:
            return None

        if url not in self.new_urls_set and url not in self.old_urls_set:
            self.new_urls_set.add(url)

    def add_new_urls(self, urls):
        '''
        Add new urls
        '''

        if urls is None or len(urls) == 0 :
            return
        for url in urls:
            self.add_new_url(url)
    
    def get_new_url(self):
        '''
        Get new url
        '''
        new_url = self.new_urls_set.pop()
        self.old_urls_set.add(new_url)
        return new_url