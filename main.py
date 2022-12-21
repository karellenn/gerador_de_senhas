import random
from time import sleep

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWYZ"
num="1234567890"
symb="_-./@!?"

all= lower+upper+num+symb

print(" Bem-Vindo ao Gerador de Senhas ")
print("")
print("")

a= int( input("por favor informe a quantidade de caracteres para sua senha: "))
print("")
print("")


print ("A quantidade de caracteres escolhida foi:",a)
length=a
psw= "".join(random.sample(all, length))
print("")
print("")
print("#"*60)
print("")
print("")
print("sua senha e:", psw)
print("")
print("")
print("#"*60)
print("")
print("")
sleep(5)
print ("Obrigado por usar o sistema de gerar senhas ")