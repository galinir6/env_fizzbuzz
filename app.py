from icecream import ic


for x in range(1 , 101):
    if x % 5 == 0 and x % 3 == 0:
        ic('FizzBuzz')
    elif x % 5 == 0:
        ic('Buzz')
    elif x % 3 == 0:
        ic('Fizz')
    else: print(x)


    