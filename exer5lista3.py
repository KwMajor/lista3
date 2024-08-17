n1 = int(input("N: "))
n2 = int(input("N: "))
while n1 % n2 !=0:
    n1, n2 = n2, n1 % n2
print(n2)