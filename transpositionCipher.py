def transEncrypt(plainText):
    evenChars = ''
    oddChars = ''
    index = 0
    
    for ch in plainText:
        if index % 2 == 0:
            evenChars += ch
        else:
            oddChars += ch
            
        index += 1
        
    cipherText = oddChars + evenChars
    return cipherText

def transDecrypt(cipherText):
    halfLength = len(cipherText) // 2
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]
    plainText = ''
    
    for i in range(halfLength):
        plainText += evenChars[i]
        plainText += oddChars[i]
        
    # See if there is one more even char
    if len(oddChars) < len(evenChars):
        plainText += evenChars[-1]
        
    return plainText

def main():
    message = input("Enter a message: ")
    enc = transEncrypt(message)
    print("Encrypted:", enc)
    dec = transDecrypt(enc)
    print("Decrypted:", dec)
    
main()