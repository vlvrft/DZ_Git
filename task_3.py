import sys
import json

f_name_usr = r"C:\\Geek\users.csv"
f_name_hbb = r"C:\\Geek\hobby.csv"
result_dict = dict()

with open(f_name_usr, 'r', encoding='utf-8') as f1, \
        open(f_name_hbb, 'r', encoding='utf-8') as f2:
    for line1 in f1:
        line2 = f2.readline().strip()
        if not line2:
            line2 = None
        if line1 not in result_dict:
            result_dict[line1.strip()] = line2
    content = f2.read()
    if content:
        sys.exit(1)

with open('result.json', 'w', encoding='utf-8') as result_file:
    dict_as_string = json.dumps(result_dict, ensure_ascii=False)
    result_file.write(dict_as_string)
with open('result.json', 'r', encoding='utf-8') as f:
    content = f.read()
    result = json.loads(content)
print(result)

