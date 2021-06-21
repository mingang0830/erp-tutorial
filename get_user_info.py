import requests


user_id = input('찾을 id 입력 : ')
url = "https://gist.githubusercontent.com/tempKDW/38c088036e5d12f1683b2d7d6a941ce6/raw/4afd2ffc19c063bc298e63da0908ffd60e045649/gistfile1.txt"
html = requests.get(url)
lst = html.text.split("\n")
search_id = []
for i in lst:
    if user_id in i:
        search_id.append(i)
user_info = search_id[0].split("] ")
del user_info[0]
name_score = "".join(user_info).split(":")
print(name_score[0])
print(name_score[1])



