def count_words(contents):
    words = contents.split()
    return len(words)


def count_characters(contents):
    characters = {}

    for c in contents:
        c = c.lower()

        if c not in characters:
            characters[c] = 0
        characters[c] += 1

    return characters


def sort_characters_dict(dict):
    result = []

    for k in dict:
        if k.isalpha():
            result.append({"char": k, "num": dict[k]})
    result.sort(reverse=True, key=sort_on)
    return result


def sort_on(dict):
    return dict["num"]
