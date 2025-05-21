def n23(N):
    n23_list = [] 
    queue = [1] 

    while len(n23_list) < N:
        k = queue.pop(0) 
        if k not in n23_list:  
            n23_list.append(k)
            queue.append(2 * k + 1)  
            queue.append(3 * k + 1)
    return sorted(n23_list)

N = int(input("N = "))
print(N,"so dau tien cua N23:", *n23(N))