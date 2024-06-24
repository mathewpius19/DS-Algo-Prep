# recursive
# O(2^N) Time | O(N) Space
def nthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return nthFib(n - 1) + nthFib(n - 2)


print(nthFib(6))

# Caching
# O(N) Time | O(n) Space
def nthMemoize(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = nthMemoize(n - 1, memoize) + nthMemoize(n - 2, memoize)
    return memoize[n]


print(nthMemoize(10))

# Iterative
# O(N) Time | O(1) Space


def nthIterative(n):
    if n <= 2:
        return 1
    f1 = 1
    f2 = 1
    fsum = 0
    for i in range(2, n):
        fsum = f1 + f2
        f1, f2 = f2, fsum
    return fsum


print(nthIterative(7))
