import os
import re
import csv

file_path = os.path.join(os.getcwd(),"phonebook_raw.csv")

def read_file(file_path):
	with open(file_path, encoding='utf-8') as f:
		rows = csv.reader(f)
		contacts_list = list(rows)
		return contacts_list


def format_full_name(contacts_list):
    name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    name_pattern_new = r'\1\3\10\4\6\9\7\8'
    contacts_list_updated = []
    for rows in contacts_list:
        rows_as_string = ','.join(rows)
        formatted_rows = re.sub(name_pattern_raw, name_pattern_new, rows_as_string)
        rows_as_list = formatted_rows.split(',')
        contacts_list_updated.append(rows_as_list)
    return contacts_list_updated


def format_number(contacts_list):
    number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                            r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                            r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    contacts_list_updated = []
    for rows in contacts_list:
        rows_as_string = ','.join(rows)
        formatted_rows = re.sub(number_pattern_raw, number_pattern_new, rows_as_string)
        rows_as_list = formatted_rows.split(',')
        contacts_list_updated.append(rows_as_list)
    return contacts_list_updated


def merge_duplicates(contacts_list):
    for i in contacts_list:
        contacts_list_updated = []
        for j in contacts_list:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                if i[2] == '':
                    i[2] = j[2]
                if i[3] == '':
                    i[3] = j[3]
                if i[4] == '':
                    i[4] = j[4]
                if i[5] == '':
                    i[5] = j[5]
                if i[6] == '':
                    i[6] = j[6]          
    for rows in contacts_list:
        if rows not in contacts_list_updated and len(rows) < 8:
            contacts_list_updated.append(rows)
    return contacts_list_updated


def write_file(contacts_list):
	with open("phonebook.csv", "w", newline='', encoding='utf-8', ) as f:
		datawriter = csv.writer(f)
		datawriter.writerows(contacts_list)


if __name__ == '__main__':
    contacts = read_file(file_path)
    contacts = format_full_name(contacts)
    contacts = format_number(contacts)
    contacts = merge_duplicates(contacts)
    write_file(contacts)