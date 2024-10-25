import json


def task(the_file) -> float:
    with open(the_file) as file:
        f = json.load(file)
    n = 0
    for i in f:
        n += i["score"] * i["weight"]
    return round(n, 3)


print(task("input.json"))
