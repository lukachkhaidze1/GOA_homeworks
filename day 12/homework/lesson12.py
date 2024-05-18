#number 1:
for i in range(10):
    if i % 2 == 1:
        print(i)
#number 2:
for i in range(50):
    if i % 5 == 0:
        print(i)
#number 3:
user_choise = int(input("please enter any number for (for range) experiment: "))
for i in range(user_choise):
    print(i)

#number 4:
num = 0
for i in range(50):   
    print(i)
    num += i
    print(num)