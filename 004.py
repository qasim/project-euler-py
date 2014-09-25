#Project Euler: Problem 4

p = []
for x in range(1000, 100, -1):
  for y in range(1000, 100 ,-1):
    if str(x*y) == str(x*y)[::-1]:
      p.append(x*y)
print(max(p))
