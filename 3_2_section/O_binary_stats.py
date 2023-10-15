def solution():
    result = [
        {
            "digits": len(bin(int(item))[2:]),
            "units": bin(int(item))[2:].count("1"),
            "zeros": bin(int(item))[2:].count("0"),
        } for item in input().split()
    ]

    print(result)


if __name__ == "__main__":
    solution()
