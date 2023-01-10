#l'opération d'affection = permet d'injecter une valeur dans une variables 

#intéger, nomber entier 

my_number1 = 123
my_number2 = -42
my_number6 = .0
print(my_number1)
print(my_number2)
print(my_number6)
print(type(my_number1))

#float, nomber à virgule flotant 

my_number3 = 3.14
my_number4 = -2.71
#0.0 ou .0 ou 0.
my_number5 = 0.0
print(my_number3)
print(my_number4)
print(my_number5)
print(type(my_number5))

#bool , booléen 

my_boolean1 = True
my_boolean2 = False 
print(my_boolean1)
print(my_boolean2)
print(type(my_boolean1))

#None, valeur nulle
#null, nil

my_none = None 
print(my_none)
print(type(my_none))

#conversion explicite  en booléen 
# mais attention None ne peut être converti en int ou float  
print (bool(None))

#string, chaine de caractères 
#double quote ou sipmle quote, c'est pareil 

my_text1 ="Ceci est une chaine des caractères"
my_text2 = "Ceci est aussi une chaine de caractères "

print(my_text1)
print(my_text2)

# \ caractères d'échappement 
# \un saut de ligne 

my_text3 = "abc/ndef/nghi"
my_text4 = "\\"
my_text5 = "John \Foo \"Doe"
print(my_text3)
print(my_text4)
print(my_text5)
print(type(my_text1))

my_text6 = """abc
def\n
ghi"""

my_text7 = '''abc
def\n
ghi'''

print(my_text6)
print(my_text7)
print(type(my_text6))

foo = "Lorem ipsum"
# affectation de valeur à partir d'une variable
bar = foo
print(bar)

a = 123 
b = 42
#permutation de la valeur des variables 
a,b = b,a 
print(a, b)

a = 123 
b = 42 

#à vous de jouer 
c = a 
a = b
b = c
print (a, b)

#variante qui ne marche qu'avec des nombres 
c = a + b 
a = c - a 
b = c - b
print(a, b)

# transtypage == type casting == conversion d'un type de données

# 0 donne False et tous les autres donnent True
my_number7 = 0
# conversion explicite en booléen
print(bool(my_number7))

# conversion implicite en booléen
if my_number7:
    print("L'utilisateur a mis autre chose que zéro")
else:
    print("L'utilisateur a mis zéro")

# conversion explicite en booléen
my_text8 = '0'
print(bool(my_text8))

# conversion implicite en booléen
if my_text8:
    print("L'utilisateur a écrit quelque chose")
else:
    print("L'utilisateur n'a rien écrit")

# Listes 
fruits = [' ananas ','banane', 'cerise']
# opérateur d'inclusion 
result = 'ananas ' in fruits 
print (result)
result = 'fraise ' in fruits
print (result)

# conversion explicite en booléen 
result = bool (fruits )
print (result)



#str vers int 
foo = int(foo)
print (type(foo))

foo = "123"
#str vers flaot 
foo = float(foo)
print(type(foo))

foo = 3.14 
# flota vers int,permet de supprimer tout ce qui se trouve derrière la virgule 
foo = int(foo)
print(foo)

foo = 3.14 
# float vers str 
foo = str(foo)
print(type(foo))

#
foo = 2.71 
# récupérer la partie entière 
a = int (foo)
# récupérer la partie après les virgules (c-à-d 0.71)
b = foo - a
print (a)
print (b)

# conversion implicite en booléen
if fruits:
    print("la liste contient des éléments ")
else:
    print("la liste ne contient aucun des éléments")
