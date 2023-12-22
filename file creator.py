import shutil
import os
import re
from datetime import datetime
files = os.listdir()

def find_max_number(files):
    max_number = 0
    posts =[]
    for file in files:
        if re.search("Post*", file):
            posts.append(file)
    for tittle in posts:
        x = tittle.replace("Post", "")
        y = x.replace(".html", "")
        if int(y)>int(max_number):
            max_number = y
    return max_number

number = int(find_max_number(files)) +1
source = r"Pattern.html"
target = r"Post" + str(number) +'.html'
shutil.copyfile(source, target)
x = datetime.fromtimestamp(os.stat("Post" + str(number) +'.html').st_ctime)
def CheckCreationDate(number):
    x = datetime.fromtimestamp(os.stat("Post" + str(number) +'.html').st_ctime)
    print(x)
    date = str(x).split()
    mainDate = date[0]
    return mainDate
print(CheckCreationDate(number))


with open("Post" + str(number) +'.html', "r") as f:
    contents = f.readlines()

contents.insert(38, '<p>  <!--start--> ' +CheckCreationDate(number)+' <!--start--> </p>')
contents.insert(0, '<!-- ' + str(x) + ' -->') 
print(x)
with open("Post" + str(number) +'.html', "w") as f: 
    contents = "".join(contents)
    f.write(contents)
