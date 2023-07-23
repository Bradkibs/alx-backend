#!/usr/bin/env python3

""" Contains a function that takes 2 args (page, page_size)
and returns a tuple containing start index and end index
corresponding to the range of indexes to return in alist
for those particular pagination parameters"""


from typing import Tuple


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
