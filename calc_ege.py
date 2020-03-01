import csv
import re


def calc_ege(subjects, csv_path='data/sc.csv', budget_flag=0):
    subjs = {
            "информатика": "info",
            "физика": "phys",
            "биология": "bio",
            "химия": "chem"
        }

    var_ret = []

    score_cur = subjects["math"] + subjects["russ"]
    stand_score = score_cur
    with open(csv_path, newline='') as csvfile:
        passing = 1e9
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            score_cur = stand_score
            row = [re.sub(r'\s+', ' ', el) for el in row]

            add_subs = row[-1].split()
            for sub in add_subs:
                score_cur += subjects[subjs[sub]]

            if budget_flag == 0: # budget
                passing = int(row[-3])
            else: # contract
                passing = int(row[-2])

            row[-2] = 'Проходные:\n- Контракт: ' + row[-2] + ";\n"
            row[-3] = '- Бюджет: '               + row[-3] + ";\n"

            if score_cur + 10 >= passing:
                var_ret.append(row + [str(score_cur)])

    return var_ret



def main():
    subjs = {
            "math": 98,
            "russ": 100,
            "info": 100,
            "phys": 78,
            "bio" : 100,
            "chem": 0
        }
    data = calc_ege(subjs, "data/sc.csv", 0)
    for el in data:
        print(el, sep='\n-------------------------------------------\n', end='\n\n===========================================================\n\n')


if __name__ == '__main__':
    main()
