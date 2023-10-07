def solution():
    numbers = [int(number) for number in input().split(" ")]
    power = int(input())
    print(" ".join([f"{number ** power}"for number in numbers]))


if __name__ == "__main__":
    solution()
