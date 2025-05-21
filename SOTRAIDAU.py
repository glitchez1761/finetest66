def trai_dau(a,b,c):
    if a + b > 0 and a + c > 0 and b + c > 0:
        print("Khong co cap so trai dau")
    elif a + b < 0 and a + c < 0 and b + c < 0:
        print("Khong co cap so trai dau")
    else:
        print("Co cap so trai dau")
        
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
trai_dau(a,b,c)