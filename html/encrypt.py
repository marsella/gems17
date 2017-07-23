# encrypts with a caesar cipher. 
# optional command-line key argument

import sys


numargs = len(sys.argv) 
if numargs == 2:
    message = sys.argv[1].upper()
    key = 'K'
elif numargs == 3:
    message = sys.argv[1].upper()
    key = sys.argv[2].upper()[0]
else:
    print '''usage: python encrypt.py <message> <key>
             where key is optional'''
    exit()

key = ord(key) - ord('A')

cipher = [chr((ord(l) + key - ord('A'))%26 + ord('A'))
            if l.isalpha() else l
            for l in message]
print ''.join(cipher)
