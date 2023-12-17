import os
import re

files = os.listdir()
# print(files)
posts = []
for file in files:
    if re.search("Post*", file):
        posts.append(file)

# print(posts)

for post in posts:
    evenN = 1
    f = open(post, "r")
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
            tablica.append(cardContent)
            cardContent =''
    
    # index = open('test2.html', 'r+')
    # indexContent = index.read()
    # indexWords = re.split(" ", indexContent)
    # for message in indexWords:
    #     if evenN % 2 == 0 and message != '<!--content-->':
    #         print('widzę plik')
    #         index.write("Działa")
    #     if message == '<!--content-->':
    #         evenN = evenN + 1

    with open("test2.html", "r") as f:
        contents = f.readlines()

    contents.insert(9, '<div class="panel" class="blog_layouts_post_card blog_layouts_shadow"> <h3>'+ tablica[1] +'</h3> <p>12-12-2003 </p> <p class="zajawka">'+ tablica[3] +'</p><a href="Post.html"><button class="button">Read More</button></a></div>')

    with open("test2.html", "w") as f:
        contents = "".join(contents)
        f.write(contents)
    print(tablica)
