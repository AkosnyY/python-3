#heredoc string 


my_text1 = """Texte 
multi-ligne 
abc 
foo 
bar""" 

print("my_text1 ")

my_text2 = "Text/multi-ligne/nabc/nfoo/nbar"

print("my_text2")

my_number1 = 123
#interpolation avec une f-string
my_text3=f"Nombre = {my_number1}" 

#interpolation avec une heredoc string 

my_text4= f"""
Le nombre 
est 
{my_number1}
foo 
"""
print('my_text4')

#afficher des accoldes dans une heredoc f-string 
my_text5 = f""" 
{{
foo 
}}
{{bar}}
"""

print (my_text5)

my_number2 = "3.14"
my_text6 = " Le nombre PI est"+ str (my_number2) + "\nEt le nombre d'or et 1.618"
print(my_text6)


my_number3 = 1 / 3 
# tronquer un float dans une interpolation 
#4.f veut dire 4 chiffres aprés la virgule 
my_text7 = f"1 / 3 ~= {my_number3:.4f}"

print(my_text7)

#les interpolations acceptent les expressions 
my_text8 = f"1 + 1={ 1 + 1 }"
print(my_text8)

#défini= tion d'une fonction (fonction utilisateur )
#l'écriture de documentation pour une fonction 
def hello (name:str)-> None :  
    """Cette fonction dis bonjour a une personne 

    name str indique de la personne a saluer 
    return None 
    """
    print(f"Salut{name}")

# appel d'une fonction 
hello('Toto')

# affiche la doc d'une fonction 
#help(hello)

my_text9 = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae officiis facilis"
#longueur d'une str 
my_number4 = len(my_text9)
print(my_number4)

#trouve la postion dans une str dans une autre str 
my_number5=my_text9.find('dolor')
print(my_number5)

my_number5=my_text9.find('dolor'+my_number5+1)
print(my_number5)

#copte le nombre d'occurence d'uen str dans une autre str 
my_number6 = my_text9.count('ipsum')
print ( my_number6)

#remplacement non permanent 
print(my_text9.replace('Lorem,Foo '))
print(my_text9)

#remplacement permanent (il suffit d'écraser la variable avec sa nouvelle valeur )
my_text9= my_text9.replace('Lorem,Foo ')
print(my_text9)

#éclate une str en liste en utilisant l'espace comme caractère 

my_list1 = my_text9.split()
print(my_list1)
# la fonction len() peut être aussi utiliser avec des listes pour compter le nombre d'éléments 
print(len(my_list1)) 