import random 

if True : 
    print( " La condition est vraie")
    print( " ce code est exécuté ")

if False : 
    print( " La condition est fause ")
    print( " ce code n'est pas  exécuté")

condition_vente = False 
if condition_vente : 
    print("L'utilisateur a accepté les condiions de vente ")
else :
    print("L'utilisateur n,a pas accepté les condiions de vente ")

if not condition_vente : 
    print("L'utilisateur n,a pas accepté les condiions de vente ")
else:
    print("L'utilisateur a accepté les condiions de vente ")


emails = random.randint(0,3 )

# elif c'est la même chose de else if 
if emails == 1 : 
    print("Vous avez un nouveau mails")

elif emails > 1: 
    print(f"Vous avez {emails} nouveaux mails ")

else : 
    print("Vous n'avez pas de  nouveau mails")


windows_closed = True 
electricity_off =  True

print(f"{windows_closed =} ")
print(f"{electricity_off =} ")


if windows_closed and electricity_off: 
    print( "les fenêtres sont fermées ")
    print("L'électricité est coupée")
    
elif not windows_closed and electricity_off:
    print( "les fenêtres ne sont pas fermées ")
    print("L'électricité est coupée")

elif windows_closed and electricity_off:
    print( "les fenêtres sont fermées ")
    print("L'électricité n'est pas coupée")

else :
    print( "les fenêtres ne sont pas fermées ")
    print("L'électricité n'est  pas coupée")

back_card= True 
cash =True 

print(f"{back_card= }")
print(f"{cash = }")


if back_card or cash : 
    print("On a un moyen de paiement ")

else : 
    print("On a aucun  moyen de paiement ")

ticket = True 
vip = False 
registration= False 
print(f"{ticket =}")
print(f"{vip =}")
print(f"{registration =}")

if (ticket or vip) and registration
     print("Access authorized ")

else : 
    print("Access not authorized ")

product_count = random.randin (0,50)

if 20 < product_count>20: 
    print(" Il y a plus de 20 articles ")
    print(" RAS")

elif  5 < product_count <= 20:
    print(" Il y a plus de 5 articles ")
    print(" Alerte approvisionnement  ")

elif  0 < product_count <= 5:
    print(" Il y a plus de 0 articles ")
    print(" Alerte rupture iminente")

else : 
    print(" Il y a plus d'articles ")
    print(" Alerte rupture ")

 product_count = 6 

# équivalent d'un encadrement python 

 if product_count >5 and product_count <= 20 
    print(" Il y a plus de 5 articles ")
    print(" Il y a 20 ou moins d'articles ")



 
 