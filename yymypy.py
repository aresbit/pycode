# from typing import List, Set

# def unique_count(nums: list[int]) -> int:
#     """counts the number of unique items in the list"""
#     uniques: set[int] = set()  # Manually added type information
#     for num in nums:
#         uniques.add(num)

#     return len(uniques)

# print(unique_count([1, 2, 1, 3, 1, 2, 4, 3, 1]))  # 4

from typing import List, Union

def print_item(item: Union[str, List[str]]) -> None:
    reveal_type(item)

    if isinstance(item, list):
        for data in item:
            reveal_type(item)
            print(data)
    else:
        reveal_type(item)
        print(item)

print_item('Hi!')
print_item(['This is a test', 'of polymorphism'])
