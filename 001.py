#Project Euler: Problem 1

sum = 0
for x in range(1000):
  if 0 in [x % 3, x % 5]:
    sum += x
print(sum)
