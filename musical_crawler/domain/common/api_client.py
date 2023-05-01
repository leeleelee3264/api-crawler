from abc import ABCMeta, abstractmethod
from typing import Dict


class GetApiClient(metaclass=ABCMeta):

    @abstractmethod
    def get(self, url: str):
        pass

    @abstractmethod
    def get_with_query_params(self, url: str, query_params: Dict):
        pass
