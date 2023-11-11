

def replace_letter(letter,index_letter,word:str):
    word1 = word
    position = index_letter
    new_letter = letter
    

    word2 = word1[:position] + new_letter + word1[position + 1:] 
    return word2


