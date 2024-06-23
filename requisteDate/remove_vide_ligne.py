import os

# Obtenir le chemin absolu du répertoire contenant le script Python
script_dir = os.path.dirname(os.path.abspath(__file__))

# Chemin complet du fichier texte
txt_file_path = os.path.join(script_dir, "economie.txt")

# Ouvrir le fichier texte en mode lecture
with open(txt_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Supprimer les lignes vides
filtered_lines = [line.strip() for line in lines if line.strip()]

# Réécrire le fichier texte avec les lignes filtrées
with open(txt_file_path, 'w', encoding='utf-8') as file:
    file.write('\n'.join(filtered_lines))

