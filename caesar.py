
def get_letter(input_letter, shift, cipher):
    """ function that gives a letter after ciphering (if cipher==True) or decipherering
    in caesar cipher with a left shift, takes only capital letters
    """
    if input_letter > 'Z' or input_letter < 'A': print('Wrong letter')
    if cipher:
        return chr((ord(input_letter)-ord('A')-shift)%26+ord('A'))
    else:
        return chr((ord(input_letter)-ord('A')+shift)%26+ord('A'))

def caesar(string, shift_len, cipher):
    """Function to cipher or decipher a message from/into caesar cipher with a left shift of shift_len.
    Put cipher=True to cipher into caesar sipher."""
    result = ""
    for i in string:
        if i == ' ': result += i
        else: result += get_letter(i, shift_len, cipher)
    return result


# print(caesar('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 3, True))
# print(caesar('QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD', 3, False))
# print(get_letter('A', 3, False))
# print(get_letter('C', 3, True))


