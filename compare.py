from difflib import SequenceMatcher
import pandas as pd
file_name = 'faq.csv'
df = pd.read_csv(file_name, sep=';', header=None, names=['type', 'title', 'question', 'answer'])
df['answer'].str.lower()

QuestionUser = "выдаются ли общежития на время поступления"



def compare():
    global Answer,Answer2,Answer3,Answer4,Answer5,Score,Score2,Score3,Score4,Score5, rawdata
    maxim = 0
    x = 0
    Answer,Answer2,Answer3,Answer4,Answer5 = '','','','',''
    Score,Score2,Score3,Score4,Score5 = 0,0,0,0,0
    for i in df['question']:
        #print(i)
        #print(df[x-1:x])
        s = SequenceMatcher(lambda x: x==" ", QuestionUser, str(i)) 
        ratio = s.ratio()
        if ratio > maxim: 
            Answer5, Score5 = Answer4, Score4
            Answer4, Score4 = Answer3, Score3
            Answer3, Score3 = Answer2, Score2
            Answer2, Score2 = Answer, Score
            Answer = str(i)
            Score = ratio
            maxim = ratio
            rawdata = [df[x:x+1],x]
            
    
        x+=1
    result = [Answer, Score,  Answer2, Score2,  Answer3, Score3,  Answer4, Score4,  Answer5, Score5,  rawdata]
    return result

compare()    
print(Answer, Score, '\n', Answer2, Score2, '\n', Answer3, Score3, '\n', Answer4, Score4, '\n', Answer5, Score5, '\n', rawdata, '\n')


