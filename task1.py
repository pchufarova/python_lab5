import re 

INPUT_PATH = "task1-ru.txt"


def find_words(text):
    res = re.findall(r"[А-Яа-я]+е\b", text) #слова оканчивающиеся на е
    return res


def find_numbers(text):
    res = re.findall(r"\(\d+\)", text)
    return res


with open(INPUT_PATH, encoding="utf-8") as text:
    e_words = []
    numbers = []
    for line in text:
        e_words.extend(find_words(line))
        numbers.extend(find_numbers(line))
    print(e_words)
    print(numbers)