def phan_loai_va_sap_xep(ds):
    so_nguyen = []
    so_thuc = []
    khac = []
    for tp in ds:
        if isinstance(tp, int):
            so_nguyen.append(tp)
        elif isinstance(tp, float):
            so_thuc.append(tp)
        else:
            khac.append(tp)
    
    so_nguyen.sort(reverse=True)
    so_thuc.sort(reverse=True)
    khac.sort(reverse=True)
    return so_nguyen, so_thuc, khac

n = int(input("Nhap N: "))
ds = []
for i in range(n):
    tp = input(f"Nhap gia tri thu {i + 1}: ")
    try:
        if '.' in tp:
            ds.append(float(tp)) 
        else:
            ds.append(int(tp)) 
    except ValueError:
        ds.append(tp)  

so_nguyen, so_thuc, khac = phan_loai_va_sap_xep(ds)

print("A =", so_nguyen)
print("B =", so_thuc)
print("C =", khac)