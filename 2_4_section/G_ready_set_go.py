def solution():
    participants_amount = int(input())

    start_delay = 3

    for participant_index in range(participants_amount):
        for i in range(start_delay + participant_index, 0, -1):
            print(f"До старта {i} секунд(ы)")
        print(f"Старт {participant_index + 1}!!!")


if __name__ == "__main__":
    solution()
