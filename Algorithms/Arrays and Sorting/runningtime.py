def insertion_sort(l):
    count = 0;
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while j > -1 and key < l[j]:
            l[j+1] = l[j]
            j -= 1
            count += 1;
        l[j+1] = key
    return count;
        
m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
print(insertion_sort(ar))