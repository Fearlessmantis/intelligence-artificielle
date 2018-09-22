'''
Le probleme des N reines
(Solution par recursivite)
(Recherche en profondeur d'abord)
Realise par :
- HASSAN BOUMARSEL
'''
#variables globales:
N=8 #Nombre des reines
echiquier=[] #tableau NxN
pos_reine=[] #Les positions des N reines

#fonctions & procedures
'''
Precedure d'initialisation :
- On fixe la taille de l'echiquier (tableau NxN) et on l'initialise par 0
- On fixe la taille du tableau contenant les positions des N reines et on l'initialise par 0
'''
def init_echiquier():
    for i in range(0,N):
        pos_reine.append(0)
        li=[]
        for k in range(0,N):
            li.append(0)
        echiquier.append(li)

'''
Procedure d'affichage de toutes les solutions possibles 
'''
def affiche():
    for element in echiquier :
        print (element)
    print ("__________")     
'''
Procedure pour 'poser les reines' sur l'echiquier 
-On remplit toutes les cases vides de l'echiquier par 0, et les cases contenant les reines par 1 
-et on affiche le resultat
'''
def poser():
    for i in range(0,N):
        for k in range(0,N):
            echiquier[i][k]=0
    for i in range(0,N): 
        echiquier[i][pos_reine[i]]=1  
    affiche()
    
'''
Fonction de teste si la case est valide:
Si la case est valide on retourne 1 sinon on retourne 0
-Teste si la ligne est vide
-Teste si la reine n'est pas a la portee d'une autre reine en diagonale
-On pose les reines en se deplacant a droite sur l'echiquier suivant les colonnes,
    donc on ne fait pas de test sur les colonnes.
'''
def valide(li ,co): 
    for i in range(0,co):
        if pos_reine[i]==li or abs(pos_reine[i]-li)==abs(i-co):
            return 0 
    return 1 

'''
- Une fonction recursive qui fait une recherche en profondeur d'abord :
- continue a developper les resultats trouves en profondeur tant que valide est 'true', en se deplacant a droite suivant les colonnes.
- S'il n'est plus possible de poser une reine sur une nouvelle colonne, la fonction recule a la colonne precedante et change la position de la reine qui s'y trouve
'''
def cherche_solution(cur_col): 
    if(cur_col==N): #si on arrive a poser toutes les reines on affiche le resultat qui represente l'une des configurations possibles
        poser()      
    else :
        '''
        pour une colonne donne, on teste si l'une des ligne est valide pour y poser la reine,
        si aucune ligne n'est valide, on retourne a la colonne precedante et change la position de la reine qui s'y trouve
        '''
	for i in range(0,N): #la colonne est fixe, et on teste pour toutes les lignes
            if(valide(i,cur_col)): #teste si la case est valide
                pos_reine[cur_col]=i #si la case (colonne=cur_col, ligne = i) est valide on y pose une reine 
                cherche_solution(cur_col+1) #on passe a la colonne suivante

#debut programme :
leN=input("Donner Le nombre des reines : ")
N=leN
init_echiquier()
cherche_solution(0)  
