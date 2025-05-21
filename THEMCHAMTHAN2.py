def them_cham_than(s):
    if s.endswith('!!!'):
        print("Chuoi S sau khi xu ly: " + s)
    else:
        count = 0
        for c in reversed(s):
            if c == '!':
                count += 1
            else:
                break
        s = s + '!' * (3 - count)
        print("Chuoi S sau khi xu ly: " + s)

s = str(input("Nhap S: "))
them_cham_than(s)