def ban_tron(n, k):
    result = 0  # Bat dau voi chi so 0 (nguoi thu 1)
    for i in range(2, n + 1):  # Duyet tu 2 den n
        result = (result + k) % i
    return result + 1  # Danh so tu 1 thay vi 0

n = int(input("So nguoi ngoi quanh ban: "))
k = 3
print(f"Nguoi o lai cuoi cung la nguoi thu {ban_tron(n, k)}")