import time
import random
import sys
import base64

# generate a 256 byte password that can use to do our encrypt
init_pass = bytearray(range(256))

# if the password is invalid
class invalidPass(Exception):
    '''throw the exception for invalid password'''

# generate a random password, make sure the same password will not appear closely
def genRanPass():
    password = init_pass.copy()
    random.shuffle(password)
    return password

# check if the password is 256 byte
def checkPassLen(password):
    if len(password) == 256:
        if len(set(password)) == 256:
            return True
        else:
            return False
    else:
        return False

# return the bytearray input string password
def inputPass(password):
    try:
        #encode the input string password first, with error handler is 'strict' as default
        encode_pass = password.encode('utf8')
        # decode the binary string using url and file system safe alphabets into normal form of strings
        password = base64.urlsafe_b64decode(encode_pass)
        # change it to bytearray form
        password = bytearray(password)
        # print (password)
    except:
        raise invalidPass

    if checkPassLen(password):
        #print (password)
        return password
    else:
        raise invalidPass
        
# dump the password
def savePass(password):
    # double check if the password is 256 byte or not
    if checkPassLen(password):
        # First we encode the string using url and file system safe alphabets into the binary form
        gen_pass = base64.urlsafe_b64encode(password)
        # then decode to get the password
        password = gen_pass.decode('utf8')
        # print (gen_pass)
        return password
    else:
        raise invalidPass

