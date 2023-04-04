from dataclasses import dataclass
from datetime import date


@dataclass
class CastingQuery:
    start_date: date
    end_date: date
    goods_code: str
    place_code: str


@dataclass
class Casting:
    """
    실제 casting 데이터를 담고 있는 DTO
    """
    pass
