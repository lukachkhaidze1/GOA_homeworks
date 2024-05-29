#here i created variable named car and its value = []
cars = []
#now i am going to make "for i cicle"
for i in range(5):
#now i am using input function to thell the user to give me their car breand 5 times
    car = input("please enter car brand: ")
    cars.append(car)
    #here i changed the first input of the user to "koninsegg"
    cars[0] = "koninsegg"
    #and at finally last i printed the result pf "cars"
    print(cars)
