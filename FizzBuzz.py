
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num, 'FizzBuzz')
    elif num % 3 == 0:
        print(num, 'Fizz')
    if  num % 5 == 0:
        print(num,'Buzz')
    else:
        print(num)