def check(pwd):
    uppercase = [ c for c in pwd if ord(c) in range(65, 91, 1) ]
    lowercase = [ c for c in pwd if ord(c) in range(97, 123, 1) ]
    numbers = [ c for c in pwd if ord(c) in range(48, 58, 1) ]
    #nonalphabet = [c for c in pwd if c in ".?!&#,;:-_*" ]
    if len(uppercase) == 0 or len(lowercase) == 0 or len(numbers) == 0:
        print("Bad password")
        return False
    else:
        print("Good password")
        return True



#Tests
check("Pass123")
check("password")
check("Password")
check("123")


def strength(pwd):
    upper = len([ c for c in pwd if ord(c) in range(65, 91, 1) ])
    lower = len([ c for c in pwd if ord(c) in range(97, 123, 1) ])
    numbers = len([ c for c in pwd if ord(c) in range(48, 58, 1) ])
    special = len(pwd) - upper - lower - numbers
    plen = len(pwd)
    if not check(pwd):
        return 0
    else:
        if upper > 2:
            upper = 2.5
        if lower > 2:
            lower = 2.5
        if numbers > 2:
            numbers = 2.5
        if special > 2:
            special = 2.5
        return upper + lower + numbers + special
    
            
print strength("jordan123")
print strength("Jordan123")
print strength("JoRdAn&*^*&!AS!(1238")
    

    
