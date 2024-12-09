def lecture_fichier(file):
    """
    Input: fichier texte (str) contenant des nombres entiers séparés par des espaces
    Output: liste de listes d'entiers
    Fonction qui lit le fichier et convertit chaque ligne en une liste d'entiers
    """
    liste = []
    
    fichier = open(file, 'r')
    for ligne in fichier:
        report=[]
        tmp = ligne.split()
        
        for val in tmp:
            report.append(int(val)) # On convertit en int 

        liste.append(report)
    return liste


def check(report):
    """
    Input: liste d'entiers (report)
    Output: booléen
    Vérifie si la liste respecte les conditions suivantes:
    - La différence entre deux nombres consécutifs doit être entre -3 et 3 (exclus)
    - La différence doit être soit toujours positive, soit toujours négative
    """
    i=1
    type_cache ="null"
    type=""

    while i < len(report):
        change = report[i-1] - report[i]

        if  change > 3 or change < -3 or change == 0 : # Les conditions de base
            return False
        
        if change < 0 :
            type = "negatif"  #Condition du type "increase or decrease"
        else : 
            type = "positif"
        
        
        if type != type_cache and type_cache != "null":
            return False
        
        type_cache = type

        i+=1 

    return True

def check2(report):
    """
    Input: liste d'entiers (report)
    Output: booléen
    Vérifie si en supprimant un élément de la liste,
    on peut obtenir une séquence valide selon les critères de check()
    """
    i=0
    for i in range(len(report)):
        copy = list(report)
        copy.pop(i)
        if check(copy) == True :
            return True
    return False
         


def solve(liste):
    """
    Input: liste de listes d'entiers
    Output: entier (compteur)
    Compte le nombre de séquences qui sont valides
    """
    compteur=0
    for report in liste:
        if check(report) == True: 
            compteur +=1
               
    return compteur
    

def solve2(liste):
    """
    Input: liste de listes d'entiers
    Output: entier (compteur)
    Compte le nombre de rapport qui sont valides soit directement,
    soit en retirant un élément
    """
    compteur=0
    for report in liste:
        if check(report) == True or check2(report)== True: 
            compteur +=1
               
    return compteur




if __name__ == "__main__":
    #Lecture du fichier 
    liste = lecture_fichier("input.txt")

    #Test parti 1 
    res = solve(liste)
    print(res)

    #Test parti 2 
    res2 = solve2(liste)
    print(res2)