import pandas as pd

data = {
    'names': ['Иванов', 'Петров', 'Сидоров', 'Палянко', 'Дударев', 'Казанцев', 'Осипова', 'Грибко', 'Бикренев', 'Моисеев'],
    'mathematics': [7, 9, 6, 4, 2, 8, 2, 5, 7, 3],
    'Belarusian language': [6, 7, 8, 5, 4, 9, 6, 8, 5, 7],
    'biology': [8, 5, 7, 6, 4, 7, 3, 6, 7, 9],
    'chemistry': [5, 6, 7, 5, 3, 8, 4, 5, 7, 6],
    'Russian literature': [7, 8, 5, 6, 6, 7, 8, 9, 6, 5],
}

df = pd.DataFrame(data)
print(df.head(6))

df = df.drop(columns='names')

subject_list = list(df.columns)

print(f'\n~ СРЕДНЯЯ ОЦЕНКА ~')
for subject in subject_list:
    print(f'Средняя оценка по предмету: "{subject}" - {df[subject].mean()}')

print(f'\n~ МЕДИАННАЯ ОЦЕНКА ~')
for subject in subject_list:
    print(f'Медианная оценка по предмету: "{subject}" - {df[subject].median()}')

Q1_math = df['mathematics'].quantile(0.25)
Q3_math = df['mathematics'].quantile(0.75)
IQR = Q3_math - Q1_math

print(f'\n~ КВАРТИЛИ ПО МАТЕМАТИКЕ ~')
print(f'Q1 по математике - {Q1_math}')
print(f'Q3 по математике - {Q3_math}')
print(f'межквартальный размах - {IQR}')

print(f'\n~ СТАНДАРТНОЕ ОТКЛОНЕНИЕ ~')
for subject in subject_list:
    print(f'Стандартное отклонение по предмету: "{subject}" - {df[subject].std()}')