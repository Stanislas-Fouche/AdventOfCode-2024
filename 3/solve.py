import re

def lecture_fichier(file):
    # Liste qui contiendra tous les résultats des multiplications
    res = []
    
    # Ouvrir et lire le fichier
    with open(file, 'r') as fichier:
        contenu = fichier.read()
        
        # Trouver toutes les instructions mul(X,Y) valides
        instructions = re.findall(r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)', contenu)
        
        # Calcul des multiplications
        for x, y in instructions:
            resultat = int(x) * int(y)
            res.append(resultat)

    return sum(res)

if __name__ == "__main__":
    # Lecture du fichier 
    total = lecture_fichier("3/input.txt")
    print(total)