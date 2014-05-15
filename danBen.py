from Tkinter import *

# Global Variables
dictionary = {"A": "Y", "B": "K", "C": "Q", "D": "W", "E": "X", "F": "P", "G": "L",
              "H": "A", "I": "B", "J": "M", "K": "T", "L": "F", "M": "U", "N": "V",
              "O": "H", "P": "O", "Q": "D", "R": "N", "S": "C", "T": "J", "U": "R",
              "V": "I", "W": "Z", "X": "E", "Y": "S", "Z": "G", " ": "@", "@": " "} #First Dictionary

dictionary2 = {"A": "Q", "B": "M", "C": "I", "D": "R", "E": "O", "F": "A", "G": "Z",
              "H": "@", "I": "P", "J": "Y", "K": "G", "L": "V", "M": "B", "N": "K",
              "O": "X", "P": "C", "Q": "U", "R": "W", "S": "J", "T": "F", "U": "E",
              "V": "D", "W": "N", "X": "S", "Y": "H", "Z": "L", "@": "T"}           #Second Dictionary

dictionary3 = {"1": "A", "2": "B", "3":""}



def enigma_encrypt(plaintext):       #First Encryption Scheme
    cipher = ''
    for index in range(len(plaintext)):
        cipher += dictionary[plaintext[index]]
    return cipher


def enigma_encrypt2(plaintext):       #First Encryption Scheme
    cipher = ''
    for index in range(len(plaintext)):
        cipher += dictionary2[plaintext[index]]
    return cipher

def caesar_encrypt(plaintext, key):
    cipher = ''
    for index in range(len(plaintext)):
        cipher += chr((ord(plaintext[index]) + key + 13) % 26 + 65)
        #print chr(ord(plaintext[index]) + key)
    return cipher

def enigma_decrypt(plaintext):
    cipher = ""


#Runs the plaintext through enigma encrypt, Caesar encryption scheme 1, engima encrypt 2, Caesar encryption
#scheme 2, enigma encrypt 2, and once more through enigma encrypt 1; slightly repetitive yet absurdly secure
def full_encrypt(plaintext, key1, key2):
    encrypt = enigma_encrypt(plaintext)
    print encrypt
    encrypt = caesar_encrypt(encrypt,key1)
    print encrypt
    encrypt = enigma_encrypt2(encrypt)
    print encrypt
    encrypt = caesar_encrypt(encrypt, key2)
    print encrypt
    encrypt = enigma_encrypt2(encrypt)
    print encrypt
    encrypt = enigma_encrypt(encrypt)
    print encrypt


def main():
    """
    Instantiates  a Tkinter frame.
    The frame will have 5 labels and 5 entries
    """
    frame = Tk()

    plaintext = Label( frame, text="Plaintext to Encrypt")
    E1 = Entry(frame, bd =5)

    label2 = Label( frame, text="Key 1")
    E2 = Entry(frame, bd =5)

    label3 = Label( frame, text="Key 2")
    E3 = Entry(frame, bd =5)


    #submit button calls an encryption method and encrypts
    #text in E1 widget



   # We now place each individual widget into the frame
    plaintext.pack()
    E1.pack()
    label2.pack()
    E2.pack()
    label3.pack()
    E3.pack()
    submit = Button( frame, text ="Submit", command= lambda: full_encrypt(E1.get(), int(E2.get()), int(E3.get())))
    submit.pack(side = BOTTOM)

    frame.mainloop()

if __name__ == "__main__":
    main()