l1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
l2 = ['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']

# Method 1
# TC: O(n)
# SC: O(n) + Auxiliary
l3 = []

for i in range(len(l1)):
    if l1[i] != None and l2[len(l2) - i - 1] != None:
        l3.append(l1[i] + l2[len(l2) - i - 1])
    elif l1[i] != None:
        l3.append(l1[i])
    elif l2[len(l2) - i - 1] != None:
        l3.append(l2[len(l2) - i - 1])

print(*l3)


# Method 2
# TC: O(n)
# SC: O(1) + Auxiliary
for i in range(len(l1)):
    if l1[i] != None and l2[len(l2) - i - 1] != None:
        l1[i].append(l2[len(l2) - i - 1])
    elif l1[i] != None:
        l1[i]
    elif l2[len(l2) - i - 1] != None:
        l3.append(l2[len(l2) - i - 1])

