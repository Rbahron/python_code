import random as r

def func_1 ():
    komp_numb = r.randint(1,11)
    attemp = 0
    while True :
        user_numb = int(input('oylagan sonni kiriting'))
        if komp_numb > user_numb :
            print('no my number greater')
        elif komp_numb < user_numb :
            print('my number lower')
        else: 
            print ('yes you find')
            break
        attemp += 1
    return attemp