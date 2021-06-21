import requests

url = "https://gist.githubusercontent.com/tempKDW/38c088036e5d12f1683b2d7d6a941ce6/raw/4afd2ffc19c063bc298e63da0908ffd60e045649/gistfile1.txt"
html = requests.get(url)
lst = html.text.split("\n")

while True:
    print("1. id로 검색")
    print("2. score 높은 10명")
    print("3. score 낮은 10명")
    print("4. 모든 user 의 score 평균")
    input_menu = input(">")

    if input_menu == "1":
        print("= id 로 검색 =")
        input_user_id = input('찾을 id 입력 : ')
        if input_user_id == "":  # 엔터치면 메뉴로 돌아가기
            continue
        else:
            search_id = []
            for i in lst:
                if input_user_id in i:
                    search_id.append(i)
            user_info = search_id[0].split(" ", 1)
            del user_info[0]
            nickname_score = "".join(user_info).split(":")
            print(nickname_score[0])
            print(nickname_score[1])
            break

    elif input_menu == "2":
        print("= score 높은 10명 =")
        user_info = []  # [['[id]','닉네임:스코어'], ...]
        for i in range(len(lst)):
            user_info.append(lst[i].split(" ", 1))
        del user_info[-1]

        nick_score = []  # ['닉네임', '스코어'], ...]
        for i in range(len(user_info)):
            nick_score.append(user_info[i][1].split(":"))

        score = []
        for i in lst:
            score.append(i.split(":")[-1])
        del score[-1]
        score = list(map(str, sorted(list(map(int, score)), reverse=True)))[0:10]  # 상위 10개의 스코어
        high_rank = [nick_score[nick_score.index(j)] for i in score for j in nick_score if i in j]

        for i in high_rank[0:10]:
            print("%s : %s" % (high_rank[high_rank.index(i)][0], high_rank[high_rank.index(i)][1]))

        #  엔터치면 메뉴로 돌아가기
        back_menu = input()
        if input_menu == "":
            continue

    elif input_menu == "3":
        print("= score 낮은 10명 =")
        user_info = []  # [['[id]','닉네임:스코어'], ...]
        for i in range(len(lst)):
            user_info.append(lst[i].split(" ", 1))
        del user_info[-1]

        nick_score = []  # ['닉네임', '스코어'], ...]
        for i in range(len(user_info)):
            nick_score.append(user_info[i][1].split(":"))

        score = []
        for i in lst:
            score.append(i.split(":")[-1])
        del score[-1]
        score = list(map(str, sorted(list(map(int, score)))))[0:10]  # 하위 10개의 스코어

        low_rank = [nick_score[nick_score.index(j)] for i in score for j in nick_score if i in j]
        for i in low_rank[0:10]:
            print("%s : %s" % (low_rank[low_rank.index(i)][0], low_rank[low_rank.index(i)][1]))

        #  엔터치면 메뉴로 돌아가기
        back_menu = input()
        if input_menu == "":
            continue

    elif input_menu == "4":
        print("= 모든 user 의 score 평균 = ")
        score = []  # 스코어만 있는 리스트
        for i in lst:
            score.append(i.split(":")[-1])
        del score[-1]  # 왜 리스트 마지막에 ''가 있는건지 모르겠음... 삭제해주기
        score = list(map(int, score))
        score_average = sum(score) / len(lst)
        print(round(score_average, 2))  # 소수점 셋째자리에서 반올림

        #  엔터치면 메뉴로 돌아가기
        back_menu = input()
        if input_menu == "":
            continue


