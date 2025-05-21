def xoa_trung(a, b, c):
    day_so = [a, b, c]
    day_so = list(set(day_so))
    day_so.sort()
    return day_so

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
day_so = xoa_trung(a, b, c)
print("Xep tang dan:", *day_so)