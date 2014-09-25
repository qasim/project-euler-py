#Project Euler: Problem 3

from functions import get_primes

number = 600851475143
primes = get_primes(10000)
divisible_primes = []
for x in primes:
  if number % x == 0:
    divisible_primes.append(x)
print(max(divisible_primes))
