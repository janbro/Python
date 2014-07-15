a=0
def caesar(plaintext,shift):

    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",
    "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    #Create our substitution dictionary
    dic={}
    for i in range(0,len(alphabet)):
        dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]

    #Convert each letter of plaintext to the corresponding
    #encrypted letter in our dictionary creating the cryptext
    ciphertext=""
    for l in plaintext.lower():
        if l in dic:
            l=dic[l]
        ciphertext+=l

    return ciphertext

while(a == 0):
    answer=raw_input("Encode or decode:")

    if answer.lower()==u'encode':
        shift = int(raw_input("Input shift:"))
        plaintext=raw_input("Input words to encode:")
        print "Plaintext:", plaintext
        print "Ciphertext:",caesar(plaintext,shift)
        a=1
        break
    if answer.lower()==u'decode':
        shift = int(raw_input("Input shift:"))
        plaintext=raw_input("Input words to decode:")
        print "Ciphertext:", plaintext
        print "Plaintext:", caesar(plaintext,shift)
        a=1
        break
    else:
        print "That is not a valid answer."


