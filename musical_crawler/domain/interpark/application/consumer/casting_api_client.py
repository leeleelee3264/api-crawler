from typing import Dict

import requests

from musical_crawler.domain.common.api_client import GetApiClient
from musical_crawler.domain.interpark.exceptions import CastingInfoNotFoundError


class CastingApiClient(GetApiClient):

    def __init__(self):
        self._casting_url = 'https://api-ticketfront.interpark.com/v1/goods/casting/schedule'

    def get(self, url: str):
        pass

    def get_with_query_params(self, url: str, query_params: Dict) -> dict:

        try:
            headers = {'Content-Type': 'application/json'}

            res = requests.get(
                url=url,
                headers=headers,
                params=query_params,
            )

            res.raise_for_status()
            payload = res.json()

            return payload
        except requests.exceptions.HTTPError as e:
            raise CastingInfoNotFoundError(
                'Interpark casting info not found. '
                f'{e.response.content}'
                f'{query_params}'
            )
