from bs4 import BeautifulSoup
import requests

import csv
import re


def csv_writer(data, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            writer.writerow(line)

def parse_stat():
    URL = 'https://pk.mipt.ru/bachelor/statistics/2019_statistics/'
    page = requests.get(URL)

    soup  = BeautifulSoup(page.content, 'html.parser')
    table = soup.find(id='wrapper').find('tbody')

    table_elems = table.findAll('tr')[2:]

    data = {}
    direct = 'ErrDir'
    fac = 'ErrFac'
    ind_of_content_group = 1

    for el in table_elems:
        if el.find('strong'):
            direct = el.find('strong').text
            continue

        parse_data = el.findAll('p')
        if len(parse_data) == 10:
            fac = parse_data[0].text
            ind_of_content_group = 1
        else:
            ind_of_content_group = 0
        data[parse_data[ind_of_content_group].text] = {
                    'direct':    direct,
                    'fac':       fac,
                    'score':     parse_data[-2].text,
                    'score_cel': parse_data[-1].text
                }

    return data


def parse_faq():
    URL = 'https://pk.mipt.ru/faq/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    questions = soup.find(id='question_list')
    q_list = questions.findAll('div', class_='q_question')
    a_list = questions.findAll('div', class_='t_answer')

    q_dict = {
            "Бакалавриат": [],
            "Магистратура": [],
            "Прочее": []
        }

    for quest, ans in zip(q_list, a_list):
        q_cat = str(quest.find('div', class_='q_cat').text)
        if not q_cat in ["Бакалавриат", "Магистратура"]:
            q_cat = "Прочее"
        q_date        = re.sub(r'\s+', ' ', quest.find('span', class_='q_date').text)
        q_title       = re.sub(r'\s+', ' ', quest.find('div',  class_='q_title').text)
        q_description = re.sub(r'\s+', ' ', quest.find('div',  class_='q_description').text)

        q_dict[q_cat].append(
                {
                    "date":        q_date,
                    "title":       q_title,
                    "description": q_description,
                    "ans":         re.sub(r'\s+', ' ', ans.text)
                }
            )

    return q_dict


def relist(lst):
    data = []
    for key, value in lst.items():
        for el in value:
            data.append([key, el['title'], el['description'], el['ans']])

    return data

def relist_data(lst):
    data = []
    for key, value in lst.items():
        data.append([key] + list(value.values()))

    return data

#
#
#  def main():
#      #  faq = parse_faq()
#      #  csv_writer(relist(faq), "faq.csv")
#      scores = parse_stat()
#      csv_writer(relist_data(scores), 'sc.csv')
#
#
#
#  if __name__ == '__main__':
#      main()
