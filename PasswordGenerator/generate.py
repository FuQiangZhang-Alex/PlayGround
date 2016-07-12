
import random


def list2str(lst):
    ss = ''
    for s in lst:
        ss += str(s)
    return ss

r = random.Random()
Alpha = [chr(i) for i in range(65, 91)]
alpha = [chr(i) for i in range(97, 123)]
number = [n for n in range(0, 10)]
# print(ord('A'))
r.shuffle(Alpha)
r.shuffle(alpha)
r.shuffle(number)
a = alpha[:4]
A = Alpha[r.randrange(0, 26)]
num = number[:5]
print(A + list2str(a) + list2str(num))
