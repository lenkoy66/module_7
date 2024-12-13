#Соревнование: Мастера кода и Волшебники данных
team1_num = 5
team2_num = 6

score_1 = 40
score_2 = 42

team1_time = 1552.512
team2_time = 2153.31451

tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / tasks_total, 1)
#%
print("В команде Мастера кода участников: %s !" %team1_num)
print("В команде Волшебники данных участников: %s !" %team2_num)
print('Итого сегодня в командах участников: %(first)s и %(second)s !' % {'first': team1_num, 'second': team2_num})

#format
print('-----------------')
print('Команда Мастера кода решила задач: {} !'.format(score_1))
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Мастера кода решили задачи за {} с!'.format(team1_time))
print('Волшебники данных решили задачи за {} с!'.format(team2_time))

#f-строка
print('-----------------')
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 and team1_time > team2_time:
    result = 'победа команды Мастера кода!'
elif score_1 < score_2 and team1_time < team2_time:
    result = 'победа команды Волшебники данных!'
else:
    result = 'ничья!'
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу.')
