#Game_python: "le pendu"
from pickle import TRUE
import random

#creative native function len()

def lenght(b):
    a = 0
    for i in b:
         a +=1

    return a

#source words from file

file = open("/home/meyze/Bureau/Game_python/dico_france.txt",encoding="ISO-8859-1")
doc = file.read()
#print(doc)

#add word in list

word = doc.split()
#print(word)
word_random = random.choice(word)
#print(word_random)


nb_lettre=len(word_random)
#print(nb_lettre)

#set a variable empty list for boucle
liste_vide=[]
letter_tape=[]


for x in word_random:
    liste_vide += "_"
#print(liste_vide)

word_list=list(word_random)
#print(word_list)

#set a variable 
end_game=True


#ask user choose level
level = input("Welcome player(s) : Choose ur level ? ( Entrez un level: debutant (vie:10), intermediaire (7) , expert (4) ): ")

while level !="debutant" and level !="intermediaire" and level !="expert":
        level = input("Choose your level : ")

#conditions pour choose level + vie
if level == "debutant":
    vie = 10 
elif level == "intermediaire" : 
    vie = 7
elif level == "expert" : 
    vie = 4

#Screen les lignes du mot at the begginin
print(' '.join(liste_vide)+"  pas de panique")

#boucle
while end_game: 
    
    
#choose ur letter 
    letter_choose=input("Choose a letter :  ")
    print("You choose the letter : " + letter_choose)
#affiche nombre de vie au start du jeu 
    print("Nombre de vie : ",vie)

#condition pour lui dire que la lettre est dans mon mot  
    if letter_choose in word_list:
#boucle qui parcours la liste ramdom pour implementer mon tableau vide 

        for i in range(nb_lettre):
        
            if  word_list[i]==letter_choose:
                liste_vide[i]=letter_choose
                letter_tape.append(letter_choose)
                print("les lettres ajouté",letter_tape)
                print(' '.join(liste_vide))

#conditions pour decrementer la vie                
    else :
#screen les lettres utiliser
        letter_tape.append(letter_choose)
        print("les lettres ajouté",letter_tape)
        vie -= 1
        print("Nombre de vie(s) restante(s)",vie)
        print(' '.join(liste_vide))


#conditions pour vie !            
    if vie == 0:
        end_game=False
        print("Vous avez perdue , retry ! , NULLLL")
        print("le mot est : ", word_random)

#conditions win
    if liste_vide == word_list:
        end_game = False
        print("You win handsome")
        print(":)")
    
    
        


  
            
  
    

      



  
   

































#condition pour choisir son niveau de jeu












