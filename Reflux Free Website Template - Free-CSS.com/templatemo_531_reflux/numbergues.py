#guese a number
#genarate random number
#ask the user to guese anumber
#tell them is the are above or below the requred number
#ask the to type a number

import random
name=input('what is your name?')
rand=random.randint(0,10)
total_guese=0

while True:
    user=input(f'{name} please guease a number  ')
    if user.isdigit():
      if int(user) <= 0:
         print(" sorry! your guese is to small")
         quit()
      if int(user) != rand:
         print("your gues is wrong")
         continue
      else:
         
         print('your guese is correct. Good job')
         break
        
    else:
      print("your input should be in number form")
      continue
