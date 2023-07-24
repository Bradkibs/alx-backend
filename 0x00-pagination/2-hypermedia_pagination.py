#!/usr/bin/env python3

""" Contains a function that takes 2 args (page, page_size)
and returns a tuple containing start index and end index
corresponding to the range of indexes to return in alist
for those particular pagination parameters"""


from typing import Tuple, List, Dict, Any
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple that contains a start and end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters eg:
    res = index_range(page=3, page_size=15)
    print(res)
    (30, 45)
    """
    end_idx: int = page_size * page
    start_idx: int = end_idx - page_size
    return tuple({start_idx, end_idx})


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns the paginated datasets according to the
        appropriate page and page size"""
        assert type(page) == int and type(page_size) == int, '''Assertion
        Error raised when page and/or page_size are not ints'''
        assert page > 0 and page_size > 0, '''AssertionError raised with
        negative values'''
        assert page != 0 and page_size != 0, 'AssertionError raised with 0'
        range_tup = index_range(page, page_size)
        return self.__dataset[range_tup[0]:range_tup[-1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """returns a dictionary containing the key-value pairs of
        page_size, page, data, next_page, prev_page, total_pages"""
        assert type(page) == int and type(page_size) == int, '''Assertion
        Error raised when page and/or page_size are not ints'''
        assert page > 0 and page_size > 0, '''AssertionError raised with
        negative values'''
        assert page != 0 and page_size != 0, 'AssertionError raised with 0'
        range_tup = index_range(page, page_size)
        hyper_media = {
            'page_size': len(self.dataset()[range_tup[0]:range_tup[-1]]),
            'page': self.dataset()[range_tup[0]:range_tup[-1]],
            'data': self.__dataset[range_tup[0]:range_tup[-1]],
            'next_page': page + 1
            if page < len(self.dataset()) // page_size else None,
            'prev_page': page - 1
            if page > 1 else None,
            'total_pages': len(self.dataset()) // page_size}
        return hyper_media
