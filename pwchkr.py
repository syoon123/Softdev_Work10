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

def check2(pwd):
    
