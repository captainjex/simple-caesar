# Caesar Cipher Hacker

message = input('\nCAESAR CIPHER BRUTE FORCE\n==========================\nmasukkan cipher text yang mau di decript\n>').lower()
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

for key in range(len(LETTERS)):
    translated = ''

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key
            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)
            # add number's symbol at the end of translated
            translated = translated + LETTERS[num]
        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol
    # display the current key being tested, along with its decryption
    print('Key #%s: %s' % (key, translated))
