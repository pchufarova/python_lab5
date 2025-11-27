import re

INPUT_PATH = "task2.html"

def get_im_sizes(text):
    res = re.findall("\d+x\d+", text)
    return res


with open(INPUT_PATH, encoding="utf-8") as text:
    sizes = []
    for line in text:
        size = get_im_sizes(line)
        sizes.extend(size)
    print(sizes)