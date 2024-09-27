c = 0
for k in range(18644, 33088):
    if "2" in str(k) and "7" not in str(k):
        c += 1
print(c)
print(len([c for c in range(18644, 33088)
           if "2" in str(c) and "7" not in str(c)]))