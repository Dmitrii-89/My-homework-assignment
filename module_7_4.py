name_1 = 'Мастера кода'
name_2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды!'


print('В команде %s участников: %s!' % (name_1, team1_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

print('Команда {} решила задач: {}!'.format(name_2, score_2))
print('{0} решили задачи за {1} с!'.format(name_2, team1_time))

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: победа команды {name_1}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')