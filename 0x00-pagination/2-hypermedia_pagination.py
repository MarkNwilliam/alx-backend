import math

class Server:
    DATA = [
        # Mocked data...
    ]

    def __init__(self):
        pass

    def get_page(self, page: int = 1, page_size: int = 10) -> list:
        # Assume you have the implementation of this method from the previous task...

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        # Utilize the get_page method
        data = self.get_page(page, page_size)
        
        # Calculate total pages
        total_pages = math.ceil(len(self.DATA) / page_size)

        # Calculate next and previous pages
        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page - 1 > 0 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

# Example
# server = Server()
# print(server.get_hyper(1, 2))
