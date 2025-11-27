import re
import csv

INPUT_PATH = "task3.txt"
OUTPUT_PATH = "sorted_data.csv"
HEADERS = ["ID", "Surname", "Email", "Registration_date", "Website"]

def find_id(text):
    res = re.findall(r"(?<=\s)\d+(?=\s)", text)
    return res


def find_surname(text):
    return re.findall(r"\b[A-Z][a-z]+\b", text)


def find_emails(text):
    return re.findall(r"\w+@[a-z-]+\.[a-z]+", text)


def find_date(text):
    return re.findall(r"\d{4}-\d{2}-\d{2}", text)


def find_website(text):
    return re.findall(r"[a-z]+://[a-z-]+(?:\.[a-z-]+)+/", text) 


with open(INPUT_PATH) as text:
    line = text.readline()
    ids = list(map(lambda x: int(x), find_id(line)))
    surnames = find_surname(line)
    emails = find_emails(line)
    dates = find_date(line)
    websites = find_website(line)

sorted_data = [HEADERS]
for i in range(len(ids)):
    line = [ids[i], surnames[i], emails[i], dates[i], websites[i]]
    sorted_data.append(line)

with open(OUTPUT_PATH, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(sorted_data)
    


    
    
