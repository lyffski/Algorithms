def isPrime (n):
  if n < 1:
    return False
  for i in range (2, n, 1): #initial value, till n reached, in 1 steps //"like" for loop
    if n % i == 0:
      return False
  return True

def sieve (n):
  primes = []
  numbers = list(range(2, n))
  i = 2
  while i * i < n:
    for k in range(i, n, i):
      if k in numbers:
        numbers.remove(k)
    primes.append(i)
    i = numbers [0]
  return primes + numbers

def FermatTest(p): 
  from random import randrange
  return randrange(2, p) ** (p-1) % p == 1


def MillerRabinTest(p): #for high prime
  from random import randrange
  d = p - 1
  r = 0
  while d % 2 == 0:
      d //= 2
      r += 1
  a = randrange(2, p-1)
  x = (a ** d) % p
  if x == 1 or x == p-1:
      return True
  while r>1:
    x=(x * x)% p
    if x == 1:
      return False
    if x == -1:
      return True
    r -= 1
  return False  

def odd(num):
   for i in range(num):
      i=2
      if (num % i == 0):
         return False
      else:
         return True
def change(list, func):
   oddList = []
   for k in list:
      if func(k):
         oddList.append(k)
   return oddList
rawList = range(1, 20)
print(rawList)
print(change(rawList, odd))

print("Naive: ", isPrime(13))
print("Sieve: ", sieve(100))
print("FermatTest: ", FermatTest(13))
print("MillerRabinTest: ", MillerRabinTest(1103))