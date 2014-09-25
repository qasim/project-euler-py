def get_primes(limit):
  n = list( range(2, limit + 1) )
  current_prime = 2
  while current_prime < n[-1]:
    not_primes = []
    for x in n:
      if x % current_prime == 0 and x != current_prime:
        n.remove(x)
    for x in range(len(n)):
      if n[x] > current_prime:
        current_prime = n[x]
        break
  return n
