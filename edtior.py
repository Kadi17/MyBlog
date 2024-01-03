import os
import re
import time
from datetime import datetime

files = os.listdir()
# print(files)
posts = []
postsDisctionary = {}
for file in files:
    if re.search("Post*", file):
        posts.append(file)
        
for nazwa_pliku in posts:
    with open(nazwa_pliku, 'r') as plik:
        pierwsza_linijka = plik.readline().strip()  # Odczytaj pierwszą linijkę
        print(pierwsza_linijka)
        x = pierwsza_linijka.replace("<!-- ", "")
        y = x.replace(' -->','')
        date = y.split('.')[0]
        postsDisctionary[date] = nazwa_pliku 
print(postsDisctionary)
ordered_postsDisctionary = sorted(postsDisctionary.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S'))
converted_dict = dict(ordered_postsDisctionary)
print(converted_dict)

# print(posts)
lines = []
linesToDelete =[]
# read file
with open(r"index.html", 'r') as fp:
    # read an store all lines into list
    lines = fp.readlines()
    for idx, line in enumerate(lines, start=1):
        print(line)
        if re.search("<!-- StartContent -->", line):
            linesToDelete.append(idx)
            print(idx)
        if re.search("<!-- EndContent -->", line):
            linesToDelete.append(idx)
            
# Write file
with open(r"index.html", 'w') as fp:
    # iterate each line
    for number, line in enumerate(lines):
        # delete line 5 and 8. or pass any Nth line you want to remove
        # note list index starts from 0
        if number not in range(linesToDelete[0], (linesToDelete[1]-1)):
            fp.write(line)


for post in converted_dict:
    evenN = 1
    f = open(converted_dict[post], "r")
    text = f.read()
    word = re.split(" ", text)
    # print(word)
    cardContent = ''
    tablica = []
    for message in word:
        if evenN % 2 == 0 and message != '<!--start-->':
            cardContent = cardContent + ' ' + message
        if message == '<!--start-->':
            evenN = evenN + 1
            if cardContent != '':
                tablica.append(cardContent)
            cardContent =''
    
    with open("index.html", "r") as f:
        contents = f.readlines()

    contents.insert(linesToDelete[0], '<div class="panel" class="blog_layouts_post_card blog_layouts_shadow"> <h3>'+ tablica[1] +'</h3> <p>'+ tablica[2] +'</p> <p class="zajawka">'+ tablica[0] +'</p><a href="'+converted_dict[post]+'"><button class="button">Read More</button></a></div>'+'\n')

    with open("index.html", "w") as f:
        contents = "".join(contents)
        f.write(contents)
    print(tablica)
