t = 1, 2
print (t)
print (type(t))
person = 'Steve', 21, 57891.50
print (person)
def midpoint(x1, y1,x2, y2):
	x = (x1 + x2 )/2
	y = (y1 + y2) /2
	return x, y
print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)
print(m[0], m[1])

i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break

i = 0
while i < 3:
	i = i + 1
	print ('hey', i)
i = 0
while i<10:
	print(i)
	i = i + 3
print ('final value of i is', i)

for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)

for i in range(5): print (i)
for i in range(0 , 5): print(i)
for i in range(0, 5, 1): print(i)
basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)

for i in range(len(basket)):
	print(basket[i])

for i in range(7):
	if i % 2 == 0: print(i, 'is even')
	else: print(i, 'is odd')





def sum(n):
    x = 0
    for numbers in range(0, n+1):
        x = x + numbers
    print(x)

def factorial(n):
    x = 1
    for numbers in range(1, n+1):
        x = x * numbers
    return x


def nchoosek(n, k):
    nchhosek = factorial(n)/(factorial(k)*factorial(n-k))
    return nchhosek

def euler(n):
    euler = 0
    for n in range(1, n+1):
        euler = euler + 1/factorial(n)
    print(euler)

def isprime(n):
    for i in range(2, n):
        if n%i == 0:
            print(f'{n} is not a prime number, it\'s divisible by {i}')
            return False
    print(f"{n} is a prime number")
    return True

def Nilakantha(n):
    for n in range(1, n):
        a = 2
        a = 2*n
        pi = 3 - (4/((a*(a+1)*(a+2))))*(-1)**(n)
    print (pi)



if __name__ == '__main__':
    Nilakantha(100)
    euler(1000)
    isprime(17)
    sum(n=int(input("Enter a number: ")))
    n = int(input("Enter a number to calculate the factorial: "))
    print(factorial(n))
    print(nchoosek(n, int(input("Enter a number to calculate the factorial: "))))