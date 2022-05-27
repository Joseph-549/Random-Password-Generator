import random

def mainPassword():
        passwordList = "abcdefghijklmnoprstuvyz-_1234567890"
        passwordListTwo = "abcdefghijklmnoprstuvyz".upper()
        mainList = passwordList + passwordListTwo

        i = ""
        j = 0

        for _ in range(8):
            i += random.choice(mainList)
            j += 1
        return i
