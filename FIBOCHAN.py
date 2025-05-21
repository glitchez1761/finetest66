import math
def so_chinh_phuong(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def so_fibonacci(n):
    return so_chinh_phuong(5 * n * n + 4) or so_chinh_phuong(5 * n * n - 4)

n = int(input("N = "))
if so_fibonacci(n) and n % 2 == 0:
    print("N la so fibonacci chan")
else:
    print("N khong phai la so fibonacci chan")