time = '1h 45m,360s,25m,30m 120s,2h 60s'
lst = time.split(',')
print(lst)

lst2=[]

for i in range(len(lst)):  
    lst2.append(lst[i].split(' ')) 

sum = 0
for ls in lst2:
    for i in ls:
        if 'h' in i:
            sum = sum + int(i.replace('h', '')) * 60
        elif 'm' in i:
            sum = sum + int(i.replace('m', ''))
        elif 's' in i:
            sum = sum + int(i.replace('s', ''))/60

print(sum)


time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

# Разбиваем строку на отдельные временные значения
time_parts = time_string.split(',')

total_minutes = 0

for part in time_parts:
    # Разбиваем каждое значение на составляющие (часы, минуты, секунды)
    units = part.split()
    minutes = 0
    
    for unit in units:
        if 'h' in unit:
            # Часы переводим в минуты
            hours = int(unit.replace('h', ''))
            minutes += hours * 60
        elif 'm' in unit:
            # Минуты оставляем как есть
            mins = int(unit.replace('m', ''))
            minutes += mins
        elif 's' in unit:
            # Секунды (кратные 60) переводим в минуты
            seconds = int(unit.replace('s', ''))
            minutes += seconds // 60
    
    total_minutes += minutes

print(f"Общее количество минут: {total_minutes}")

   
