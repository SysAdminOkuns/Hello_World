myMessage = ""

def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def getMessage():
    stringToEncrypt = raw_input("Please enter a message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = raw_input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

def encryptMessage(message, cipherkey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherkey)
        if currentCharacter in alphabet:
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print('Alphabet: {}'.format(myAlphabet))
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print('Alphabet2: {}'.format(myAlphabet2))
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print('Encrypted Message: {}'.format(myEncryptedMessage))
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print('Decypted Message: {}'.format(myDecryptedMessage))




