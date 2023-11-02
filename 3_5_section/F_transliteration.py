def solution():
    dictionary = {
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "G",
        "Д": "D",
        "Е": "E",
        "Ё": "E",
        "Ж": "ZH",
        "З": "Z",
        "И": "I",
        "Й": "I",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "KH",
        "Ц": "TC",
        "Ч": "CH",
        "Ш": "SH",
        "Щ": "SHCH",
        "Ы": "Y",
        "Э": "E",
        "Ю": "IU",
        "Я": "IA",
    }

    with open("cyrillic.txt", "r", encoding="UTF-8") as file:
        data = file.readlines()

    data = [item.replace("ъ", "").replace("ь", "").replace("Ъ", "").replace("Ь", "")
            for item in data]

    new_lines = []

    for line in data:
        new_string = ""

        for char in line:
            if char.upper() not in dictionary:
                new_string += char
                continue

            if char.islower():
                new_string += dictionary[char.upper()].lower()
            else:
                new_string += dictionary[char].lower().capitalize()

        new_lines.append(new_string)

    with open("transliteration.txt", "w", encoding="UTF-8") as file:
        file.writelines(new_lines)


if __name__ == "__main__":
    solution()
