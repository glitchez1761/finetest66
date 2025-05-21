def F(n):
    tong = 0
    for k in range(1, n+1):
        S = k * (k + 1) // 2  # Tổng từ 1 đến k
        tong += S ** (1 / k)
    return tong

n = int(input("N = "))
print(f"F({n}) = {F(n):.7f}")