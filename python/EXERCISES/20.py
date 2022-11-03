for i in range(1, 100+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        print('fizzbuzz')
    elif i % 3 == 0:
        print(i)
        print('fizz')
    elif i % 5 == 0:
        print(i)
        print('buzz')
    
    