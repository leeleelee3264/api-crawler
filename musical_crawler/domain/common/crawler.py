from abc import ABCMeta, abstractmethod


class Crawler(metaclass=ABCMeta):

    @abstractmethod
    def crawl(self, url: str, selector: str):
        pass

    @abstractmethod
    def parse(self):
        pass
