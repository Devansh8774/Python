import random 
jackpot = random.randint(1,100)
print("this is guessing game you have to guess the jackpo number ...the jackpot num lie b/w 1 to 100")
guess =int(input("chal guess kr="))
count =1

while guess !=jackpot:
    if count>8:
        break
    if guess<jackpot:
        print("guess the higher number")
    else:
        print ("guess the lower number")
    guess = int (input("chal fir se guess kar =")) 
    count =count +1
if count ==9:
    print("you took more than8 attempts so you lost")
else:
    print(f"sahi jawab you took {count}attempts")               


import random
jackpot = random.randint(1,100)
print("this is guessing game you have to guess the jackpot number ...the jackpot num lie b/w 1 to 100")
guess = int(input("chal guess kar = "))
count = 1
for i in range(8):
    if guess< jackpot:
       print("guess the higher number ")
    elif guess>jackpot:
       print("guess the lower number ")
    else:
       print(f"sahi jawab you took {count} attempts")
       break
    guess = int(input("chal firse guess kar = "))
    count = count+1
else:
       print("you lost the game took more than 8 attempts")

       print(" next line of code ")
 
 
 
import random
jackpot = random.randint(1,100)
print ("this is a guessing game you have to guess  the jackpot number the number lie between 1 to 100")
guess =int(input ("guess the number" ))
count =1
for i in range (8):
    if  guess>jackpot:
        print ("you guess the higher number")
    elif guess <jackpot:
        print("you guess the lower number") 
    else:
        print -(f"sahi jawab you took {count} attempts")
        break
    guess =int (input ("chalo fir se guess kro "))
    count =count+1
else:
    print ("you lost the game took more then 8 attempts ")
    
    print ("next line of code")



