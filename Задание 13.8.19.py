n = int(input('Введите количество билетов: '))
sum_total = 0
for i in range(1, n + 1):
    age = int(input('Введите возраст посетителя: '))
    if age < 18:
        sum_total += 0
    elif 18 <= age <25:
        sum_total += 990
    elif age >= 25:
        sum_total += 1390
if n > 3:
    sum_total -= sum_total * 0.1
print(sum_total)