import requests
import matplotlib.pyplot as plt
import numpy as np


#  Counts how many times a category (ex. “Action”) appears in a given string (the url’s script) and returns that number.
def cntWord(word, s):
    N = len(word)
    cnt = 0
    for i in range(len(s) - N):
        if word == s[i:i+N]:
            cnt += 1
    return cnt


#  Input for the user to insert the site's url.
#  Try top 2019 movies from Imdb: https://www.imdb.com/best-of/highest-rated-movies-of-2019/ls091392448/
#  Try top 2020 movies from Imdb: https://www.imdb.com/best-of/col-needham-2020-movies-rated-9-and-up/ls082776990/
url = input("Please enter a url of a website that you want to gain statistics:")

#  Contains the most common movie-categories and their frequencies on the given site.
Genre = {"drama": 0, "comedy": 0, "sci-fi": 0, "biography": 0,
         "adventure": 0, "romance": 0, "action": 0, "fantasy": 0,
         "crime": 0, "thriller": 0, "horror": 0, "animation": 0}

#  The site’s script with lowercase letters.
myF = requests.get(url)
Data = myF.text.lower()
#  For every movie-category, it counts their total number of appearances on the site.
for cat in Genre:
    cnt = cntWord(cat, Data)
    Genre[cat] = cnt

#  Creating the x and y coordinates of the bar graph.
x = np.array(list(Genre.keys()))
y = np.array(list(Genre.values()))
plt.subplot(2, 1, 1)
plt.title("Best movies' genres and their frequencies")
plt.xlabel("Genres")
plt.ylabel("Frequencies")
plt.bar(x, y)
#  Creating the pie chart.
plt.subplot(2, 1, 2)
plt.pie(y, labels=Genre.keys())
#  Print graphs
plt.show()
#  ---End of Code---
