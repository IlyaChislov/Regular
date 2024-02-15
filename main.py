# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
for i, contact in enumerate(contacts_list[1:]):
    names = (" ".join(contact[0:3]).strip()).split(" ")
    contacts_list[i + 1][0:3] = names
    text = contact[-2]
    if "доб" in text:
        pattern = r'(\+7|8)?\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})\s*\(*(доб.)*\s*(\d+)\)*'
        result = re.sub(pattern, r"+7(\2)\3-\4-\5 \6\7", text)
    else:
        pattern = r'(\+7|8)?\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})'
        result = re.sub(pattern, r"+7(\2)\3-\4-\5", text)
    contacts_list[i + 1][-2] = result

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
