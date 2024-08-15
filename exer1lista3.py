n = int(input("numero: "))
while n < 0 or n > 10:
    print("erro")
    n = int(input("numero: "))
print(f"você digitou {n}")
