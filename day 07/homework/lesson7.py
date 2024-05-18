#inport temperture in Celsius: 
celsius = int(input("please input youre temperture in Celsius: "))

print((celsius * 1.8)+ 32)

#______________________________
#lets improt youre age and see if it is more than 12 and less than 20, shall we ?

age = int(input("please enter youre age: "))

print(age > 12 and age < 20)

#__________________________________
#now import the side of a rectangle.

one_side = (float(input("please enter one side of the rectangle: ")))
second_side = (float(input("please input second side of the ractangle: ")))
third_side = (one_side * 2)
forth_side = (second_side * 2)
all_side = (one_side + second_side + third_side + forth_side)

print(all_side)
#_____________________________________
#youre num. again.
num = float(input("please enter youre choosen number: "))
print(num > 100 and num % 9)
#____________________________________
#lets try to use "And" and "Or" operator

plate = int(input("how many plates are on the shelf ?: "))
print(plate > 10 or plate < 10)

plate1 = int(input("how many plates are on the shelf ?: "))
print(plate > 10 and plate < 10)






