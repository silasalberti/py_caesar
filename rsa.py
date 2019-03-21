import math
import random

DEBUG = False

class RSA:
    def __init__(self, n, e, d=None):
        self.private_key = (n, d)
        self.public_key = (n, e)
        self.e = e
        self.d = d
        self.n = n

    def encode(self, message):
        return (message**self.public_key) % self.modulus

    def decode(self, message):
        return (message**self.private_key) % self.modulus



def generate_keyset():
    primes = prime_sieve(10000,20000)
    
    p = random.choice(primes)

    while True:
        q = random.choice(primes)
        
        # Close, but not too close
        if 0.1 < abs(math.log(p, 2) - math.log(q, 2)) < 30:
            break

    n = p*q # Modulus
    phi = (p-1)*(q-1) # Euler phi function

    e = 65537

    if n % e == 0:
        print("This is actually possible.")
        return generate_keyset()

    d, _ = solve_diophantic(e, phi)

    if d<0:
        d += phi

    # public_key = (n, e)
    # private_key = (n, d)

    return RSA(n, e, d)

    

def solve_diophantic(a, b):
    ''' Using the Euclidean algorithm this procedure
    solves a*x + b*y = gcd(a,b) for x and y. '''

    # Ensure that a > b
    if a < b:
        a, b = b, a 

    if DEBUG:
        print(f"q: _, r: {a}, s: 1, t: 0")
        print(f"q: _, r: {b}, s: 0, t: 1")

    return euclidean(a, b, 1, 0, 0, 1)[1:]

def gcd(a,b):
    ''' Computes the gcd (greatest common divisor) of a and b.
    Utilizes the (extended) euclidean algorithm.'''

    # Ensure that a > b
    if a < b:
        a, b = b, a 

    return euclidean(a, b, 1, 0, 0, 1)[0]

def lcm(a, b):
    ''' Computes the lcm (least common multiple) of a and b.
    Utilizes the function gcd. '''

    return int(a*b/gcd(a,b))

def euclidean(r0, r1, s0, s1, t0, t1):
    ''' Recursive implementation of the extended Euclidean
    algorithm. 

    q for quotient, r for remainder, s and t the right values
    in the table. The lowermost part of the table always looks
    like this:

    _ r0 s0 t0
    _ r1 s1 t1
    q r2 s2 t2 

    If r2 is 0, then r1 is the gcd and t1 & s1 are the factors
    of the initial values for the remainder if the initial values
    for s0, s1, t0, t1 were 1, 0, 0, 1.'''


    q = 0
    r2 = r0
    while r2-r1 >= 0:
        r2 -= r1
        q += 1

    s2 = s0 - q * s1
    t2 = t0 - q * t1

    if DEBUG:
        print(f"q: {q}, r: {r2}, s: {s2}, t: {t2}")

    if r2 == 0:
        return r1, t1, s1
    else:
        return euclidean(r1, r2, s1, s2, t1, t2)


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
