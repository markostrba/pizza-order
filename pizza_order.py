print('Thank you for choosing Python Pizza Deliveries!')
size = input('S, M, L ')
add_pepperoni = input()
extra_cheese = input()
small_pizza = 15
medium_pizza = 20
large_pizza = 25

extra = 0
if size == 'S':
    if add_pepperoni == 'Y':
        extra += 2
        if extra_cheese == 'Y':
            extra +=3
            print(small_pizza+extra)
        else:
            extra +2
            print(small_pizza+extra)
    elif extra_cheese == 'Y':
        extra +=1
        print(small_pizza+extra)
    else:
        print(small_pizza)
elif size == 'M' or size == 'L':
    if add_pepperoni == 'Y':
        extra += 3
        if extra_cheese == 'Y':
            extra +=4
            if size == 'M':
                print(medium_pizza+extra)
            else:
                print(large_pizza+extra)
        else:
            extra +3
            if size == 'M':
                print(medium_pizza+extra)
            else:
                print(large_pizza+extra)
    elif extra_cheese == 'Y':
        extra +=1
        if size == 'M':
            print(medium_pizza+extra)
        else:
            print(large_pizza+extra)        
    else:
        if size == 'M':
            print(medium_pizza+extra)
        else:
            print(large_pizza+extra)            