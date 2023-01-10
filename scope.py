# scope ou la portée de variables
# le scope fonctionne exactement pareil en js 

# foo = 123 # scope global ( n'est ni dans un if ou une liste, elle n'est pas entourer)

def  bar (): 
    foo = 42 # scope local 
    print(foo)

print(foo) # 123 # scope global
bar() # 42,  scope local de la fonction bar()
print(foo) # 123

def baz():
    print('baz',foo) # scope global 
    lorem = 'ipsum'

baz() # 123 , scope global 
#print(lorem) #l'appel est dans le scope mais la variables lorem est dans un scope local 