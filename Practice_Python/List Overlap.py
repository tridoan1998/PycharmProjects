a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = []
for i in range(0, len(a)):
    if (a[i] in b) is True:
        print(a[i])
        new_list.append(a[i])

print("print out the new list")
for i in range(0, len(new_list)):
    print(new_list[i])

another_list = []
print("Check for repeat")
for i in range(0, len(new_list)):
    print(new_list[i] , "repeat" , new_list.count(new_list[i]))
    if new_list.count(new_list[i]) < 2:
        another_list.append(new_list[i])
    if new_list.count(new_list[i]) > 1:



print("Final list")
for i in range(0, len(another_list)):
    print(another_list[i])




