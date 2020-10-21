#password at least 6 chars -> 12 chars

# DATA
#     ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#     ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     digits = '0123456789'
#     hexdigits = '0123456789abcdefABCDEF'
#     octdigits = '01234567'
#     printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
#     punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#     whitespace = ' \t\n\r\x0b\x0c'

import random
import string

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str
sample = "dcmm2201"
test = ""
cnt = 0
while (sample != test):
    test = get_random_alphanumeric_string(len(sample))
    cnt +=1
    print(cnt," ",test)
