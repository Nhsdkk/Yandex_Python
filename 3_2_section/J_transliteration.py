def solution():
    chars = {
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
        "Ъ": "",
        "Ь": "",
    }

    string = ""

    for char in input():
        if char.upper() in chars:
            if char.isupper():
                string += chars[char.upper()].lower().capitalize()
            else:
                string += chars[char.upper()].lower()
        else:
            string += char

    print(string)


if __name__ == "__main__":
    solution()
