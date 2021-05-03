"""
File: caesar.py
Name: Justin Kao
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    The encrypted string will be shifted back by Caesar Cipher method,
    then we'll find out the true string.
    """
    dspc = int(input("Secret number: "))
    encrypt = input("What's the ciphered string: ")
    encrypt = encrypt.upper()
    new_s = decipher_define(dspc)
    ans = decipher(encrypt, new_s)
    print("The deciphered string is:", ans)


def decipher_define(dspc):
    """
    Define the new ALPHEBET order.
    :param dspc: The displacement need to shift.
    :return: new_s
    """
    new_s = ""
    divide = len(ALPHABET) - dspc
    new_s = ALPHABET[divide:] + ALPHABET[:divide]
    return new_s


def decipher(encrypt, new_s):
    """
    Find out the original string by look up to the position in new ALPHABET order,
    and correspond to the original ALPHABET by the same position.
    :param encrypt:
    :param new_s:
    :return: ans(the original string)
    """
    ans = ""
    for ch in encrypt:
        if ch in ALPHABET:
            ans += ALPHABET[new_s.find(ch)]
        else:  # assign punctuation marks directly.
            ans += ch
    return ans



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
