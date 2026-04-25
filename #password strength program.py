#password strength program
#prompt user for a password
#evaluate password strength
#password != requirements --> prompt user for a password until it meets criteria
#password requirements --> 1 upper/1 lower/1 number/ 1 special character
def pwordCHECK(pword): #define a function
    if len(pword) >= 12: #check the length of password
        print("Password passes the minimum length requirements! ")
    else:
        print("Password does not meet character length minimum! ")
    upperEval = False  #upper case evaluation set to False
    for char in pword: #for loop which iterates through the password for an uppercase character
        if char.isupper(): #if that character is uppercase change the uppercase evaluation variable to True
            upperEval = True
    if upperEval == True: #if true, print the following, else, print the following
        print("At least one upper case character detected! ")
    else:
        print("Password requires at least one upper case character! ")
    lowerEval = False #lower case evaluation set to False
    for char in pword: #for loop which iterates through the password for a lowercase character
        if char.islower(): #if that character is lowercase change the lowercase evaluation variable to True
            lowerEval = True
    if lowerEval == True: #if true, print the following, else, print the following
        print("At least one lower case character detected! ")
    else:
        print("Password requires at least one lower case character! ")
    numEval = False #number evaluation set to False
    for num in pword: #for loop which iterates through the password for a number
        if num.isdigit(): #if a number is present change the number variable to true
            numEval = True
    if numEval == True: #if true, print the following, else, print the following
        print("At least one number has been detected! ")
    else:
        print("Password requires at least one number! ")
    specChar = False #special character evaluation set to False
    for special in pword: #for loop which iterates through the password for a special number
        if not special.isalnum(): #if there is a character that is NOT an alphanumeric character has been detected, change special character evaluation to True
            specChar = True
    if specChar == True: #if true, print the following, else, print the following
        print("At least one special character detected! ")
    else:
        print("Password requires at least one special character! ")
    
    pwordValid = True #password valid variable set to True
    if upperEval == False: #if this variable is false, change the valid password variable to false
        pwordValid = False
    if lowerEval == False:
        pwordValid = False
    if numEval == False:
        pwordValid = False
    if specChar == False:
        pwordValid =False
    if len(pword) < 12:
        pwordValid = False
    
    if pwordValid: #if the password valid variable is true, print the following
        print("Your password meets all security requirements! ")
    if pwordValid == False: #if the password valid variable is false, print the following
        print("Your password does not meet all requirements!\n"
              "Please try again! ")

    return(pwordValid) #return the value of password valid variable

pwordSTORE = [] #create a list to store passwords inside

while True: #while loop that runs continuously 
    pword = input("Please enter in a new password: ") #prompt user for a password
    pwordSTORE.append(pword) #append the password to the list
    if pwordCHECK(pword) == True: #call the function and check if the password valid variable returns True
        print("Your password is set! ") #print the following if True
        break
    else:
        print("Your password is not set yet!\n" #print the following if False
              "See which requirements you are still missing! ")
        

    





