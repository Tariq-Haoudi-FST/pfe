import requests
import bs4

type_of_news = ["أخبار-وطنية", "المغرب-العالمي", "regions", "politique", "صحة", "economie", "art-et-culture"]

for type_news in type_of_news:
    with open(f"{type_news}.txt", "w", encoding="utf-8") as file:
        for page_number in range(1, 201):  # Nous continuons jusqu'à la page 200 pour chaque type de news
            url = f"https://www.maroc24.com/ar/{type_news}/page/{page_number}/"
            goosread_website = requests.get(url)

            if goosread_website.status_code == 200:
                html = goosread_website.text
                html_parser = bs4.BeautifulSoup(html, "html.parser", from_encoding="utf-8")
                quotes = html_parser.findAll("div", attrs={"class": "post-content"})

                if not quotes:
                    break  # Si aucune nouvelle n'est trouvée, nous quittons la boucle

                file.write(f"---- {type_news} - Page {page_number} ----\n\n")

                for quote in quotes:
                    file.write(quote.text.strip() + "\n\n")

                print(f"Nombre de nouvelles récupérées de {type_news} - Page {page_number} : {len(quotes)}")
            else:
                print(f"Impossible d'accéder à la page {url}")
                break
