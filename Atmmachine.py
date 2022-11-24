Account_2 = "Current"
Account_1 = "Saving" 
pin1 = 1234
Password = int(input("Enter The Password : "))
if pin1 != Password:
    print("Incorrect Password")
if pin1==Password:
    Account =  input ("Enter the Account Type:")
if pin1 == Password and Account_1 == Account:
    withdraw = int(input("Enter the Amount: "))
    print ( withdraw, " Amount has been detucted from your account." )
elif pin1== Password and Account_2 == Account:
    print("Your Account Type is wrong")
else :
    print("You are Not Authorized")
    
