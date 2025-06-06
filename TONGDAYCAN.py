tong_can = lambda n: sum(((i * (i + 1) / 2) ** 0.5) for i in range(1, n + 1))

n = int(input("N = "))
print(f"F({n}) = {round(tong_can(n), 7)}")
