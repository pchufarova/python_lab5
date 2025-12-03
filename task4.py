import re

INPUT_PATH = "task_add.txt"


def find_dates(text):
    res = re.findall(r"(?<=\s)(?:(?:\d{2}(?:\.|/|-)){2}\d{4})"
                       r"|(?:\d{4}(?:(?:\.|/|-)\d{2}){2})", text)
    return res


def find_emails(text):
    res = re.findall(r"(?<=\s)\w+@[a-z-]+\.[a-z]+", text)
    return res


def find_websites(text):
    res = re.findall(r"(?<=\s)[a-z]+://[a-z-]+(?:\.[a-z-]+)+", text)
    return res


with open(INPUT_PATH) as file:
    dates = []
    emails = []
    websites = []
    for line in file:
        dates.extend(find_dates(line))
        emails.extend(find_emails(line))
        websites.extend(find_websites(line))

print(f"Спрятанные даты: {', '.join(dates)}")
print(f"Спрятанные почты: {', '.join(emails)}")
print(f"Спрятанные сайты: {', '.join(websites)}")
    