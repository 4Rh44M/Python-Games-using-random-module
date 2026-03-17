import random
alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',']
password=""
alpha=int(input("Enter number of alphabets in ur password: "))
num=int(input("Enter number of numbers in ur password: "))
sy=int(input("Enter number of symbols in ur password: "))
for i in range(0,alpha):
    password+= alphabet[ random.randint(0,25)]
for i in range(0,num):
    password+= numbers[random.randint(0,8)]
for i in range(0,sy):
    password+=symbols[random.randint(0,11)]
password_list = list(password)
random.shuffle(password_list)
password = "".join(password_list)
print("Your password is: " + password)

    
    
