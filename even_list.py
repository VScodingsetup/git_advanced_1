even_list

from typing import List

def even_list(int_list: List[int]) -> List[int]:
    return [num for num in int_list if num % 2 == 0]