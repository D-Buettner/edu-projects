nums = 0
for n in range(0, 1000):
    if n % 3.0 == 0:
        nums = nums + n
    elif n % 5.0 == 0:
        nums = nums + n
    else:
        pass

print nums
    