# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
for i, contact in enumerate(contacts_list[1:]):
    names = (" ".join(contact[0:2])).strip().split(" ")
    if len(names) == 2:
        contacts_list[i + 1][0:2] = names
    else:
        contacts_list[i + 1][0:3] = names
    text = contact[-2]
    if "доб" in text:
        pattern = r'(\+7|8)?\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})\s*\(*(доб.)*\s*(\d+)\)*'
        result = re.sub(pattern, r"+7(\2)\3-\4-\5 \6\7", text)

    else:
        pattern = r'(\+7|8)?\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})'
        result = re.sub(pattern, r"+7(\2)\3-\4-\5", text)
    contacts_list[i + 1][-2] = result
# список фиксированной длины:
# 1 - Отчество, 2 - место работы, 3 - должность, 4 - телефон, 5 - эмэйл
del_list = []
for i, contact1 in enumerate(contacts_list[1:]):
    uniq_key = f"{contact1[0]} {contact1[1]}"
    dict_sravn = {uniq_key: contact1[0:]}
    for contact2 in contacts_list[i + 2:]:
        if uniq_key == f"{contact2[0]} {contact2[1]}":
            for num, elem in enumerate(dict_sravn[uniq_key]):
                if elem == "":
                    dict_sravn[uniq_key][num] = contact2[num]
            contact_result = dict_sravn[uniq_key]
            contacts_list[i + 1] = contact_result
            del_list.append(contact2)
for contact in del_list:
    contacts_list.remove(contact)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
