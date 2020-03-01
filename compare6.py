# import pandas as pd
import csv
from difflib import SequenceMatcher
#from nltk.corpus import stopwords

# from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

#Create lemmatizer and stopwords list
mystem = Mystem()

#Preprocess function
def preprocess_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if #if token not in russian_stopwords\
              token != " " \
              and token.strip() not in punctuation]
    
    text = " ".join(tokens)
    
    return text
#file_name = 'data/faq.csv'
file_name = 'faq_clean.csv'
NO_RESULT = "Ничего не найдено по вашему вопросу, вы можете задать вопрос по " \
            "ссылке https://pk.mipt.ru/faq/"


def compare(question):
    global Answer,Answer2,Answer3,Answer4,Answer5,Score,Score2,Score3,Score4,Score5, Index, Index2, Index3, Index4, Index5, rawdata, result
    maxim = 0
    x = 0
    Answer, Answer2, Answer3, Answer4, Answer5 = '', '', '', '', ''
    Score, Score2, Score3, Score4, Score5 = 0, 0, 0, 0, 0
    Ind, Index,Index2,Index3,Index4,Index5 = 0, 0,0,0,0,0
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
                s = SequenceMatcher(lambda x: x == " ", question, str(row[i]))
                ratio = s.ratio()
                if ratio > maxim:
                    Answer5, Score5, Index5 = Answer4, Score4, Index4
                    Answer4, Score4, Index4 = Answer3, Score3, Index3
                    Answer3, Score3, Index3 = Answer2, Score2, Index2
                    Answer2, Score2, Index2 = Answer, Score, Index
                    Answer = row[1:]
                    Index = Ind
                    Score = ratio
                    maxim = ratio
                    rawdata = row

            Ind+=1
            #print(Ind, Index,Index2,Index3,Index4,Index5)
            #x += 1
    result = [Answer, Score, Index,  Answer2, Score2, Index2,  Answer3, Score3, Index3, Answer4, Score4, Index4, Answer5, Score5, Index5, rawdata]
    #print(result)
    if Score >= 0.21:
        quest = list()
        for i in range(3):
            print("results:", result[i * 3], result[i * 3 + 1])
            if result[i * 3 + 1] >= 0.2:
                quest.append(
                    [result[i * 3][1] if result[i * 3][1] else result[i * 2][0],
                     result[i * 3][2]])
        return quest
    return NO_RESULT


if __name__ == "__main__":
    question = preprocess_text("Какой проходной балл нужен для поступления?")
    print(question, '\n')
    print(compare(question), '\n')
    
    print('\n', '\n', Answer, Score, Index, '\n', Answer2, Score2, Index2, '\n', Answer3, Score3, Index3, '\n', Answer4, Score4, Index4, '\n', Answer5, Score5, Index5, '\n', rawdata, '\n')
