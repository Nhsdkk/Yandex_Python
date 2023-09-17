def solution():
    n = int(input())
    players = []

    for _ in range(n):
        players.append(input())

    players.sort()
    print(players[0])


if __name__ == "__main__":
    solution()
