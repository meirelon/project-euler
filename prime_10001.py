# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(x):
    return x > 1 and all(x % n for n in range(2, x, 1))

number = 1
prime_count = 0

while prime_count < 10001:
    number+=1
    if is_prime(number):
        prime_count+=1

print(number)
