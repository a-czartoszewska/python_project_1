import string

def get_letter(input_letter, shift, decipher):
    # function that gives a letter after deciphering (if decipher==True) or cipher
    alphabet = string.ascii_letters[0:26]
    base = 97
    input_letter_num = ord(input_letter)-base
    if decipher:
        return alphabet[(input_letter_num-shift)%len(alphabet)]
    else:
        return alphabet[(input_letter_num+shift)%len(alphabet)]