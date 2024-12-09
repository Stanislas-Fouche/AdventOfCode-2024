

def lecture_fichier(file):

    liste = [[],[]]
    
    fichier = open(file,'r')
    
    for line in fichier:
        a,b=line.split()
        liste[0].append(a)
        liste[1].append(b)
    return liste

def solve(liste):
    res = 0

    liste1 = liste[0]
    liste2 = liste[1]
    
    i=0
    for i in range(len(liste1)):
        min1= min(liste1)
        min2= min(liste2)
        index1 = liste1.index(min1)
        index2 = liste2.index(min2)
        liste1.pop(index1)
        liste2.pop(index2)     
        i+=1
        
        diff = abs(int(min1) - int(min2))
        res = res + diff     
    return res 


def solve2 (liste): 
    res = 0
    
    liste1 = liste[0]
    liste2 = liste[1]

    for i in liste1:
        compteur = 0
        for j in liste2:
             if j==i:
                 compteur+=1
        res += int(i)*compteur

    return res


if __name__ == "__main__":
    liste = lecture_fichier("input.txt")
    res1 = solve(liste)
    liste2 = lecture_fichier("input.txt")
    res2 = solve2(liste2)
    print(res1)
    print(res2)

