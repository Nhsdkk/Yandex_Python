def solution():
    time_h, time_m, duration = int(input()), int(input()), int(input())
    new_time_h, new_time_m = (time_h + ((time_m + duration) // 60)) % 24, (time_m + duration) % 60

    new_time_h = "0" * (2 - len(str(new_time_h))) + str(new_time_h)
    new_time_m = "0" * (2 - len(str(new_time_m))) + str(new_time_m)

    print(f"{new_time_h}:{new_time_m}")


if __name__ == "__main__":
    solution()
