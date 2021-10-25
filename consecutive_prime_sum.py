# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

def is_prime(x):
    return x > 1 and all(x % n for n in range(2, x, 1))

def argmax(iterable):
    return max(enumerate(iterable), key=lambda x: x[1])[0]

all_primes_below_1m = [p for p in range(2,10**6,1) if is_prime(p)]

start = 0
iter = 1
end = len(all_primes_below_1m)-1
consecutive_primes_list = []


for i in range(0,end):
    for j in range(1,end):
        consecutive_primes = all_primes_below_1m[i:j]
        if sum(consecutive_primes) > all_primes_below_1m[end]:
            continue
        if is_prime(sum(consecutive_primes)) and sum(consecutive_primes) < all_primes_below_1m[end]:
            consecutive_primes_list.append(consecutive_primes)

consecutive_primes = consecutive_primes_list[argmax([len(c) for c in consecutive_primes_list])]

print(len(consecutive_primes), sum(consecutive_primes))
