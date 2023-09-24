def solution():
    pet, vas, tol = int(input()), int(input()), int(input())
    if pet >= vas >= tol or pet >= tol >= vas:
        print("Петя")
    elif vas >= pet >= tol or vas >= tol >= pet:
        print("Вася")
    elif tol >= pet >= vas or tol >= vas >= pet:
        print("Толя")


if __name__ == "__main__":
    solution()
