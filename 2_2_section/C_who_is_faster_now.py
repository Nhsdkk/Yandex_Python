def solution():
    pet, van, tol = int(input()), int(input()), int(input())
    maximum = max(pet, van, tol)
    if maximum == pet:
        print("Петя")
    elif maximum == van:
        print("Вася")
    elif maximum == tol:
        print("Толя")


if __name__ == "__main__":
    solution()
