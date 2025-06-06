xoa_trung = lambda a,b,c: sorted(set([a,b,c]))

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
day_so = xoa_trung(a, b, c)
print("Xep tang dan:", *day_so)