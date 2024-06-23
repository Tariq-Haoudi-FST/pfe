import csv

type_of_news = ["أخبار-وطنية", "المغرب-العالمي", "regions", "politique", "صحة", "economie", "art-et-culture"]

for x in type_of_news:
    txt_filename = f"{x}.txt"
    csv_filename = f"{x}.csv"
    
    with open(txt_filename, "r", encoding="utf-8") as content, open(csv_filename, "w", encoding="utf-8", newline="") as csvfile:
        lines = content.readlines()
        writer = csv.writer(csvfile)
        writer.writerow(["Ligne précédente", "Date", "Heure"])  # Écrire l'en-tête du CSV
        
        for i in range(len(lines)):
            if "Maroc24" in lines[i]:
                # Vérifiez si ce n'est pas la première ligne et qu'il y a une ligne suivante
                if i > 0 and i + 1 < len(lines):
                    previous_line = lines[i - 1].strip()  # Supprimer les espaces blancs autour de la ligne précédente
                    next_line = lines[i + 1].strip()  # Supprimer les espaces blancs autour de la ligne suivante
                    
                    # Vérifier si la ligne suivante contient le séparateur " - "
                    if " - " in next_line:
                        # Formater la ligne avec la date et l'heure
                        date, time = next_line.split(" - ")
                        print(previous_line)
                        print(date)
                        print(time)  # Utilisation de print pour imprimer la variable time
                        writer.writerow([previous_line, date, time])  # Écrire les données dans le fichier CSV
                    else:
                        continue  # Ignorer cette itération et passer à la suivante


