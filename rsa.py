import math
import random

class RSA:
    def __init__(self, modulus, public_key, private_key=None):
        self.private_key = private_key
        self.public_key = public_key
        self.modulus = modulus

    def encode(self, message):
        return (message**self.public_key) % self.modulus

    def decode(self, message):
        return (message**self.private_key) % self.modulus



def generate_keyset():
    primes = prime_sieve(100,200)
    
    p = random.choice(primes)

    while True:
        q = random.choice(primes)
        
        # Close, but not too close
        if 0.1 < abs(math.log(p, 2) - math.log(q, 2)) < 30:
            break

    modulus = p*q
    phi = (p-1)*(q-1)

    

def solve_diophantic(a, b):
    ''' Using the Euclidean algorithm this procedure
    solves a*x + b*y = 1 for x and y if a and b are coprime. '''

    # Ensure that a > b
    if a < b:
        a, b = b, a 

def euclidean(a, b):
    q = 0
    while a-b > 0:
        a -= b
        q += 1

    result = euclidean


def prime_sieve(lower_n, upper_n):
    max_divisor = int(math.sqrt(upper_n))
    divisors = range(2, max_divisor+1)

    numbers = list(range(lower_n, upper_n+1))

    for divisor in divisors:
        next_numbers = []
        for number in numbers:
            if number % divisor != 0:
                next_numbers.append(number)

        numbers = next_numbers
    
    return numbers
