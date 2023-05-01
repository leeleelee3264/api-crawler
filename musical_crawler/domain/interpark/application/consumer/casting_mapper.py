from musical_crawler.domain.interpark.dto.casting import CastingQuery, Casting


class CastingMapper:

    def __init__(self):
        self._start_date = 'startDate'
        self._end_date = 'endDate'
        self._goods_code = 'goodsCode'
        self._place_code = 'placeCode'

    def to_casting_query_dict(self, query: CastingQuery) -> dict:
        pass

    def to_casting_dto(self, res: dict) -> Casting:
        pass
