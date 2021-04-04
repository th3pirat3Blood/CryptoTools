import codecs
import sys

if len(sys.argv) !=2:
    print('USAGE: \t python script.py <encoded_text> ')
    exit(0)
else:
    print(sys.argv[1])
    dec=codecs.encode(sys.argv[1], 'rot_13')
    print(dec)
