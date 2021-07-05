import requests
import os
import get_user_info


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


url = "https://gist.githubusercontent.com/tempKDW/38c088036e5d12f1683b2d7d6a941ce6/raw/4afd2ffc19c063bc298e63da0908ffd60e045649/gistfile1.txt"
html = requests.get(url)
lst = html.text.split("\n")

user_info = []  # [['[id]','닉네임:스코어'], ...]
for i in lst:
    user_info.append(i.split(" ", 1))
del user_info[-1]

nick_score = []  # ['닉네임', '스코어'], ...]
for i in range(len(user_info)):
    nick_score.append(user_info[i][1].split(":"))


while True:
    print("1. id로 검색")
    print("2. score 높은 순서로 검색")
    print("3. score 낮은 순서로 검색")
    print("4. 모든 user 의 score 평균")
    input_menu = input(">")

    if input_menu == "1":
        print("= id 로 검색 =")
        try:
            user_id = input('찾을 id 입력 : ')
            if user_id == "":  # 엔터치면 메뉴로 돌아가기
                continue

            users = get_user_info.get_data(url, user_id)

            user = users.get(user_id)

            print(f'{user.nickname}\n{user.score}')
            break
        except AttributeError:
            print("잘못된 입력입니다.\n")

    elif input_menu == "2":
        print("= score 높은 순서로 검색 =")
        num = input("몇명? > ")

        score = []  # 스코어만 있는 리스트
        for i in lst:
            score.append(i.split(":")[-1])
        del score[-1]  # 왜 리스트 마지막에 ''가 있는건지 모르겠음... 삭제해주기

        score = list(map(str, sorted(list(map(int, score)), reverse=True)))[0:int(num)]  # 상위 num 개의 스코어
        high_rank = [" : ".join(nick_score[nick_score.index(j)]) for i in score for j in nick_score if i in j]
        inner = []
        result = []
        for i in high_rank[0:int(num)]:
            inner.append(i)
            if len(inner) == 5:
                result.append(inner)
                inner = []
        result.append(inner)

        for i in result:
            print()
            print("엔터를 치면 5명씩 표시합니다")
            input()
            os.system('cls')
            for j in i:
                print(j)

        print()
        print("출력 완료")

        #  엔터치면 메뉴로 돌아가기
        print()
        back_menu = input('엔터를 치면 메뉴로 돌아갑니다')
        if back_menu == "":
            print()
            continue

    elif input_menu == "3":
        print("= score 낮은 순서로 검색 =")
        num = input("몇명? > ")

        score = []  # 스코어만 있는 리스트
        for i in lst:
            score.append(i.split(":")[-1])
        del score[-1]

        score = list(map(str, sorted(list(map(int, score)))))[0:int(num)]  # 하위 10개의 스코어
        low_rank = [" : ".join(nick_score[nick_score.index(j)]) for i in score for j in nick_score if i in j]

        inner = []
        result = []
        for i in low_rank[0:int(num)]:
            inner.append(i)
            if len(inner) == 5:
                result.append(inner)
                inner = []
        result.append(inner)

        for i in result:
            print()
            print("엔터를 치면 5명씩 표시합니다")
            input()
            os.system('cls')
            for j in i:
                print(j)

        print()
        print("출력 완료")

        #  엔터치면 메뉴로 돌아가기
        print()
        back_menu = input('엔터를 치면 메뉴로 돌아갑니다')
        if back_menu == "":
            print()
            continue

    elif input_menu == "4":
        print("= 모든 user 의 score 평균 = ")
        score = []
        for i in lst:
            score.append(i.split(":")[-1])
        del score[-1]
        score = list(map(int, score))
        score_average = sum(score) / len(lst)
        print(round(score_average, 2))  # 소수점 셋째자리에서 반올림

        #  엔터치면 메뉴로 돌아가기
        print()
        back_menu = input('엔터를 치면 메뉴로 돌아갑니다')
        if back_menu == "":
            print()
            continue