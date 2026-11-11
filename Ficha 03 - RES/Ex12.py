
def palindrome(number):
    """ 
    """
    if number == number[::-1]:
        return True
    else:
        return False
    
    
    
number = input("Numero: ")

if number.isnumeric() == False or len(number) != 3:
    print("Invalid number")
    exit()
if palindrome(number):
    print("É Palindromo")
else:
    print("ÑÃO é  Palindromo")
    

