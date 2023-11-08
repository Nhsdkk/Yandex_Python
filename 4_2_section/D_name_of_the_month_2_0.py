def month(index: int, lang: str = "ru"):
    dictionary = {
        1: ["Январь", "January"],
        2: ["Февраль", "February"],
        3: ["Март", "March"],
        4: ["Апрель", "April"],
        5: ["Май", "May"],
        6: ["Июнь", "June"],
        7: ["Июль", "July"],
        8: ["Август", "August"],
        9: ["Сентябрь", "September"],
        10: ["Октябрь", "October"],
        11: ["Ноябрь", "November"],
        12: ["Декабрь", "December"],
    }

    if lang == "en":
        return dictionary[index][1]
    else:
        return dictionary[index][0]