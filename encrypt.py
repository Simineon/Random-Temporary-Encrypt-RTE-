from random import *

# global variables
g = None
char_to_number = {}
number_to_char = {}

def init_generator():
    global g
    g = get_number()
    next(g)

# getting numbers
def get_number():
    used_numbers = set()
    ch = yield

    while True:
        if ch not in char_to_number:
            if ch == ' ':
                char_to_number[ch] = 0
            else:
                # randomize
                main_random = randint(1, 99)
                while main_random in used_numbers:
                    main_random = randint(1, 99)
                used_numbers.add(main_random)
                char_to_number[ch] = main_random
                number_to_char[main_random] = ch
        # NOT IN IF!!!
        ch = yield char_to_number[ch]

# encrypt data
def encrypt(data):
    global g
    result = ""

    for char in data:
        r = g.send(char)
        result += str(r) + "-"

    print(result)
    return result.rstrip('-')

# dencrypt data
def decrypt(encrypted_data):
    result = ""

    numbers = encrypted_data.split("-")

    for num_str in numbers:
        if num_str:
            number = int(num_str)
            if number in number_to_char:
                result += number_to_char[number]
            else:
                result += " "
    print(result)
    return result

# init global variables
init_generator()

# while True:
#     inp = input()
#     encrypt(inp)

# # Encrypting
# original_text = "hello, world!"
# encrypted = encrypt(original_text)
# print(f"Encrypted: {encrypted}")
#
# # Decrypting
# decrypted = decrypt(encrypted)
# print(f"Decrypted: {decrypted}")