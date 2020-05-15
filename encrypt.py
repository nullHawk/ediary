# Copyrights to Suryansh Shakya

def encrypt(txt):
    new_txt  = ""
    for i in range(len(txt)):
        new_txt  = new_txt +chr(ord(txt[i]) + 300000)
    return(new_txt)

def decrypt(txt):
    new_txt = ""
    for i in range(len(txt)):
        new_txt = new_txt + chr(ord(txt[i]) - 300000)
    return(new_txt)


#for testing purpose
'''txt = input("Enter text to encrypt\n")
print(encrypt(txt))

txt = input("Enter text to decrypt\n")
print(decrypt(txt))'''