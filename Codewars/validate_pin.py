# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# eg:

# validate_pin("1234") == True
# validate_pin("12345") == False
# validate_pin("a234") == False

def validate_pin(pin):
    print(len(pin))
    #return true or false
    if len(pin)!=4 and len(pin)!=6:
        return False
    return True
#Another
def validate_pin1(pin):
    return len(pin) in (4, 6) and pin.isdigit()
print(validate_pin('1234'))