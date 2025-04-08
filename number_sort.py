my_list = [2, 5, 3, 4, 1]

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[j] < my_list[i]:
            my_list[i], my_list[j] = my_list[j], my_list[i]

print(my_list)  
            
        