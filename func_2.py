import random as r

def func_2() :
    komp_numb = r.randint(1,11)
    attemp = 1
    while True:
        user_numb = input(f"oylagan soningiz{komp_numb} mi")
        if user_numb == 'yes':
            attemp = 1
            break
        elif user_numb == 'greater':
            komp_numb += 1

        elif user_numb == 'lower':
            komp_numb -= 1
        attemp += 1
        
    return attemp