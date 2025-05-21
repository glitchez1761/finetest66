# Nhập 3 số nguyên a, b, c
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

# Kiểm tra điều kiện để 3 số có thể là cạnh của một tam giác
if a + b > c and a + c > b and b + c > a:
    print("Dung la tam giac")
else:
    print("Khong phai tam giac")