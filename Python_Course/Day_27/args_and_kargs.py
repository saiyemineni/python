def add(*args):
    sum_of_numbers = 0
    for num in args:
        sum_of_numbers += num

    return sum_of_numbers


print(add(4, 5, 6, 7, 8))

def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
calculate(add = 2, multiply = 5)