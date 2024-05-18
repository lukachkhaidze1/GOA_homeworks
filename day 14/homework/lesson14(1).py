
num_repetitions = int(input("Enter the number of repetitions: "))  
num_numbers = int(input("Enter the number of numbers to enter: "))
total_num = 0  
for _ in range(num_repetitions):  
    iteration_num = 0  
    for _ in range(num_numbers):  
        num = int(input("Enter a number: "))  
        iteration_num += num  
    total_num += iteration_num  
print("The sum of the input numbers is:", total_num)  
