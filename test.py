# def inc(x: int) -> int:
#     return x + 1
# p = inc(1)

# print(p)


# from typing import Iterator


# def fib(n: int) -> Iterator[int]:
#     a, b = 0, 1
#     while a < n:
#         yield a
#         a, b = b, a + b

# if __name__ == '__main__':
#     for x in fib(20000):
#         print(x, end=' ')
# from typing import List

# def average(nums: List[int]) -> float:
#     total = sum(nums)
#     count = len(nums)
#     return total / count

# print(average([1, 2, 3, 4])) # 2.5



def generator(n):
    yield 'start'

    for i in range(n):
        yield f'item number {i+1}'

    yield 'end'

    return 42

for string in generator(3):
    print(string)

    