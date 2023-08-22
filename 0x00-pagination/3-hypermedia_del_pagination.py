from typing import List, Dict

class Server:
    # ... [other methods and definitions] ...

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        # Step 1: Ensure the index is valid
        assert isinstance(index, int) and 0 <= index < len(self.__indexed_dataset)

        # Retrieve data for the page starting from the given index
        keys = sorted(self.__indexed_dataset.keys())  # sorted indices
        data = []
        next_index = index

        while len(data) < page_size and next_index < len(self.__indexed_dataset):
            if next_index in self.__indexed_dataset:
                data.append(self.__indexed_dataset[next_index])
                last_index = next_index  # Save the last added index
            next_index += 1  # Move to the next potential index

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
