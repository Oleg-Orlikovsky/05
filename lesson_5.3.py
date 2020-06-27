with open('prem.txt', 'r') as my_file:
    prem = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[2]) < 20000:
             poor.append(i[1])
        prem.append(i[2])
print(f'Оклад меньше 20000 {poor}, средний оклад {sum(map(int, prem)) / len(prem)}')
