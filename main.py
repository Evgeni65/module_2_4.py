numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [2]
not_primes = []
for i  in numbers[1:]:
    for j in numbers[1:(i-1)]:
       if i%j == 0:
        not_primes.append(i)
        break
       if i%j != 0 and i - j <= 1:
        primes.append(i)
print('primes: ', (primes) )
print('not_primes: ', (not_primes) )