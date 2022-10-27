print('Hello World')
#comentariu pe o singura linie
''' comentariu 
pe mai multe linii
'''
#VARIABILE:
'''
O variabila este o adresa de memorie in care putem stoca anumite valori

*Conditii:
- nu poate sa inceapa cu o cifra 
- nu sunt permise spatii 
- sa aiba un nume unic
- daca are mai multe cuvinte trebuie separate prin underscore "_" sau sa inceapa al doilea cuvant cu litera mare 

Declararea reprezinta alocarea unui spatiu de memorie care este identificat de numele variabilei
Initializarea reprezinta stocarea unei valori initiale in spatiul de memorie alocat anteriorn 

'''
varsta = 15 # declararea si initializarea unei variabile
# print(f'Vane are varsta de  {varsta}  ani') # printare prin formatare a textului
# print('Vane are varsta de ' + varsta + ' ani') # printare prin concatenare de stringuri
#nu se poate face concatenare intre 2 tipuri de date adica str+int sau int+bool

# TIPURI DE DATE:
'''
 *O proprietate a unei adrese de memorie care descrie ce fel de valori pot fi stocate in acea adresa de memorie
    - string"str", intiger "int", boolean "bool",float {duble (nr cu zecimale) si cher (un singur caracter) in java}
 
 *In python tipul de date nu este declarat explicit si este dedus din valoarea care este salvata intr-o adtesa de memorie
    - ca o confecinta in python nu putem ave variabile declarate fara a fi initializate 
 '''
test = 3

# CONSTANTA:
'''
*O adresa de memorie in care putem stoca anumite valori care nu pot fi modificate ulterior
-In general numele constantelor ca si conventie sunt scrise cu litere mari
-In python conceptul de constanta nu este implementat asadar folosirea acestui concept ramane doar o conventie

'''

# FUNCTIA TYPE:

print(type(varsta))
nume = 'Vanessa'
print(type(nume))
cont_activ = True
valoare_abonament = 350.99
print(type(cont_activ))
print(type(valoare_abonament))

# TYPE CASTING:
'''
*Reprezinta modificarea unui tip de date asupra altei variabile
1.Casting explicit
2.Casting implicit
'''
# Casting Explicit
print(int(valoare_abonament))
print(type(str(valoare_abonament)))
print(int(cont_activ))
# print(int(nume)) # nu se poate sa modifici un str in int

# Casting Implicit
nr_1 = 30
nr_2 = 3.5
nr_3 = nr_1 + nr_2 # nr_1 se converteste automat

# USER INPUT:

#input('Introduceti varsta utilizatorului')
# user_furnizat = input('Introduceti utilizatorul')
# parola_furnizata = input('Introduceti parola')
# user_asteptat = 'Vanessa'
# parola_asteptata = '123'
# assert user_furnizat == user_asteptat
# assert parola_furnizata == parola_asteptata, 'Erroare, parola incorecta'

# STRING SLICING:
'''
  *Fiecare caracter dintr-un string este aflat la o pozitie identificabila de un index
-Primul caracter se afla la index-ul 0
-Putem sa extragem bucati dintr-un string folosind conceptul de slicing
-Slicing-ul se poate face folosind urmatoarea sintaxa
mystr[startpos, endpos, step]
  *Intotdeauna valoarea pt endpos nu este luata in considerare
By default startpos este 0 si endpos si step sunt 1

'''
prop = 'My name is python and I am a snake'
# prop[0] # am accesat primul caracterdin string aflat la pozitia 0
# print(prop[:]) #se iau in considerare si spatiile
# print(prop[0]) #printeaza caracterul din string cu indexul 0 adica M
# print(prop[0:3]) #printeaza primele 3 caractere de la index 0 la 2adica "my "
# print(prop[::-1]) # printeaza de la coada la cap tot stringul
# print(prop[-1])  # printeaza ultimul caracter din string
# print(prop[-3]) #printeaza al treilea caracter de la coada
# print(prop[0:10:2]) #printeaza de la indexul 0 la indexul 10 din 2 in 2 adica " M aei"
# print(len(prop)) # printeaza numarul de caractere din string
# print(prop[-5::]) #printeaza de la caracterul -5 pana la final
# print(prop[:8]) #ultimul caracter nu se i-a in considerare
# print(prop[::3]) # printeaza caracterele din 3 in 3

# METODE STRING
print(len(prop)) # Functia len este o functie pe care o folosim sa vedem cate caractere are stringul
print(prop.count('a')) # ne calculeaza de cate ori apare caracterul "a" in string
print(prop.upper()) # transforma stringul din litere mici in litere mari sau de tipar
print(prop.replace('i','y')) #inlocuieste caracterul "i" din string cu caracterul "y"


mystr = 'Azi e miercuri'
last_index = len(mystr)-1 # functia len numara caracterele dintr-un string, adaugam -1 deoarece indexul incepe de la 0
print(last_index) # verificam ultumul index
print(f'The last letter in \"{mystr}\" is \"{mystr[last_index]}\"')





