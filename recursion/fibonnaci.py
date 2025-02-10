from functools import lru_cache
@lru_cache(maxsize= None)

def fibonnaci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci (n-2)

# btw first term of fibonnaci series is 1 not 0

print(fibonnaci(900))