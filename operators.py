import random 
import math

# = affectaction 
foo = 123

# + addition 
foo = 123 + 42 
foo = foo + 42
# += opérateur d'incrémentation 
foo += 42
print(foo)

#foo++ équivalent de foo + = 1
#mais l'opérateur n'existe pas en python 

# - soustraction 
foo = 123 - 42
foo = foo -42

# -= opérateur de décrémentation
#foo-- équivalent de foo - = 1
#mais l'opérateur n'existe pas en python 

foo = -42 
print(foo)

# / division 
foo = 123 / 42
foo /= 42
print(foo)
print(type(foo))


# // division entières 
foo = 123// 42
foo = foo // 42
foo //= 42
print(foo)
print(type(foo))

# % modulo 
foo = 4 % 3
foo = random.randint(1,100)
print(foo)
print(foo % 2 )

# * multiplication 
# ** puissance 
foo = 2** 2
foo = 2** 3
foo = 2** 4
foo = 2** 5
foo = 2** 6
foo = 2** 7
print(foo)


# ^ puissance mais pas en python 
# sqrt () racine carré 
# ** 0.5 racine carré 
foo = math.sqrt(4)
foo = 4 ** 0.5 
#0.5 == 1/2 
foo = 4 ** (1/2)
# racine cubique 
foo = 8 ** (1/3)
print (foo)

# les opérateurs de comparaison 

# l'égalité == 
#à ne pas confondre avec l'affectation 
#à ne pas confondre avec l'dentité === (qui n'existe pas en python) 
result = 1 == 1 
print(result)

# les grandeurs
# plus petit que
result = 123 < 42
print(result)

# plus petit ou égal à
# à ne pas confondre avec => js
result = 123 <= 42
print(result)

# plus grand que
result = 123 > 42
print(result)

# plus grand ou égal à
result = 123 >= 42
print(result)

# l'inégalité 
result = 123 != 42 
print (result)
# les encadrements avec  <  > <= >= 
my_number = random.randint(0,100)
result = 0 <= my_number <= 50 
print(result)
result = 50 < my_number <= 100 
print(result)

# l'opérateur and ( et )
result =  True  and False # False 
print(result)
result =  False and True # False
print(result)
result =  True  and True # True 
print(result)
result =  False  and False # False 
print(result)

a = random.randint(0, 1 )
b = random.randint(0, 1 )
result =  a and b
result = (a, b)
print(result)

# l'opérateur or (ou )
result =  True  or False # True  
print(result)
result =  False or True # True 
print(result)
result =  True  or True # True 
print(result)
result =  False  or False # False 
print(result)

#opérateur not (négation) 
result = not True
print(result)
result = not False 
print(result)

# on peut utiliser d'autres type de données que l'or converti en booléen avec les opérateurs booléens 
a = random.randint(0, 1 )
b = random.randint(0, 1 )
result = a or b 
result = (a, b)
print(result)


#utilisation un peu "spéciales " des comparaisons de grandeur 
result = "abc"< "bcd"
result = 97098099 < 98099100
print(result)

result = "A"< "a"
print(result)

fruits = ['abricot', 'baie', 'cerise']
result = 'ananas' in fruits
print(result)
result = 'cerise' in fruits
print(result)