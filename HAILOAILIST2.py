def hai_list(ds):
    kieu_so = []
    kieu_khac = []
    for gt in ds:
        if isinstance(gt, float):
            kieu_so.append(gt)
        else:
            kieu_khac.append(gt)
    return kieu_so, kieu_khac

def tbc_so(kieu_so):
    return 0 if len(kieu_so) == 0 else print("TBC cua A =", float(sum(kieu_so) / len(kieu_so)))

n = int(input("Nhap N: "))
ds = []
for i in range(n):
    gt = input(f'Nhap gia tri thu {i+1}: ')
    try:
        ds.append(float(gt))
    except ValueError:
        ds.append(gt)

kieu_so, kieu_khac = hai_list(ds)
tbc_so(kieu_so)
print("B =", kieu_khac)