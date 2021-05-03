"""
File: caesar.py
Name: Justin Kao
------------------------------
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program will do the Caesar Cipher to encrypt your message.
    """
    dspc = int(input("Enter secret key: "))
    message = input("What's the message you want to encrypt: ")
    message = message.upper()
    new_s = cipher_define(dspc)
    encrypt = decipher(message, new_s)
    print("The deciphered string is:", encrypt)


def cipher_define(dspc):
    """
    Define the new ALPHEBET order.
    :param dspc: The displacement need to shift.
    :return: new_s
    """
    new_s = ""
    divide = len(ALPHABET) - dspc
    new_s = ALPHABET[divide:] + ALPHABET[:divide]
    return new_s


def decipher(message, new_s):
    """
    Find out the original string by look up to the position in new ALPHABET order,
    and correspond to the original ALPHABET by the same position.
    :param message:
    :param new_s:
    :return: ans(the original string)
    """
    ans = ""
    for ch in message:
        if ch in ALPHABET:
            ans += new_s[ALPHABET.find(ch)]
        else:  # assign punctuation marks directly.
            ans += ch
    return ans



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
