def solution():
    str1, str2, str3 = input(), input(), input()

    min_str, max_str = min(str1, str2, str3), max(str1, str2, str3)

    if (min_str == str1 and max_str == str2) or (min_str == str2 and max_str == str1):
        sr = str3
    elif (min_str == str1 and max_str == str3) or (min_str == str3 and max_str == str1):
        sr = str2
    else:
        sr = str1

    if "зайка" in min_str:
        print(min_str, len(min_str))
    elif "зайка" in sr:
        print(sr, len(sr))
    else:
        print(max_str, len(max_str))


if __name__ == "__main__":
    solution()
