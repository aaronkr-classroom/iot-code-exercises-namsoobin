# 3_dict.py
famous_ppl = {
        1: {
        "name": "Hank Aaron",
        "job": "baseball player",
        "age": "dead",
        "bithday": "1934/02/05",
        "died": "2021/01/22"
        },
        2: {
        "name": "이순신",
        "job": "장군",
        "age": "사망",
        "탄생": "1545/04/28",
        "died": "1598/12/16"
        }
    }

print(famous_ppl)
print(famous_ppl[2]['name'])#요소가 2개->앞에 키값 표시해야함.ex [2][name]
print(famous_ppl[2]['탄생'])