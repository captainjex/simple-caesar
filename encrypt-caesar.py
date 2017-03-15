message = input('\nCAESAR CIPHER ENCRYPT\n==========================\nmasukkan plaintext yang mau di encript\n>').lower()
key = input('\n\n>>> masukkan key (int)\n>')

letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (letters.index(l) + n) % 26
            result += letters[i]
        except ValueError:
            result += l

    return result.lower()


# def decrypt(n, ciphertext):
#     """Decrypt the string and return the plaintext"""
#     result = ''
#
#     for l in ciphertext:
#         try:
#             i = (letters.index(l) - n) % 26
#             result += letters[i]
#         except ValueError:
#             result += l
#
#     return result


def show_result(plaintext, n):
    """Generate a resulting cipher with elements shown"""
    encrypted = encrypt(n, plaintext)
    # decrypted = decrypt(n, encrypted)

    print ('\n>>> Result')
    print ('key: %s' % n)
    print ('Plaintext: %s' % plaintext)
    print ('Encrytped: %s' % encrypted)
    # print ('Decrytped: %s' % decrypted)


if __name__ == '__main__':
    show_result(message, 3)
