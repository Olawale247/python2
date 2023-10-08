# breathe= int(input("enter first number:    "))
# length=int (input("enter second number:    "))
# breathe * 2 , length * 2
# result= breathe * 2 + length * 2
# print(result)

first_name=str(input("enter first name:    "))
last_name=str(input("enter second name: "))
email = str(input("Enter your email address:   "))
password= input("enter your password:   ")
combo = first_name + " "  + last_name + " " + email
special_character = str(['&', '$', '!','%' ,'1', '2', '3', '4', '5','6','7', '8','9', '10'])
if len(password) >= 8 and special_character in password:
    print(combo)
else:
    print("Your password is weak")
