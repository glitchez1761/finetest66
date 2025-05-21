def tong_luy_thua_n(n):
    tong = 0
    giai_thua = 1
    for i in range(1,n+1):
        giai_thua *= i
        tong += giai_thua
    print(f"F({n}) = {tong}")

n = int(input("Nhap N duong: "))
tong_luy_thua_n(n)