def my_generator(n):
    for i in range(n):
        yield i

gen = my_generator(5)
for value in gen:
    print(value)