print( )
a = "Uzdevums- Izveidot sarakstu kurā ir noteikts skaits skailū un šo skaitu ievada cilvēks, programma aprēkina videjo aritmētisko, nosaka cik ir pāra un nepāra  skaiļu, cik ir pozitīvi un cik negatīvi skaiļi, skaiļus sakotnējā saraktā saliek pēc kartas augošā secībā jaunā sarakstā  " 

print(a)
print( )
sk = []
while n < 20 or n > 50:
    n = int(input("Cik skaitļu būs saraksta? (Ievadiet skaitli intervālā no 20 līdz 50.)"))
    if n < 20:
        print("šis skaitlis neder,jo ir mazākas par 20. Ievadi vēlreiz:")
    elif n > 50:
        print("šis skaitlis neder, jo ir lielāks par 50. Ievadi vēlreiz:")
import random

for i in range(n):
    sk.append(random.randrange(-100, 100))
print(sk)


x=int(input("Ievadiet skaitli! kuru pievienosim izveidotajam sarakstas intervālā no -100 līdz 100:"))
sk.append(x)   

print(sk)

for num in sk:
    if num % 2 == 0:
        print(num)


for num in sk:
    if num % 2 == 0:
        print(num)    
       