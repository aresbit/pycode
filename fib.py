# test

# fib

# def fib(n):
#     return  n if n < 2 else fib(n-1) + fib(n-2)



# cache = {}

# def fib(n):
#     if n in cache:
#         return cache[n]

#     else:
#         cache[n] = n if n < 2 else fib(n-1) + fib(n-2)
#         return cache[n]


# def fib(n):
#     def fib_acc(n, a, b):
#         if n < 2:
#             return a
#         else:
#             return fib_acc(n-1, a+b, a)
#     return fib_acc(n, 1, 0)



# def memoize(f):

#     cache = {}

#     def memoized(n):
#         if n in cache:
#             return cache[n]
#         else:
#             cache[n] = f(n)
#             return cache[n]
#     return memoized


# @memoize
# def fib(n):
#     return n if n < 2 else fib(n-1) + fib(n-2)




# def memoize(f):
#     cache = {}
#     def decorated_function(*args):
#         if args in cache:
#             return cache[args]
#         else:
#             cache[args] = f(*args)
#             return cache[args]
#     return decorated_function

# @memoize
# def fib(n):
#     return n if n < 2 else fib(n-2) + fib(n-1)


# def memoize(f):
#     cache = {}
#     return lambda *args: cache[args] if args in cache else cache.setdefault(args, f(*args))

# @memoize
# def fib(n):
#     return n if n < 2 else fib(n-2) + fib(n-1)


def memoize(f):
    cache = {}
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]

@memoize
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)


if __name__ == '__main__':
    print(fib(10))
    print(fib(200))