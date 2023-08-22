#!/usr/bin/env python3
"""
Module for task 0-simple_helper_function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination parameters.

    Arguments:
    - page: int
        The page number, 1-indexed.
    - page_size: int
        The size of each page.

    Returns:
    - tuple of (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index