factors = []
num = 600851475143
d = 2
while num > 1:
    while num % d == 0:
        factors.append(d)
        num /= d
    d += 1

print factors