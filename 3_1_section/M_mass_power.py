def solution():
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    power = int(input())
    print("\n".join([f"{number ** power}"for number in numbers]))


if __name__ == "__main__":
    solution()
