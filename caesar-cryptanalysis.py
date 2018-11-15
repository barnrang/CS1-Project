import sys # Needed to access the arguments given in command line

def enc(k, plaintext):
    """Encode the given plaintext
        with Caesar cipher and shift key k.
        Change only lowercase characters,
        Keep other characters.
        Return the corresponding ciphertext.
        """
    
    #####################
    ### TO WRITE HERE ###
    #####################
    N = 26
    a_base = ord('a')
    z_base = ord('z')
    
    def shift(k, chr):
        '''
            shift small case char, ignore large case
            output: int
            '''
        intchr = ord(chr)
        return (intchr + k - a_base) % N + a_base if intchr >= a_base and intchr <= z_base else intchr
    
    intchr_list = [shift(k, x) for x in plaintext]
    
    plaintext = bytes(intchr_list).decode('ascii')
    
    return plaintext # To change here

def dec(k, ciphertext):
    """Decode the given ciphertext
        with Caesar cipher and shift key k.
        Change only lowercase characters,
        Keep other characters.
        Return the corresponding plaintext.
        """
    #####################
    ### TO WRITE HERE ###
    #####################
    N = 26
    a_base = ord('a')
    z_base = ord('z')
    
    def shift(k, chr):
        '''
            shift small case char, ignore large case
            output: int
            '''
        intchr = ord(chr)
        return (intchr - k - a_base) % N + a_base if intchr >= a_base and intchr <= z_base else intchr
    
    intchr_list = [shift(k, x) for x in ciphertext]
    
    ciphertext = bytes(intchr_list).decode('ascii')
    
    
    return ciphertext # To change here



####################
### MAIN PROGRAM ###
####################
# You do not need to modify anything below
# But (of course) you could/should try to understand it.

# To read arguments given in command lines
# sys.argv is an array (list) of arguments
# ex: typing "python caesar.py enc 3" gives the following
#     sys.argv = ["caesar.py", "enc", "3"]
# We can check the length of sys.argv to detect the commands
if len(sys.argv) > 1:
    command = sys.argv[1]
else:  # give a default value
    command = "dec"

# Read the input text, either the plaintext or the ciphertext
# sys.stdin is the STandarD INput: everything which is typed in the terminal
# it can be also given using the '<' symbol in command line
input_text = [ line.rstrip() for line in sys.stdin ]

# Execute the appropriate command
if command == "help":
    print("python caesar-cryptanalysis.py < <text>")
    print("  command: enc | dec")
    print("  key:     number between 0 and 25")

print(input_text)
