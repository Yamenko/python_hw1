#TASK1
n = 123
n = str(n)
print(int(n[0]) + int(n[1]) + int(n[2]))


#TASK2
n = 120
print(int(n/6), int(n * 2 / 3),int(n/6) )


#TASK3
n = 385915
n = str(n)

if (int(n[0]) + int(n[1]) + int(n[2])) == (int(n[3]) + int(n[4]) + int(n[5])):
    print("yes")
else:
    print("no")


#TASK4
a = 3
b = 7
c = 6

if (c > 1 and (c % a == 0 or c % b == 0)) or (c == 1 and (a == 1 or b == 1)):
    print("yes")
else:
    print("no")