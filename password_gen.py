import random


c = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
n='0123456789'
s='!@#$%()*+'

pwd = ''
print("-----------------------------------------------------")
a=int(input("ENTER NUMBER OF ALPHABETS:"))
b=int(input("ENTER NUMBER OF NUMBERS:"))
d=int(input("ENTER NUMBER OF SYMBOLS:"))
print("-----------------------------------------------------")

for i in range(0,a):
    pwd += random.choice(c)
for j in range(0,b):
    pwd+=random.choice(n)
for j in range(0,d):
    pwd+=random.choice(s)
pwd_list = list(pwd)
random.shuffle(pwd_list)
password = ''.join(pwd_list)
print("PASSWORD: ",password)

print("-----------------------------------------------------")



