from datetime import *
from calendar import *
from math import *
from random import *
#10
nim=int(input("Sisesta minutites: "))
if nim>0:
    m=nim//60
    l=int((nim/60-m)*60)
    print(f"{m} tundi {l} minutit")
else:
    print('ploxo')
# #9
M=randint(1,1000)
M/=60
a=29.9
b=M*a
print(f"rulluisutaja keskmine kiirus: {a}; ja läbitus kaugus:{b} ")
#8
nan=float(input("Sisesta tangitud : "))
if nan<0:
    print('ploxo')
else:
    ot=float(input("Sisesta läbitud kilomeetrid: "))
    nana=(nan*100)/ot
    print(f"Kütusekulu 100km kohta keskmiselt: {round(nana,2)}")
#7
try:
    a=float(input("sisesta ristküliku lähiskülg a: "))
    b=float(input("sisesta ristküliku lähiskülg b: "))
    if a>0 and b>0:
        print("pindala ja umbermoodu arvutamine: ")
    else:
        print("arvud peavad olla suurem kui 0 ")
    Prist=2*(a+b)
    Srist=a*b
    print(f"ristküliku ümbermõõt on {Prist} ja pindala on {Srist}.")
except:
    print("valed andmed")
print()

#6
aa='''Rong see sõitis tsuhh tsuhh tsuhh
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?'''

bb='''Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.'''
print(aa, bb)

#5
k1="kill-koll ".capitalize()
k2="killadi-koll ".capitalize()
print(f"{k1*2}{k2}{k1*2}{k2}{k1*4}")
#4
maa=6378
d=2.575 #km
maa*=100000 #maa=maa*100000 sm
Lmaa=2*pi*maa
kogus=Lmaa/d
print(f"Meil on vaja {int(kogus):,d} munti")
print(f"Meil on vaja {int(kogus*2):,d} eur")


#3
try:
    num11=float(input('kirjuta sruudu '))
    sruudu=round((2*num11)**2,2)
    sringi=round(pi*num11**2,2)
    pruudu=round(8*num11,2)
    pringi=round(2*pi*num11,2)
    print(f'vastus on: struudu on {sruudu}, srtingi on {sringi}, pruudu on {pruudu}, pringi on {pringi}')
except:
    print('sisesta ujukomaarvud')

#2
from math import *
num1=int(3+8/(4 - 2)*4) #sulgudes 
print(f'sulgudes vastus on {num1}')
num2=int(3+8/4 - 2*4) #loeb ilma sulgudeta
print(f'loeb ilma sulgudetavastus on {num2}')
vastus3=(3 + 8) / (4 - 2) * 4
print(vastus3)

#1

tana=date.today()
print(f'tere! tana on {tana}')
tana1 = tana.strftime("%d/%m/%Y")
print(f'tere. tana on {tana1}')
# December 27, 2022
tana3 = tana.strftime("%B %d, %Y")
print(f'jaanuais on{tana3}paeva')

paevadekogus = monthrange(2025, 1)[1]
print(f'jaanuaris on {paevadekogus} paeva')
paevad = tana.day
onjj = paevadekogus - paevad
print(f'jaanuaris on jaaud {onjj} paeva')

aastaloop=365-mothrange(2025,1)[1]+onjj
print=(f'aasta lopuni on jaanus {aastaloop}')
# # 12/27/22
# tana = tana.strftime("%m/%d/%y")

# # Dec-27-2022
# tana = tana.strftime("%b-%d-%Y")
