# Using reverse function
n = int(input("Enter the length of arrays:\t"))
l1 = []

print("Enter elements for list")
for i in range(n):
    l1.append(int(input(f"Enter element no {i + 1} :\t")))


l2 = [*l1]
l2.reverse()
l3 = []
for i in range(n):
    l3.append(l1[i] + l2[i])

print(*l3)


# Without using reverse 
n = int(input("Enter the length of arrays:\t"))
l1 = []
l2 = []

print("Enter elements for list")
for i in range(n):
    l1.append(int(input(f"Enter element no {i + 1} :\t")))

for i in range(n - 1, -1, -1):
    l2.append(l1[i])

l3 = []
for i in range(n):
    l3.append(l1[i] + l2[i])

print(*l3)
