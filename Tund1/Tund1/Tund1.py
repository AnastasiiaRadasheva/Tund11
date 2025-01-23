#8 ulesanne
print("    @..@")
print("   (----)")
print("  ( \__/ )")
print("   ^^ "" ^^  ")

#4 ulesanne
from math import *
puu_umbermoot= float(input("kirjuta puu umbermoot: "))
labimoot= math.sqrt(puu_umbermoot / pi)
print("puu läbimõõt on",labimoot , "meetrit.")

#5 ulesanne
from math import *
n=float(input("maatukki pikkus: "))
m=float(input("maatukki laius: "))
diagonaal=n**2+m**2
print("maatukki diagonaal on", diagonaal, "meetrit" )

#3
from random import *
kommid=randint(1,15)
print(F'kommid laual: {kommid}')
ykral=int(input('nii palju kui soovite ykrast?'))
ykradenie=kommid-ykral
print(f'ostalos konfet', ykradenie)
#1
print("Tere, maailm!")
nimi=input("kirjuta oma nimi: ")
print("Tere maailm!, Tervistan sind,")
vanus=int(input("kirjuta oma vanus: "))
print("Tere, maailm! tervitan sind", nimi ,"!","sa oled", vanus,"aastat vana.")
# #2
vanuss=18
eesnimi='jaak'
pikus=1.6
kas_kaib_koolis=True
print(type(vanuss))
print(type(eesnimi))
print(type(pikus))
print(type(kas_kaib_koolis))

# #6 ulesanne
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg
print("Sinu kiirus oli " + str(kiirus) + " km/h")


# #9 ulesanne
a=int(input(" kolmnurga külg a: "))
b=int(input(" kolmnurga külg b: "))
c=int(input(" kolmnurga külg c: "))
umbermoot=a+b+c
print("kolmnurga ümbermõõt on", umbermoot)

# #10 ulesanne
pitsa_hind=12.90
jootraha=0.10 * pitsa_hind

sobrad=int(input("kui palju inimest söövad pitsat?: "))
maksma= (pitsa_hind + jootraha) / sobrad
print("igauks peab maksma", maksma, "€")
#7
print("Sisesta 5 täisarvu:")
arv1 = int(input("Esimene arv: "))
arv2 = int(input("Teine arv: "))
arv3 = int(input("Kolmas arv: "))
arv4 = int(input("Neljas arv: "))
arv5 = int(input("Viies arv: "))
arvss=(arv1+arv2+arv3+arv4+arv5)´/5
print(arvss)
