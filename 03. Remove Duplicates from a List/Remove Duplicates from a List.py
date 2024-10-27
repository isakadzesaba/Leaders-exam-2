def duplicates(lst):
    u = []
    s = set()

    for i in lst:
        if i not in s:
            u.append(i)
            s.add(i)
    
    return u

print(duplicates([1, 2, 2, 3, 4, 4, 5]))
print(duplicates(['a', 'b', 'a', 'c']))