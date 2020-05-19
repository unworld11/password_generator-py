import random
import time
import sys

print("PASSWORD GENERATOR 1.0.4 ")
passw = ["1","2","3","4","5","6","7","8","9","0"]

for i in range(32,127):
    passw.append(chr(i))

def pass_generator():
    
    us_input = int(input("Enter Number of characters :"))
    pass_gen = ""

                        
    j=0
    while j in range(us_input):
        if us_input < 7:
            print("Password has to be greater than 7 characters for safety \n : )")
            break
            
            
            
        else:
            a = str(random.choice(passw))
            pass_gen += a
            j+=1
        

    print("Generating Password....")          

    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    
    print("\n")
    print("Your Password is : ",pass_gen)    
    print("\n")

    ans=input("Do you want to save our password remembering services ?")
    if ans == "yes" or ans == "Yes" or ans == "y":
        user_name = input('Enter name : ')
        user_service = input("Enter Service (Gmail etc.) : ")

        #Creating a file
        password = open("password.txt","x")

        password = open("password.txt","a")
        password.write(user_service)
        password.write(pass_gen)
        password.close()

pass_generator()
