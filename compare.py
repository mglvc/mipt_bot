# import pandas as pd
import csv
from difflib import SequenceMatcher
#from nltk.corpus import stopwords

from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

#Create lemmatizer and stopwords list
mystem = Mystem() 
russian_stopwords = stopwords.words("russian")

#Preprocess function
def preprocess_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords\
              and token != " " \
              and token.strip() not in punctuation]
    
    text = " ".join(tokens)
    
    return text

file_name = 'faq.csv'
NO_RESULT = "Ничего не найдено по вашему вопросу, вы можете задать вопрос по " \
            "ссылке https://pk.mipt.ru/faq/"


def compare(question):
    global Answer, Answer2, Answer3, Answer4, Answer5, Score, Score2, Score3, Score4, Score5, rawdata, result
    maxim = 0
    x = 0
    Answer, Answer2, Answer3, Answer4, Answer5 = '', '', '', '', ''
    Score, Score2, Score3, Score4, Score5 = 0, 0, 0, 0, 0
    with open(file_name, encoding='utf-8', newline='') as csvfile:
        df = csv.reader(csvfile, delimiter=';')
        #print(df[1][2])
        for row in df:
            # print(i)
            # print(df[x-1:x])
            # if row[2]:
            #     s = SequenceMatcher(lambda x: x == " ", question, row[2])
            # else:
            for i in range (1,4):
                #global Answer, Answer2, Answer3, Answer4, Answer5, Score, Score2, Score3, Score4, Score5, rawdata, maxim
                #maxim = 0
                s = SequenceMatcher(lambda x: x == " ", question, str(i))
                ratio = s.ratio()
                if ratio > maxim:
                    Answer5, Score5 = Answer4, Score4
                    Answer4, Score4 = Answer3, Score3
                    Answer3, Score3 = Answer2, Score2
                    Answer2, Score2 = Answer, Score
                    Answer = row[1:]
                    Score = ratio
                    maxim = ratio
                    rawdata = row

            x += 1
            print(x)
    result = [Answer, Score, Answer2, Score2, Answer3, Score3, Answer4, Score4, Answer5, Score5, rawdata]
    #print(result)
    if Score >= 0.21:
        quest = list()
        for i in range(3):
            print("results:", result[i * 2], result[i * 2 + 1])
            if result[i * 2 + 1] >= 0.2:
                quest.append(
                    [result[i * 2][1] if result[i * 2][1] else result[i * 2][0],
                     result[i * 2][2]])
        return quest
    return NO_RESULT


if __name__ == "__main__":
    question = preprocess_text("Какой проходной балл нужен для поступления?")
    print(compare(question), '\n', '\n запрос первого резулта')
 
    print( '\n', '\n')
    #print('\n', '\n', Answer, Score, '\n', Answer2, Score2, '\n', Answer3, Score3, '\n', Answer4, Score4, '\n', Answer5, Score5, '\n', rawdata, '\n')
