import random
import time
passw = ["1","2","3","4","5","6","7","8","9","0"]

for i in range(32,127):
    passw.append(chr(i))
                
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
print(pass_gen)    
print("\n")
