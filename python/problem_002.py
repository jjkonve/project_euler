from common.fibonacci import fibonacci_generator


print(sum([n for n in fibonacci_generator(4000000) if n % 2 == 0]))
