sum_of_squares_of_even

def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    even_numbers = even_list(even_int_list)
    return sum(num ** 2 for num in even_numbers)
