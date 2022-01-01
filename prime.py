import math

primeLimit = 10000001
isPrime = []
ithings = []
for i in range(primeLimit):
   isPrime.append(True)
isPrime[0] = False
isPrime[1] = False
for i in range(int(math.sqrt(primeLimit))):
   if isPrime[i] == True:
      for j in range(i**2, primeLimit, i):
         isPrime[j] = False
print(isPrime[2371])