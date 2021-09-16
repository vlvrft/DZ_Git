
f_name = r"C:\\Geek\nginx_logs.txt"
result = []

with open(f_name, "r", encoding="utf-8") as f:
    for file in f:
        file_1 = file.split()
        result.append((file_1[0], file_1[5].strip('"'), file_1[6]))
print('\n'.join(map(str, result)))

