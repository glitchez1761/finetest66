def tong_2n(n):
    s = 0
    if n>=0:
        for i in str(2**n):
            s += int(i)
        print("Tong =", s)

n = int(input("N = "))
tong_2n(n)