def pot2(n):
    print('n inicio:', n)
    if n == 0:
        resp = 20
        
    else:
        print('Antes de operar n:', n)
        resp = 2 * pot2(n-1)
    print('operacion: ', resp)
    print('n: ', n)
    return resp
print(pot2(5))
#print(2**5)


