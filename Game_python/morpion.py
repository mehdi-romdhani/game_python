#Creation du jeu de morpion 

# Morpion partie avec deux jours 
# donc crée deux user 

#Demander si on souhait JOUER ou voir les SCORES

ask = input("Morpion : Pour jouer entrée : play  pour voir les scores entrée : score : ")

#variable pour jouer
j1=[]
j2=[]



#list pour la map du morpion 

tab1=["_","_","_"]
tab2=["_","_","_"]
tab3=["_","_","_"]

#conditions pour choisir play or score

if ask == "play":
     a = input("user 1 :")
     print(a)
     b = input("user 2 :")
     print(b)
     a = print(a+" joue contre "+b)
     print(tab1+"\n"+tab2+tab3)

     
elif ask == "score":
    print("votre score")  

