# Q9. Create a decorator to cache function results

# This decorator stores (caches) the result of a function
# so that if the same input is used again,
# the result is returned instantly without recalculating.
def cache_decorator(func):

    # Dictionary to store cached results
    # key   → function input
    # value → function output
    cache = {}

    # Wrapper function that replaces the original function
    def wrapper(n):

        # Check if result for this input already exists in cache
        if n in cache:
            print("Returning cached value")
            return cache[n]   # return saved result

        # If result is NOT cached
        else:
            print("Calculating and caching result")

            # Call the original function
            result = func(n)

            # Store result in cache for future use
            cache[n] = result

            # Return the calculated result
            return result

    # Return the wrapper function
    return wrapper


# Apply the decorator to the square function
@cache_decorator
def square(n):
    # Returns the square of the number
    return n * n


# First time → value is calculated and cached
print(square(4))

# Second time → cached value is returned
print(square(4))