def xoa_cham_than(s):
    result = s.replace("!", "")
    return result

s = input("Nhap S: ")
print("Chuoi S sau khi loai bo dau cham than:", xoa_cham_than(s))