import csv

f = open('vacancy.csv', 'r', encoding='utf8')
r = csv.DictReader(f, delimiter=';')
a = []
for k in r:
    a.append((k['Company'], k['Role'], k['\ufeffSalary']))
a = sorted(a, key=lambda i: i[2], reverse=True)
nf = open('vacancy_new.csv', 'w', encoding='utf8', newline='')
n_v = csv.writer(nf, delimiter=';')
n_v.writerow(['company', 'role', 'Salary'])
for el in a:
    n_v.writerow(el)
f.close()
nf.close()

nnf = open('vacancy_new.csv', 'r', encoding='utf8')
nnr = csv.DictReader(nnf, delimiter=';')
c = 0
n = 3
for string in nnr:
    c += 1
    if c <= n:
        print(f'<{string["company"]}> - <{string["role"]}> - <{string["Salary"]}>')
    else:
        break
