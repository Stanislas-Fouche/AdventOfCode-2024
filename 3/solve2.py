import re

def lecture_fichier(file):
    # Liste qui contiendra tous les résultats des multiplications
    resultats = []
    enabled = True  # Start with mul instructions enabled
    
    # Ouvrir et lire le fichier
    with open(file, 'r') as fichier:
        contenu = fichier.read()
        
        # Trouver toutes les instructions valides, y compris do() et don't()
        instructions = re.findall(r'do\(\)|don\'t\(\)|mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)', contenu)

        for instruction in instructions:
            if instruction == 'do()':
                enabled = True  # Enable future mul instructions
            elif instruction == "don't()":
                enabled = False  # Disable future mul instructions
            elif enabled and isinstance(instruction, tuple) and len(instruction) == 2:  # Check if mul instruction is enabled
                x, y = instruction
                if x and y:  # Vérifier que x et y ne sont pas vides
                    try:
                        resultat = int(x) * int(y)
                        resultats.append(resultat)
                    except ValueError:
                        pass  # Ignore if conversion fails

    return sum(resultats)

if __name__ == "__main__":
    # Lecture du fichier 
    total = lecture_fichier("3/input.txt")
    print(total)