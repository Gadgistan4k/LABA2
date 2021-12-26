import csv

questions = ('Введите минимальный рейтинг аниме:',
             'Введите желаемые жанры (через запятую):',
             'Введите не желательные предупреждения (через запятую):',
             'Введите формат показа:',
             'Введите минимальное количество эпизодов:',
             'Введите год выпуска:',
             'Введите год окончания:',
             'Введите минимальное количство сезонов:',
             'Введите студию:')

answers = {'Rating Score': '',
           'Tags': '',
           'Content Warning': '',
           'Type': '',
           'Episodes': '',
           'StartYear': '',
           'EndYear': '',
           'Season': '',
           'Studios': ''}

all_anime = []
with open('anime.csv', newline='', encoding='utf-8') as csvfile:
    reader = list(csv.DictReader(csvfile, delimiter=','))
    for row in reader:
        all_anime.append(row['Name'])

print('Пройдите опрос (если пункт не важен, нажмите Enter)')
answer = []
for i in questions:
    n = input(i)
    answer.append(n)
answer = dict(zip(answers, answer))


def filter_1(parametr):
    anime = []
    for row in reader:
        if (row[parametr] < answer[parametr]) and (answer[parametr] != ''):
            anime.append(row['Name'])
    return anime


def filter_2(parametr):
    anime = []
    for row in reader:
        k = 0
        for m in answer:
            if m in row[parametr]:
                k = k+1
        if k != len(answer) and answer[parametr] != '':
            anime.append(row['Name'])
    return anime


def filter_3(parametr):
    anime = []
    for row in reader:
        if (row[parametr] != answer[parametr]) and (answer[parametr] != ''):
            anime.append(row['Name'])
    return anime


def filter_4(parametr):
    anime = []
    for row in reader:
        if (answer[parametr] not in row[parametr]) and (answer[parametr] != ''):
            anime.append(row['Name'])
    return anime


anime_rai = filter_1('Rating Score')
anime_tag = filter_2('Tags')
anime_cont = filter_2('Content Warning')
anime_type = filter_3('Type')
anime_epi = filter_1('Episodes')
anime_start = filter_4('StartYear')
anime_end = filter_4('EndYear')
anime_seas = filter_1('Season')
anime_stu = filter_3('Studios')

for bad in (anime_stu, anime_seas, anime_end, anime_start, anime_epi, anime_type, anime_cont, anime_tag, anime_rai):
    for ani in bad:
        if ani in all_anime:
            all_anime.remove(ani)

if len(all_anime) != 0:
    with open("youranime.txt", 'w', encoding='utf-8') as res:
        for i in all_anime:
            res.write(f'{i}\n')
    print('Аниме с вашими характеристиками здесь - "youranime.txt"')
else:
    print('Вы настолько индивидуален, что мы не нашли аниме для вас((')
