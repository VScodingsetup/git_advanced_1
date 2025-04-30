main.py

from typing import List

def main():
    input_str = input()
    int_list = list(map(int, input_str.split()))
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(int_list)
    print(output)
    
    
if __name__ == "__main__":
    main()