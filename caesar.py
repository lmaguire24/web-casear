# this is to decrypt the second part of the crypto pro
def alphabet_position(letter):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in letter.lower():
        number = alpha.find(letter)
    else:
        number = ALPHA.find(letter)
    return number


# rotate the characters based on the rot
def rotate_character(char, rot):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = alphabet_position(char)
    new_value = number + rot
    if char.isalpha():
        if char in char.lower():
            return alpha[new_value % 26]
        else:
            return ALPHA[new_value % 26]
    else:
        return char

# print an encrypted string
def encrypt(message, rot):
    encrypted = ''
    for char in message:
        encrypted += rotate_character(char, rot)
    return encrypted