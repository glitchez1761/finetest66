def tong_uoc_so(n):
    tong = 0
    sqrt_n = int(n**0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n // i
    return tong

n = int(input("N = "))
print(f"Tong cac uoc so cua {n} la {tong_uoc_so(n)}")