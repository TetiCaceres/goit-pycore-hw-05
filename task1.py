def caching_fibonacci():
    # create an empty cache (dictionary)
    cache = {}

    def fibonacci(n):
        # base cases
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # if the value is already in the cache — return it immediately
        if n in cache:
            return cache[n]
        
        # compute recursively and store the result in the cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    # return the inner function that "remembers" the cache (closure)
    return fibonacci


# Usage example
# create a cached Fibonacci function
fib = caching_fibonacci()

# compute Fibonacci numbers
print(f"fib(6) = {fib(6)}")   # Output: 8
print(f"fib(10) = {fib(10)}") # Output: 55
print(f"fib(15) = {fib(15)}") # Output: 610


