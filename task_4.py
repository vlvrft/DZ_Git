import sys

f_name_usr = r"C:\\Geek\users.csv"
f_name_hbb = r"C:\\Geek\hobby.csv"
result_dict = dict()
with open(f_name_usr, 'r', encoding='utf-8') as f1, \
        open(f_name_hbb, 'r', encoding='utf-8') as f2, \
        open('usr_hbb.txt', 'w', encoding='utf-8') as f3:
    for line1 in f1:
        line2 = f2.readline().strip()
        if not line2:
            line2 = None
        f3.write(f'{line1.strip()}: {line2}\n')
    content = f2.readline()
    if content:
        sys.exit(1)
