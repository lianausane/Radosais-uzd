print( )
a = "Uzdevums- Izveidot sarakstu kurā ir noteikts skaits skailū un šo skaitu ievada cilvēks, programma aprēkina videjo aritmētisko, nosaka cik ir pāra un nepāra  skaiļu, cik ir pozitīvi un cik negatīvi skaiļi, skaiļus sakotnējā saraktā saliek pēc kartas augošā secībā jaunā sarakstā  " 

print(a)
print( )
sk = []
n = int(input("Cik skaitļu būs saraksta? (20-50 skaitļi) "))
import random

for i in range(n):
    sk.append(random.randrange(-100, 100))
print(sk)

x=int(input("Ievadiet skaitli! kuru pievienosim izveidotajam sarakstas intervālā no -100 līdz 100:"))
sk.append(x)   


"""
for num in sk:
    if num % 2 == 0:
        print(num)    
"""        