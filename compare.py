# import pandas as pd
import csv
from difflib import SequenceMatcher

from string import punctuation


# Preprocess function
def preprocess_text(text):
    new_text = ''
    for symb in text:
        if symb not in punctuation:
            new_text += symb.lower()
    return new_text


file_name = 'data/faq_clean.csv'
raw_data = 'data/faq.csv'
NO_RESULT = "Ничего не найдено по вашему вопросу, вы можете задать вопрос по " \
            "ссылке https://pk.mipt.ru/faq/"


def find_in_csv(indexes):
    res = list()
    with open(raw_data, encoding='utf-8', newline='') as csvfile:
        df = csv.reader(csvfile, delimiter=';')
        for i, row in enumerate(df):
            if i in indexes:
                res.append(row)
    return res


def compare(question):
    question = preprocess_text(question)
    global Answer, Answer2, Answer3, Answer4, Answer5, Score, Score2, Score3, Score4, Score5, rawdata, result
    maxim = 0
    Answer, Answer2, Answer3, Answer4, Answer5 = '', '', '', '', ''
    Score, Score2, Score3, Score4, Score5 = 0, 0, 0, 0, 0
    indexes = [0 for _ in range(5)]
    with open(file_name, encoding='utf-8', newline='') as csvfile:
        df = csv.reader(csvfile, delimiter=';')
        # print(df[1][2])
        for j, row in enumerate(df):
            for i in range(1, 4):
                # global Answer, Answer2, Answer3, Answer4, Answer5, Score, Score2, Score3, Score4, Score5, rawdata, maxim
                # maxim = 0
                s = SequenceMatcher(lambda x: x == " ", question, str(row[i]))
                ratio = s.ratio()
                if ratio > maxim:
                    Answer5, Score5, indexes[4] = Answer4, Score4, indexes[3]
                    Answer4, Score4, indexes[3] = Answer3, Score3, indexes[2]
                    Answer3, Score3, indexes[2] = Answer2, Score2, indexes[1]
                    Answer2, Score2, indexes[1] = Answer, Score, indexes[0]
                    Answer = row[1:]
                    Score = ratio
                    maxim = ratio
                    indexes[0] = j
                    rawdata = row

    result = [Answer, Score, Answer2, Score2, Answer3, Score3, Answer4, Score4,
              Answer5, Score5, rawdata]
    # print(result)
    # print(indexes)
    if Score >= 0.21:

        res = find_in_csv(indexes)
        # print(res)
        quest = list()
        find_in_csv(indexes)
        for i in range(3):
            # print("results:", res[i], result[i * 2 + 1])
            if result[i * 2 + 1] >= 0.2:
                quest.append(
                    [res[i][2] if res[i][2] else res[i][1],
                     res[i][3]])
        return quest
    return NO_RESULT


if __name__ == "__main__":
    question = "Какой проходной балл нужен для поступления?"
    print(compare(question), '\n', '\n запрос первого резулта')

    # print('\n', '\n')
    # print('\n', '\n', Answer, Score, '\n', Answer2, Score2, '\n', Answer3, Score3, '\n', Answer4, Score4, '\n', Answer5, Score5, '\n', rawdata, '\n')
