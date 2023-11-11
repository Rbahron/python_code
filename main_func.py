import func_1 as user_find
import func_2 as komp_find

def find_numbr ():
    print('you find number')
    attemp = user_find.func_1()
    print(f"you find in {attemp} attemp")
    print('I will find number ')
    attemp2 = komp_find.func_2()
    print(f"I find in {attemp2} attemp")
    while True :
        ask = input('doyou wanna try again yes/no')
        if ask == 'yes':
            find_numbr ()
        else :
            break

find_numbr()