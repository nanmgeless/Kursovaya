from django.db import models


class Statistics:
    def __init__(self, symbol_count: dict, str_len: int, s: str):
        self.symbol_count = symbol_count
        self.str_len = str_len
        self.s = s
