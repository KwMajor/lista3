a = 80000
b = 200000
npa = 0.03
npb = 0.015
anos = 0
while a < b:
    a = a + (a * npa)
    b = b + (b * npb)
    anos += 1
print(f"a população A vai ultrapassar a população B em {anos} anos!")