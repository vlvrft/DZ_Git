
f_name = r"C:\\Geek\nginx_logs.txt"
result = []
d = dict()

with open(f_name, "r", encoding="utf-8") as f:
    for file in f:
        file_1 = file.split()
        ip = file_1[0]
        result.append(ip)
        if ip not in d:
            d[ip] = 1
        else:
            d[ip] += 1
print('\n'.join(result))


m = 0
k = ''
for key, value in d.items():
    if value > m:
        m = value
        k = key
print(k, m)