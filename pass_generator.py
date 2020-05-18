import random
import time

print("PASSWORD GENERATOR 1.0.3 ")
passw = ["1","2","3","4","5","6","7","8","9","0"]

for i in range(32,127):
    passw.append(chr(i))

def pass_generator():
    
    us_input = int(input("Enter Number of characters :"))
    pass_gen = " "

                        

    for i in range(us_input):
        if us_input < 7:
            print("Password has to be greater than 7 characters for safety \n : )")
            break
        else:
            a = str(random.choice(passw))
            pass_gen += a
        

    print("Generating Password....")
    time.sleep(2)
    print("Your Password is : ",pass_gen)    
    print("\n")

    ans=input("Do you want to save our password remembering services ?")
    if ans == "yes" or ans == "Yes" or ans == "y":
        user_name = input('Enter name : ')
        user_service = input("Enter Service (Gmail etc.) : ")

        #Creating a file
        password = open("password.txt","x")
        password.close()

        password = open("password.txt","a")
        password.write(user_service)
        password.write(pass_gen)
        password.close()

pass_generator()
