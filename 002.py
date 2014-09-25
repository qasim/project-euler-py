#Project Euler: Problem 2

current = 1
last = 1
sum = 0
while current < 4000000:
  sum += current if current % 2 == 0 else 0
  current = last + current
  last = current - last
print(sum)
