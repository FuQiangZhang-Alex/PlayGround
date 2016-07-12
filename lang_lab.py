
x = (ord(a) for a in '12345')
print(list(x))


def get_square(s):
    for i in range(s):
        yield i ** 2

print(list(get_square(5)))
print('{1}, {0}, {2:.2f}'.format(42.2, 'spam', 1 / 3.0))
