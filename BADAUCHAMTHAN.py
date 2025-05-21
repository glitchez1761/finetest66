def ba_cham_than(c):
    if c.endswith("!!!"):
        print("Chuoi sau khi bo sung dau cham than: '" + c + "'")
    else:
        count = 0
        for i in reversed(c):
            if i == "!":
                count += 1
            else:
                break
        c = c + "!" * (3 - count)
        print("Chuoi sau khi bo sung dau cham than: '" + c + "'")

c = str(input("Nhap chuoi: "))
ba_cham_than(c)
