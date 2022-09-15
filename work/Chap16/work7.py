import json
menu = \
    {
    "breakfast" : {
        "hours" : "7-11",
        "items" : {
            "breakfast burritos" : "$6.00",
            "pancakes" : "$4.00"
        }
    },
    "lunch" : {
        "hours" : "11-3",
        "items" : {
            "hamburger" : "$5.00"
        }
    },
    "dinner" : {
        "hours" : "3-10",
        "items" : {
            "spaghetti" : "$8.00"
        }
    }
}

menu_json = json.dumps(menu) # dumps : 자료구조를 JSON 문자열로 인코딩
print(menu_json)

menu2 = json.loads(menu_json) # loads : JSON 문자열을 자료구조로 디코딩
print(menu2)