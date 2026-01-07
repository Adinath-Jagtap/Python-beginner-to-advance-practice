#11. Create a generator that yields even numbers from 1 to 100

def even_gen(n=100):
    for i in range(2, n+1, 2):
        yield i

g = even_gen(100)
print(next(g))  # 2
print(list(even_gen(20)))  # even numbers up to 20