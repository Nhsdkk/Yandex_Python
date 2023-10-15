def solution():
    points = [input().split() for _ in range(int(input()))]
    possible_pairs = [f"{point[0][:-1]} {point[1][:-1]}" for point in points]
    counts = {pair: possible_pairs.count(pair) for pair in set(possible_pairs)}
    print(max(counts.values()))


if __name__ == "__main__":
    solution()
