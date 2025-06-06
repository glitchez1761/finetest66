import math

def tong_uoc_so(n):
    tong = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n // i
    return tong

n = int(input("N = "))
print(f"Tong cac uoc so cua {n} la {tong_uoc_so(n)}")