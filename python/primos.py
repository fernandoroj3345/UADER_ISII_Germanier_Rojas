import time
# prime number calculator: find all primes up to n
max = int(input("Fino a quale numero vuoi trovare i numeri primi?  : "))
primeList = []
#for loop for checking each number
for x in range(2, max + 1):
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
<<<<<<< HEAD
print ("Fecha y hora " + time.strftime("%c"))
=======
print(primeList)
print(time.strftime("%c"))
>>>>>>> 2809dbc96fec6660c2874734fe43d1ae3e343b1e
#-------------------------------------------------------------
# prime number calculator: find the first n primes
count = int(input("Quanti cugini vuoi trovare?: "))
primeList = []
x = 2
while len(primeList) < count:
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
	x += 1
print(primeList)
<<<<<<< HEAD
print ("Fecha y hora " + time.strftime("%c"))
=======
print(time.strftime("%c"))
>>>>>>> 2809dbc96fec6660c2874734fe43d1ae3e343b1e
