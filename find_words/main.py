import uzwords
import get_word
import display
import creat_dsp
import replace

def main_game():
    wrong_answers = ''
    word = get_word.get_word(uzwords.words)
    created_word = creat_dsp.creat_dsp(word)
    print(created_word)
    while True:
        if '-' in created_word:
            word2 = input('harf kiriting')
            index_letter = display.dispaly_word(word2,word)
            if index_letter:
                created_word = replace.replace_letter(word2,index_letter,created_word)
                print(created_word.upper())
            else:
                print('afsuski bu harf mavjud emas')
                print(created_word.upper())
                wrong_answers += word2
                print(f"notogri tergan harlaringiz:{wrong_answers.upper()}")

        else:
            break
    attemp = len(wrong_answers)
    print(f"tabriklaymiz siz {attemp} urunishda topdingiz")
    print(created_word.upper()) 



print('oyin oynashni xohlaysizmi')
accept = input('ha/yoq')
if accept == 'ha':
   main_game()
else:
   print('sog salomat boling')

