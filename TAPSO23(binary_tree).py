def n23(n):
    n23_list = [1]
    index = 0
    insert_index = 1

    while insert_index < n:
        k = n23_list[index]
        num1 = 2 * k + 1
        num2 = 3 * k + 1

        if num1 not in n23_list[:insert_index]:
            n23_list.append(num1)
        if num2 not in n23_list[:insert_index]:
            n23_list.append(num2)

        index += 1
        insert_index = len(n23_list)

    return sorted(n23_list[:n])

N = int(input("N = "))
print(f"{N} so dau tien cua N23:", *n23(N))