{i: text.lower().count(i) for i in set("".join([char for char in text.lower()
                                                if char.isalpha()]))}