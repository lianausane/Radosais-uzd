print( )
a = "Uzdevums- Izveidot sarakstu kurā ir noteikts skaits skailū un šo skaitu ievada cilvēks, programma aprēkina videjo aritmētisko, nosaka cik ir pāra un nepāra  skaiļu, cik ir pozitīvi un cik negatīvi skaiļi, skaiļus sakotnējā saraktā saliek pēc kartas augošā secībā jaunā sarakstā  " 

print(a)
print( )
sk = []
n = -1
while n < 20 or n > 50:
    n = int(input("Cik skaitļu būs saraksta? (Ievadiet skaitli intervālā no 20 līdz 50.)"))
    if n < 20:
        print("šis skaitlis neder,jo ir mazākas par 20. Ievadi vēlreiz:")
    elif n > 50:
        print("šis skaitlis neder, jo ir lielāks par 50. Ievadi vēlreiz:")
import random
summa = 0
for i in range(n):
    a = random.randrange(-100, 100)
    summa += a
    sk.append(a)
print(sk)
print("Visu skaitļu suma ir ", summa)
print()
print("Vidējā aritmētiskā ir ", summa/n )
print()
m = min(sk)
l = max(sk)
print("Mazākā vertība sarakstā ir", m)
print("Lielākā vērtība sarakstā ir", l)
x=int(input("Ievadiet skaitli! kuru pievienosim izveidotajam sarakstas intervālā no -100 līdz 100:"))
sk.append(x)   

print("Jauniegūtais saraksts", sk)
sk.sort()
print("Izvadu sakartotu sarakstu augošā secībā", sk)

ne = []
pa = []
for num in sk:
    if num % 2 == 0:
        pa.append(num)
    else:
        ne.append(num,)    
print("Nepāra skaitļi ir šadi ", ne)
print()
print("Pāra skaitļi ir šadi ", pa)

 
       