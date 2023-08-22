def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """Get a specific page of the dataset."""
    
    
    # Use assert to check both page and page_size are positive integers
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0

    # Use index_range function to get start and end indices
    start_idx, end_idx = index_range(page, page_size)

    # Return the relevant portion of the dataset
    return self.dataset()[start_idx:end_idx]
