import sys
class colors:
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    CYAN = '\033[96m'


def gen_no(num):
    digit_start='1'
    num-=1
    start=pow(10,num)
    final=pow(10,num+1)
    for f in range(start,final,1):
        print(f)

if len(sys.argv) == 2:
    no_digits = sys.argv[1]
    gen_no(int(no_digits))
else:
    print(f"{colors.BOLD} This script generates all possible numbers based on number of digits")
    print(f"{colors.ENDC}",'USAGE:\t', f"{colors.CYAN}python3 <script.py> <no_of_digits>")
    exit(0)
