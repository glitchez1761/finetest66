def F(n):
    tong = 0
    tong_binh_phuong = 0
    for k in range(1, n+1):
        tong_binh_phuong += k**2
        tong += n / tong_binh_phuong
    return tong
n = int(input("N = "))
print(f"F({n}) = {F(n):.7f}")