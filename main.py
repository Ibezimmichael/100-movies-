import requests
from bs4 import BeautifulSoup
import pandas

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


def get_web_page(url):
    format_text = requests.get(url).text
    food = BeautifulSoup(format_text, "html.parser")
    movies = [film.getText() for film in food.find_all(name="h3", class_="title")]
    return movies


response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
film_names = [film.getText() for film in soup.find_all(name="h3", class_="title")]
# film_names.reverse()
films = film_names[::-1]
print(films)
with open("new_movies.txt", mode='w', encoding="utf-8") as file:
    for film in films:
        file.write(f"{film}\n")




