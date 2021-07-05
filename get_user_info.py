import requests
import re

url = "https://gist.githubusercontent.com/tempKDW/38c088036e5d12f1683b2d7d6a941ce6/raw/4afd2ffc19c063bc298e63da0908ffd60e045649/gistfile1.txt"


class User:
    def __init__(self, id, nickname, score):
        self.id = id
        self.nickname = nickname
        self.score = score
    id = ""
    nickname = ""
    score = 0


def get_data(url, user_id):
    html = requests.get(url)
    data = {}
    for row in html.text.split("\n"):
        if user_id not in row:
            continue
        user_id, nickname, score = re.match(r"\[(\w+)\]\s(.+):(\d+)", row).groups()
        data[user_id] = User(id=user_id, nickname=nickname, score=score)
    return data


if __name__ == "__main__":
    user_id = input('찾을 id 입력 : ')
    users = get_data(url, user_id)

    user = users.get(user_id)

    print(f'{user.nickname}\n{user.score}')
