from json import load, dump


def solution():
    users, updates = input(), input()
    
    with open(users, "r") as file:
        json_users = load(file)

    with open(updates, "r") as file:
        json_updates = load(file)

    result = dict()

    for item in json_users:
        result[item["name"]] = {key: item[key] for key in item.keys() if key != "name"}

    for item in json_updates:
        if item["name"] not in result:
            continue

        for key in item.keys():
            if key == 'name':
                continue

            if key not in result[item["name"]]:
                result[item["name"]][key] = item[key]
                continue

            if result[item["name"]][key] < item[key]:
                result[item["name"]][key] = item[key]

    with open(users, 'w+') as f:
        dump(result, f, indent=2)


if __name__ == "__main__":
    solution()
