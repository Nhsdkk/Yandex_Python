def solution():
    people = {}

    while prompt := input():
        splitted_prompt = prompt.split()
        if splitted_prompt[0] in people:
            people[splitted_prompt[0]].append(splitted_prompt[1])
        else:
            people[splitted_prompt[0]] = [splitted_prompt[1]]

        if splitted_prompt[1] in people:
            people[splitted_prompt[1]].append(splitted_prompt[0])
        else:
            people[splitted_prompt[1]] = [splitted_prompt[0]]

    second_level = {}

    for person in people.keys():
        second_level_friends = set()

        for friend in people[person]:
            second_level_friends.update(people[friend])
            if person in second_level_friends:
                second_level_friends.discard(person)

        for friend in people[person]:
            if friend in second_level_friends:
                second_level_friends.discard(friend)

        second_level[person] = sorted(second_level_friends)

    print("\n".join([f"{person_name}: {', '.join(second_level[person_name])}"
                     for person_name in sorted(second_level.keys())]))


if __name__ == "__main__":
    solution()
